from config import riot_api_key
import json
import requests

base_url_na1 = "https://na1.api.riotgames.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": riot_api_key
}

def get_summoner_account(summoner):
    r = requests.get(base_url_na1 + "/lol/summoner/v4/summoners/by-name/" + summoner.name, headers=headers)
    return json.loads(r.text)

def get_summoner_rank(summoner):
    r = requests.get(base_url_na1 + "/lol/league/v4/entries/by-summoner/" + summoner.id, headers=headers)
    return json.loads(r.text)[0]