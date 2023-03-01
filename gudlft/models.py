import json

DATA_DIRECTORY = 'gudlft/data/'


def load_clubs():
    with open(DATA_DIRECTORY + 'clubs.json') as c:
        clubs_list = json.load(c)['clubs']
        return clubs_list


def load_competitions():
    with open(DATA_DIRECTORY + 'competitions.json') as comps:
        competitions_list = json.load(comps)['competitions']
        return competitions_list
