from typing import List
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from .services import riot_api
from players.models import Player
from matches.models import Match
from player_stats.models import PlayerStats
import json

# Create your views here.
def get_puuid(request, summoner_name):
    try:
        # TODO - make this a POST request since it's setting db data
        puuid = riot_api.get_summoner(summoner_name)['puuid']
        player, created = Player.objects.update_or_create(puuid = puuid, defaults = {'name': summoner_name})

        return JsonResponse({'puuid': puuid, 'created': created})

    except Exception as e:
        print(f'Exception {e}')
        return HttpResponse('')


# TODO - add region
# Returns a list of matches with this information: 
#   game mode
#   timestamp
#   length of game
#   win/loss
#   kills, deaths, assists
#   champion, champion level
#   items
#   control wards (?), maybe ward score
#   cs
#   rank
#   names of the other players & roles
def get_last_matches(request, summoner_name, count):
    # Put count between 1 and 5
    count = max(1, count)
    count = min(20, count)

    try:
        puuid = riot_api.get_summoner(summoner_name)['puuid']

        # Update the Player table with most updated summoner name
        Player.objects.update_or_create(puuid=puuid, defaults = {'name': summoner_name})

        result = riot_api.get_match_list(puuid=puuid, count=count)
        matches = []
        for match_id in result: 
            match, _ = get_or_create_match(match_id)
            matches.append(match)

        ser = {'matches': []}
        match: Match = None
        for match in matches:
            ser['matches'].append(
                {
                    'gameMeta': get_game_metadata(match),
                    'playerData': get_player_stats(match, puuid),
                    'gameSummary': get_game_summary(match)
                }
            )

        return JsonResponse(ser)

    except Exception as e:
        print(f'Exception {e}')
        return HttpResponse("")

def get_game_summary(match):
    # Retrieve all player statistics for the specified match
    player_stats_list = PlayerStats.objects.filter(match_id=match)

    # Calculate the total kills by summing up kills from each player
    total_kills = sum(player_stats.kills for player_stats in player_stats_list)

    # Extract summoner names, team positions, and champions for each player
    player_summary = []
    for player_stats in player_stats_list:
        summary_entry = {
            'name': player_stats.summonerName,
            'role': player_stats.teamPosition,
            'champion': player_stats.championName,
        }
        player_summary.append(summary_entry)

    # Create the final summary dictionary
    game_summary = {
        'totalKills': total_kills,
        'playerSummary': player_summary,
    }

    return game_summary

def get_game_metadata(match):
    # Extract game metadata from the specified match
    metadata_dict = {
        'gameDuration': match.gameDuration,
        'gameStartTimestamp': match.gameStartTimestamp,
        'gameVersion': match.gameVersion,
        'mapId': match.mapId,
        'platformId': match.platformId,
        'queueId': match.queueId,
    }

    # Adjust gameDuration if gameEndTimestamp is None
    if match.gameEndTimestamp is None:
        metadata_dict['gameDuration'] /= 1000

    return metadata_dict

def get_player_stats(match, puuid):
    # Retrieve player statistics for the specified match and puuid
    player_stats = PlayerStats.objects.filter(match_id=match, puuid=puuid).first()

    if player_stats:
        # Extract desired fields from the player_stats instance
        stats_dict = {
            'win': player_stats.win,
            'kills': player_stats.kills,
            'deaths': player_stats.deaths,
            'assists': player_stats.assists,
            'champion': player_stats.championName,
            'champion_level': player_stats.champLevel,
            'items': [player_stats.item0, player_stats.item1, player_stats.item2,
                      player_stats.item3, player_stats.item4, player_stats.item5, player_stats.item6],
            'control_wards': player_stats.visionWardsBoughtInGame,
            # Add more fields as needed
        }
        return stats_dict
    else:
        # Return an empty dictionary if PlayerStats not found
        return {}


def create_playerstats_instance(match, match_json):
    participant_list = match_json['info']['participants']

    for p in participant_list:
        puuid = p['puuid']
        name = p['summonerName']
        player, _ = Player.objects.get_or_create(puuid = puuid, defaults = {'name': name})
        PlayerStats.create_from_json(match, player, p)

# Helpers
def get_or_create_match(match_id) -> (Match, bool):
    match = Match.objects.filter(match_id=match_id)
    if match.exists() == False:
        match_json = riot_api.get_match(match_id)
        match = Match.create_from_json(match_id, match_json['info'])
        create_playerstats_instance(match, match_json)
        return match, True
    
    return match.first(), False

