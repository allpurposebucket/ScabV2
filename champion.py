from api import get_champion_data

class Champion:
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.title = ""
        self.lore = ""
        self.partype = ""
        self.get_champion_data()

    def get_champion_data(self):
        data = get_champion_data(self)
        self.name = data["name"]
        self.title = data["title"]
        self.lore = data["lore"]
        self.partype = data["partype"]

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return str(self)