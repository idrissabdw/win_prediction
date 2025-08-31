import numpy as np
import requests
import time
from dotenv import load_dotenv
import os
import csv

# API Key setting
load_dotenv("api.env")
API_KEY = os.getenv("API_KEY")
headers = {"X-Riot-Token": API_KEY}

# Player scraping algorithm
players_summonerId_list = []
region = "euw1"
nb_pages = 20
for i in range (1,nb_pages):
    url = f'https://{region}.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/EMERALD/I?page={i}'
    users_data = requests.get(url, headers=headers).json()
    for player in users_data:
        players_summonerId_list.append(player['summonerId'])
    time.sleep(1.3)

puuid_list = []
for ids in players_summonerId_list:
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/{ids}"
    user_data = requests.get(url, headers=headers).json()
    user_puuid = user_data['puuid']
    puuid_list.append(user_puuid)
    time.sleep(1.3)

# Summoner's IDs saving
with open("../data/raw/summoner_ids.cvs", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for id in players_summonerId_list:
        writer.writerow([id])

# PUUID's IDs saving
with open("../data/raw/puuid_ids.cvs", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for id in puuid_list:
        writer.writerow([id])

 