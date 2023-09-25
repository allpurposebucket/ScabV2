import api
class Summoner:
    def __init__(self, name):
        self.name = name
        self.get_initial_data()
        self.get_ranked_data()

    def get_initial_data(self):
        data = api.get_summoner_account(self)
        self.id = data["id"]
        self.account_id = data["accountId"]
        self.encrypted_puuid = data["puuid"]
        self.profile_icon_id = data["profileIconId"]
        self.revision_date = data["revisionDate"]
        self.summoner_level = data["summonerLevel"]

    def get_ranked_data(self):
        data = api.get_summoner_rank(self)
        self.league_id = data["leagueId"]
        self.queue_type = data["queueType"]
        self.tier = data["tier"]
        self.rank = data["rank"]
        self.league_points = data["leaguePoints"]
        self.wins = data["wins"]
        self.losses = data["losses"]
        self.veteran = data["veteran"]
        self.inactive = data["inactive"]
        self.fresh_blood = data["freshBlood"]
        self.hot_streak = data["hotStreak"]


    def __str__(self):
        return f"id: {self.id}\naccountId: {self.account_id}\npuuid: {self.encrypted_puuid}\nname: {self.name}\nprofileIconId: {self.profile_icon_id}\nrevisionDate: {self.revision_date}\nsummonerLevel: {self.summoner_level}"

me = Summoner("username")
print(type(me.losses))