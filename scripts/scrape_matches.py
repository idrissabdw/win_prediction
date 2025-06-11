import numpy as np
import requests
import time
from dotenv import load_dotenv
import os
import csv
import pandas as pd

# API Key setting
load_dotenv("api.env")
API_KEY = os.getenv("API_KEY")
headers = {"X-Riot-Token": API_KEY}

# Summoner's ID importation
puuid_list = []
region = "euw1"
with open("../data/raw/puuid_ids.cvs", "r", encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:  # éviter les lignes vides
            puuid_list.append(row[0])

# Games tracking & Featuring extraction
player_metrics = []
for player_puuid in puuid_list:
    match_number = 30 
    match_list_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{player_puuid}/ids?start=0&count={match_number}&queue=420"
    match_ids = requests.get(match_list_url, headers=headers).json()

    metrics = 8 # (KDA, CS/min, Gold/min, Damage/min, Damage taken/min, Vision Score, KP, Winrate  )
    stat_data = np.zeros((metrics,match_number))

    # Featuring Extraction Algorithm 
    for i, match_id in enumerate(match_ids):
        match_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}"
        match_data = requests.get(match_url, headers=headers).json()
        print(match_data)
        time_game = match_data['info']['gameDuration']/60
        
        for p in match_data['info']['participants']:
            if p['puuid'] == player_puuid:
                if p['deaths'] > 0 :
                    stat_data[0,i] = (p['kills']+p['assists'])/p['deaths']  # KDA
                else :
                    stat_data[0,i] = p['kills']+p['assists']
                
                stat_data[1,i] = (p['totalMinionsKilled']+p['neutralMinionsKilled'])/time_game  # CS/min
                stat_data[2,i] = p['goldEarned']/time_game  # Gold/min
                stat_data[3,i] = p['totalDamageDealtToChampions']/time_game  # Damage/min
                stat_data[4,i] = p['totalDamageTaken']/time_game # Damages taken
                stat_data[5,i] = p['visionScore']  # Vision Score
                stat_data[6,i] = p['challenges']['killParticipation'] # KP
                stat_data[7, i] = int(p['win'])

        time.sleep(1.5)  # Respect the rate limit !
        print("Tour :",i)
    player_stat = []
    for i in range (metrics):
        player_stat.append(round(np.mean(stat_data[i]),2))
    
    player_metrics.append(player_stat)

colomns = ['KDA', 'CS/min', 'Gold/min', 'Damage/min', 'DamageTaken/min', 'Vision Score', 'Kill Participation', 'Win Rate']

df = pd.DataFrame(player_metrics, index=puuid_list, columns=colomns)
df = df.T
df.to_csv("../raw/player_stats.csv", encoding="utf-8")