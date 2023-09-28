from api import get_match_data, get_summoner_name_from_id
from summoner import Summoner

class Match:
    def __init__(self, id):
        self.id = id
        self.participants = None

    @property
    def participants(self):
        if self.participants is None:
            self.load()
        return self.participants

    def load(self):
        data = get_match_data(self.id)
        self.participants = []

        for player in data["metadata"]["participants"]:
            name = get_summoner_name_from_id(player)
            self.participants.append(Summoner(name))

    def __str__(self):
        return f"Match ID: {self.id}"

    def __repr__(self):
        return str(self)
