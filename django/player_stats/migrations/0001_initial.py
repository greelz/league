# Generated by Django 4.2.8 on 2023-12-17 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assists', models.IntegerField()),
                ('baronKills', models.IntegerField()),
                ('bountyLevel', models.IntegerField()),
                ('champExperience', models.IntegerField()),
                ('champLevel', models.IntegerField()),
                ('championId', models.IntegerField()),
                ('championName', models.CharField(max_length=255)),
                ('championTransform', models.IntegerField(choices=[(0, 'None'), (1, 'Slayer'), (2, 'Assassin')])),
                ('consumablesPurchased', models.IntegerField()),
                ('damageDealtToBuildings', models.IntegerField()),
                ('damageDealtToObjectives', models.IntegerField()),
                ('damageDealtToTurrets', models.IntegerField()),
                ('damageSelfMitigated', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('detectorWardsPlaced', models.IntegerField()),
                ('doubleKills', models.IntegerField()),
                ('dragonKills', models.IntegerField()),
                ('firstBloodAssist', models.BooleanField()),
                ('firstBloodKill', models.BooleanField()),
                ('firstTowerAssist', models.BooleanField()),
                ('firstTowerKill', models.BooleanField()),
                ('gameEndedInEarlySurrender', models.BooleanField()),
                ('gameEndedInSurrender', models.BooleanField()),
                ('goldEarned', models.IntegerField()),
                ('goldSpent', models.IntegerField()),
                ('individualPosition', models.CharField(max_length=255)),
                ('inhibitorKills', models.IntegerField()),
                ('inhibitorTakedowns', models.IntegerField()),
                ('inhibitorsLost', models.IntegerField()),
                ('item0', models.IntegerField()),
                ('item1', models.IntegerField()),
                ('item2', models.IntegerField()),
                ('item3', models.IntegerField()),
                ('item4', models.IntegerField()),
                ('item5', models.IntegerField()),
                ('item6', models.IntegerField()),
                ('itemsPurchased', models.IntegerField()),
                ('killingSprees', models.IntegerField()),
                ('kills', models.IntegerField()),
                ('lane', models.CharField(max_length=255)),
                ('largestCriticalStrike', models.IntegerField()),
                ('largestKillingSpree', models.IntegerField()),
                ('largestMultiKill', models.IntegerField()),
                ('longestTimeSpentLiving', models.IntegerField()),
                ('magicDamageDealt', models.IntegerField()),
                ('magicDamageDealtToChampions', models.IntegerField()),
                ('magicDamageTaken', models.IntegerField()),
                ('neutralMinionsKilled', models.IntegerField()),
                ('nexusKills', models.IntegerField()),
                ('nexusTakedowns', models.IntegerField()),
                ('nexusLost', models.IntegerField()),
                ('objectivesStolen', models.IntegerField()),
                ('objectivesStolenAssists', models.IntegerField()),
                ('participantId', models.IntegerField()),
                ('pentaKills', models.IntegerField()),
                ('physicalDamageDealt', models.IntegerField()),
                ('physicalDamageDealtToChampions', models.IntegerField()),
                ('physicalDamageTaken', models.IntegerField()),
                ('profileIcon', models.IntegerField()),
                ('quadraKills', models.IntegerField()),
                ('riotIdName', models.CharField(max_length=255)),
                ('riotIdTagline', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('sightWardsBoughtInGame', models.IntegerField()),
                ('spell1Casts', models.IntegerField()),
                ('spell2Casts', models.IntegerField()),
                ('spell3Casts', models.IntegerField()),
                ('spell4Casts', models.IntegerField()),
                ('summoner1Casts', models.IntegerField()),
                ('summoner1Id', models.IntegerField()),
                ('summoner2Casts', models.IntegerField()),
                ('summoner2Id', models.IntegerField()),
                ('summonerId', models.CharField(max_length=255)),
                ('summonerLevel', models.IntegerField()),
                ('summonerName', models.CharField(max_length=255)),
                ('teamEarlySurrendered', models.BooleanField()),
                ('teamId', models.IntegerField()),
                ('teamPosition', models.CharField(max_length=255)),
                ('timeCCingOthers', models.IntegerField()),
                ('timePlayed', models.IntegerField()),
                ('totalDamageDealt', models.IntegerField()),
                ('totalDamageDealtToChampions', models.IntegerField()),
                ('totalDamageShieldedOnTeammates', models.IntegerField()),
                ('totalDamageTaken', models.IntegerField()),
                ('totalHeal', models.IntegerField()),
                ('totalHealsOnTeammates', models.IntegerField()),
                ('totalMinionsKilled', models.IntegerField()),
                ('totalTimeCCDealt', models.IntegerField()),
                ('totalTimeSpentDead', models.IntegerField()),
                ('totalUnitsHealed', models.IntegerField()),
                ('tripleKills', models.IntegerField()),
                ('trueDamageDealt', models.IntegerField()),
                ('trueDamageDealtToChampions', models.IntegerField()),
                ('trueDamageTaken', models.IntegerField()),
                ('turretKills', models.IntegerField()),
                ('turretTakedowns', models.IntegerField()),
                ('turretsLost', models.IntegerField()),
                ('unrealKills', models.IntegerField()),
                ('visionScore', models.IntegerField()),
                ('visionWardsBoughtInGame', models.IntegerField()),
                ('wardsKilled', models.IntegerField()),
                ('wardsPlaced', models.IntegerField()),
                ('win', models.BooleanField()),
                ('allInPings', models.IntegerField(null=True)),
                ('assistMePings', models.IntegerField(null=True)),
                ('baitPings', models.IntegerField(null=True)),
                ('basicPings', models.IntegerField(null=True)),
                ('commandPings', models.IntegerField(null=True)),
                ('dangerPings', models.IntegerField(null=True)),
                ('eligibleForProgression', models.BooleanField(default=False)),
                ('enemyMissingPings', models.IntegerField(null=True)),
                ('enemyVisionPings', models.IntegerField(null=True)),
                ('getBackPings', models.IntegerField(null=True)),
                ('holdPings', models.IntegerField(null=True)),
                ('needVisionPings', models.IntegerField(null=True)),
                ('onMyWayPings', models.IntegerField(null=True)),
                ('placement', models.IntegerField(null=True)),
                ('playerAugment1', models.IntegerField(null=True)),
                ('playerAugment2', models.IntegerField(null=True)),
                ('playerAugment3', models.IntegerField(null=True)),
                ('playerAugment4', models.IntegerField(null=True)),
                ('playerScore0', models.IntegerField(null=True)),
                ('playerScore1', models.IntegerField(null=True)),
                ('playerScore2', models.IntegerField(null=True)),
                ('playerScore3', models.IntegerField(null=True)),
                ('playerScore4', models.IntegerField(null=True)),
                ('playerScore5', models.IntegerField(null=True)),
                ('playerScore6', models.IntegerField(null=True)),
                ('playerScore7', models.IntegerField(null=True)),
                ('playerScore8', models.IntegerField(null=True)),
                ('playerScore9', models.IntegerField(null=True)),
                ('playerScore10', models.IntegerField(null=True)),
                ('playerScore11', models.IntegerField(null=True)),
                ('playerSubteamId', models.IntegerField(null=True)),
                ('pushPings', models.IntegerField(null=True)),
                ('riotIdGameName', models.CharField(max_length=255, null=True)),
                ('subteamPlacement', models.IntegerField(null=True)),
                ('totalAllyJungleMinionsKilled', models.IntegerField(null=True)),
                ('totalEnemyJungleMinionsKilled', models.IntegerField(null=True)),
                ('visionClearedPings', models.IntegerField(null=True)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.match')),
                ('puuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.player')),
            ],
        ),
    ]
