from config import riot_api_key
import json
import requests
import time
import sys

base_url_lol_na1 = "https://na1.api.riotgames.com"
base_url_lol_americas = "https://americas.api.riotgames.com"
base_url_datadragon = "https://ddragon.leagueoflegends.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": riot_api_key
}

def rate_limit(endpoint):
    print("Requesting " + endpoint)
    r = requests.get(endpoint, headers=headers)
    if r.status_code == 429:
        print("Rate limit exceeded. Waiting 2 minutes...")
        time.sleep(120)
        r = requests.get(endpoint, headers=headers)
    elif r.status_code == 403:
        print("API key invalid. Exiting...")
        sys.exit()
    time.sleep(0)
    return r

def get_game_version():
    r = requests.get(base_url_datadragon + "/api/versions.json")
    return json.loads(r.text)[0]

def get_summoner_name_from_id(puuid):
    r = rate_limit(base_url_lol_na1 + "/lol/summoner/v4/summoners/by-puuid/" + puuid)
    return json.loads(r.text)["name"]

def get_summoner_account_data(summoner):
    r = rate_limit(base_url_lol_na1 + "/lol/summoner/v4/summoners/by-name/" + summoner)
    return json.loads(r.text)

def get_summoner_ranked_data(summoner):
    r = rate_limit(base_url_lol_na1 + "/lol/league/v4/entries/by-summoner/" + summoner.account_data.id)
    data = json.loads(r.text)
    if len(data) == 0:
        return {}
    return json.loads(r.text)[0]

def get_summoner_mastery_data(summoner, count):
    r = rate_limit(base_url_lol_na1 + "/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner.account_data.id + "/top" + "?count=" + str(count))
    data = json.loads(r.text)
    if len(data) == 0:
        return []
    return data

def get_champion_data(champion_id):
    r = requests.get(base_url_datadragon + "/cdn/" + get_game_version() + "/data/en_US/championFull.json")
    data = json.loads(r.text)["data"]
    for champ in data:
        if champion_id == int(data[champ]["key"]):
            return data[champ]
            
def get_match_data(match_id):
    r = rate_limit(base_url_lol_americas + "/lol/match/v5/matches/" + match_id)
    return json.loads(r.text)

def get_matches_by_puuid(puuid, count):
    r = rate_limit(base_url_lol_americas + "/lol/match/v5/matches/by-puuid/" + puuid + "/ids" + "?count=" + str(count))
    return json.loads(r.text)