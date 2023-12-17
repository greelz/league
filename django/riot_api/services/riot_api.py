import requests
from enum import Enum

class QueueType(Enum):
    RANKED5V5 = 420

class Platforms(Enum):
    BR1 = 'br1'
    EUN1 = 'eun1'
    EUW1 = 'euw1'
    JP1 = 'jp1'
    KR = 'kr'
    LA1 = 'la1'
    LA2 = 'la2'
    NA1 = 'na1'
    OC1 = 'oc1'
    TR1 = 'tr1'
    RU = 'ru'
    PH2 = 'ph2'
    SG2 = 'sg2'
    TH2 = 'th2'
    TW2 = 'tw2'
    VN2 = 'vn2'

class TeamPosition(Enum):
    TOP = 'Top'
    JUNGLE = 'Jungle'
    MIDDLE = 'Mid'
    BOTTOM = 'Bot'
    UTILITY = 'Support'

class Regions(Enum):
    AMERICAS = 'americas'
    ASIA = 'asia'
    EUROPE = 'europe'
    SEA = 'sea'

def region_from_platform(platform):
    if platform in [Platforms.NA1.value, Platforms.BR1.value, Platforms.LA1.value, Platforms.LA2.value]:
        return Regions.AMERICAS.value
    if platform in [Platforms.KR.value, Platforms.JP1.value]:
        return Regions.ASIA.value
    if platform in [Platforms.EUN1.value, Platforms.EUW1.value, Platforms.TR1.value, Platforms.RU.value]:
        return Regions.EUROPE.value
    if platform in [Platforms.OC1.value, Platforms.PH2.value, Platforms.SG2.value, 
                    Platforms.TH2.value, Platforms.TW2.value, Platforms.VN2.value]:
        return Regions.SEA.value
    return None

API_KEY = 'RGAPI-1b563ac1-206e-4c71-8202-3ff527dd6894'

######################### CORE API ##################################
# Function to get summoner ID by summoner name
def get_match_list(puuid, queue = None, region=Regions.AMERICAS.value, count = 10):
    queue_url = ""
    if queue is not None:
        queue_url = f'queue={queue}'
    url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?{queue_url}&count={count}'
    headers = {'X-Riot-Token': API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error getting match list: {response.status_code}")
        return None

# Function to get summoner ID by summoner name
def get_summoner(summoner_name, platform=Platforms.NA1.value):
    url = f'https://{platform}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
    headers = {'X-Riot-Token': API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error getting summoner ID: {response.status_code}")
        return None

def get_match(match_id, region=Regions.AMERICAS.value):
    url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}'
    headers = {'X-Riot-Token': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error getting match {match_id}: {response.status_code}")
        return None
#################### End of Core API ####################################

#################### API helpers / simplify ############################
def get_puuid(summoner_name, platform=Platforms.NA1.value):
    try:
        return get_summoner(summoner_name, platform)['puuid']
    except TypeError:
        return

def get_match_list_by_summoner_name(summoner_name, platform):
    return get_match_list(get_puuid(summoner_name, platform), None, region_from_platform(platform), 1)
###################### end of API helpers ##############################
