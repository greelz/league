from django.db import models

# Create your models here.

class Match(models.Model):
    match_id = models.CharField(max_length=255, primary_key=True)
    gameCreation = models.BigIntegerField()
    gameDuration = models.BigIntegerField()
    gameEndTimestamp = models.BigIntegerField(null=True)
    gameId = models.BigIntegerField()
    gameMode = models.CharField(max_length=255)
    gameName = models.CharField(max_length=255)
    gameStartTimestamp = models.BigIntegerField()
    gameType = models.CharField(max_length=255)
    gameVersion = models.CharField(max_length=255)
    mapId = models.IntegerField()
    platformId = models.CharField(max_length=255)
    queueId = models.IntegerField()
    tournamentCode = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Match ID: {self.match_id}"

    @classmethod
    def create_from_json(cls, match_id, json_data):

        # json_data represents InfoDto from Riot's API
        filtered_data = {
            'gameCreation': json_data['gameCreation'],
            'gameDuration': json_data['gameDuration'],
            'gameEndTimestamp': json_data.get('gameEndTimestamp', None),
            'gameId': json_data['gameId'],
            'gameMode': json_data['gameMode'],
            'gameName': json_data['gameName'],
            'gameStartTimestamp': json_data['gameStartTimestamp'],
            'gameType': json_data['gameType'],
            'gameVersion': json_data['gameVersion'],
            'mapId': json_data['mapId'],
            'platformId': json_data['platformId'],
            'queueId': json_data['queueId'],
            'tournamentCode': json_data.get('tournamentCode', None),
        }

        # Unhandled keywords 
        instance = cls(match_id=match_id, **filtered_data)
        instance.save()

        return instance