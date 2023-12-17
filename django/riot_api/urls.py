from django.urls import path
from .views import get_puuid, get_last_matches

# URLConf
urlpatterns = [
    path('get_puuid/<str:summoner_name>/', get_puuid),
    path('get_matches/<str:summoner_name>/<int:count>/', get_last_matches)
]