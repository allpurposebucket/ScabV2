from api import get_summoner_account_data

class AccountData:
    def __init__(self, summoner):
        self.summoner = summoner
        self.data = None

    def load(self):
        self.data = get_summoner_account_data(self.summoner.name)

    def __getattr__(self, name):
        if self.data is None:
            self.load()
        if name in self.data:
            return self.data[name]
        else:
            raise AttributeError(f"'AccountData' object has no attribute '{name}'")

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)
