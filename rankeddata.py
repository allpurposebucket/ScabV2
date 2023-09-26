from api import get_summoner_ranked_data

class RankedData:
    def __init__(self, summoner):
        self.summoner = summoner
        self.data = {}

    def load(self):
        self.data = get_summoner_ranked_data(self.summoner)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)