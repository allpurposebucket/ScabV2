from api import get_match_data, get_summoner_name_from_id
from summoner import Summoner

class Match:
    def __init__(self, id):
        self.id = id
        self.participants = []

    def load(self):
        from api import get_match_data, get_summoner_name_from_id
        data = get_match_data(self.id)

        for player in data["metadata"]["participants"]:
            name = get_summoner_name_from_id(player)
            self.participants.append(Summoner(name))

    def __str__(self):
        return f"Match ID: {self.id}"

    def __repr__(self):
        return str(self)