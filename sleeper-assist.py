import json
import requests
import sys

def get_userid(input):
    r = requests.get("https://api.sleeper.app/v1/user/" + input)
    user_obj = r.json()#orjson.loads(r.json())
    return user_obj["user_id"]

def get_leagueid(input):
    user_id = get_userid(input)
    r = requests.get("https://api.sleeper.app/v1/user/" + user_id + "/leagues/nfl/2024")
    league_obj = r.json()
    return league_obj#[1]["league_id"]

def get_rosters(input):
    get_leagueid(input)
    return





if __name__ == "__main__":
    args = sys.argv[1:]
    command = args[0]
    input = args[1]
    if command == "user":
        print(get_userid(input))
    if command == "league":
        print(get_leagueid(input))
