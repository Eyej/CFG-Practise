# A small game where players compare stats, similar to the Top Trumps
# card game.
import random
import requests
def random_pokemon():
    pokemon_id=random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        }

def run():


url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
response = requests.get(url)
pokemon = response.json()
library = {'names':pokemon['name'], 'heights':pokemon['height'], 'weights':pokemon['weight']
            }
