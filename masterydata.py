from api import get_summoner_mastery_data
from champion import Champion

class MasteryData:
    def __init__(self, summoner, count=5):
        self.summoner = summoner
        self.data = []
        self.count = count

    def load(self):
        self.data = get_summoner_mastery_data(self.summoner, self.count)

    @property
    def top_champions(self):
        if not self.data:
            self.load()
        sorted_data = sorted(self.data, key=lambda champ: champ['championPoints'], reverse=True)

        champs = [Champion(champ['championId']) for champ in sorted_data]

        return champs

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)
