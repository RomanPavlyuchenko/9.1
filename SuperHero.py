import requests
from pprint import pprint


def who_most_intelligence(hero_list_name, token):
    hero_dict = {}
    for hero in hero_list_name:
        url = 'https://superheroapi.com/api/' + token + '/search/' + hero + '/'
        response = requests.get(url)
        resp = response.json()
        for i in resp['results']:
            if i['name'] == hero:
                hero_dict[hero] = int(i['powerstats']['intelligence'])
    pprint(hero_dict)
    most_intelligence = list(hero_dict.items())
    most_intelligence.sort(key=lambda i: i[1])
    return most_intelligence[-1][0]


print(who_most_intelligence(['Hulk', 'Captain America', 'Thanos'], '2619421814940190'))
