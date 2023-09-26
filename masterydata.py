from api import get_summoner_mastery_data

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
            self.load_default_data()

        sorted_data = sorted(self.data, key=lambda champ: champ['masteryPoints'], reverse=True)

        return sorted_data[:5]

    def load_default_data(self):
        self.load()

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)
