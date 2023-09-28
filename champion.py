from api import get_champion_data

class Champion:
    def __init__(self, champ_id):
        self.id = champ_id

    def load(self):
        data = get_champion_data(self.id)
        self.name = data["name"]
        self.title = data["title"]
        self.lore = data["lore"]
        self.partype = data["partype"]

    def __getattr__(self, name):
        if name not in self.__dict__:
            self.load()
        if name in self.__dict__:
            return self.__dict__[name]
        else:
            raise AttributeError(f"'Champion' object has no attribute '{name}'")

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)