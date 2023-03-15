import json


def load_clubs(clubs):
    with open(clubs) as c:
        clubs_list = json.load(c)['clubs']
        return clubs_list


def load_competitions(competitions):
    with open(competitions) as comps:
        competitions_list = json.load(comps)['competitions']
        return competitions_list
