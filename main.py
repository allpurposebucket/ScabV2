from summoner import Summoner
from match import Match
def main():
    # summoner = Summoner("allpurposebucket")
    # print(summoner.account_data.puuid)
    # print(dir(summoner.account_data))
    match1 = Match("NA1_4785135226")
    print(match1.participants)


if __name__ == "__main__":
    main()