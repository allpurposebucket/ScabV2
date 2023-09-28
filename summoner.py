from api import get_matches_by_puuid
from rankeddata import RankedData
from accountdata import AccountData
from masterydata import MasteryData

class Summoner:
    def __init__(self, name):
        self.name = name
        self.matches = []

    def get_matches(self, count):
        from match import Match

        match_ids = get_matches_by_puuid(self.account_data.puuid, count)
        self.matches = [Match(match_id) for match_id in match_ids]

    def get_all_data(self, mastery_count, match_count):
        self.account_data.load()
        self.ranked_data.load()
        self.mastery_data.load(mastery_count)
        self.get_matches(match_count)

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        
        if name == "account_data":
            self.account_data = AccountData(self)
            self.account_data.load()
            return self.account_data

        elif name == "ranked_data":
            self.ranked_data = RankedData(self)
            self.ranked_data.load()
            return self.ranked_data

        elif name == "mastery_data":
            self.mastery_data = MasteryData(self)
            self.mastery_data.load()
            return self.mastery_data

        else:
            raise AttributeError(f"'Summoner' object has no attribute '{name}'")

    def __str__(self):
        return f"Name: {self.name}\n"

    def __repr__(self):
        return str(self)
