# A small game where players compare stats, similar to the Top Trumps
# card game.
import random
import requests
print('Welcome to the Top Trumps with Pokemon Game! \n')
"""This extended game generates 5 diff Pokemon ids for two players to choose 
and then compares based on selected stat to find a winner"""


def random_pokemon():
    pokemon_id = [random.randint(1, 151) for i in range(5)]
    # print(pokemon_id)  # To check random list of five ids are generated
    choice = int(input(f'Choose your pokemon from these options ({pokemon_id}): '))
    if choice in pokemon_id:
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
        response = requests.get(url)
        pokemon = response.json()

        return {
            'name': pokemon['name'],
            'id': pokemon['id'],
            'height': pokemon['height'],
            'weight': pokemon['weight']
            }


def run():
    my_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))
    stat_choice = input('Which stat do you want to use? (id, height, weight) ')
    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    players_score = 0
    computers_score = 0
    loss = 0
    if my_stat > opponent_stat:
        print('You Win!')
        players_score += 1
    elif my_stat < opponent_stat:
        print('You Lose!')
        computers_score += 1
    else:
        print('Draw!')
        loss += 1
    # return [players_score, computers_score, loss]
    print(f'You won {players_score} rounds, lost {loss} and computer won {computers_score}')


# print(f'\nLet\'s play again! This is round {count+1} \n')
count = 1

for count in range(3):
    run()
    count += 1
    print(f'\nLet\'s play again! This is round {count +1} \n')






