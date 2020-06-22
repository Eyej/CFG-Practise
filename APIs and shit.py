# Week 6- Learning about Files, APIs and PIP

# with open('people.txt', 'w+') as text_file:         # Syntax for writing to a file
#     people = 'Joanne \nSusan \nAmina'
#     text_file.write(people)
# with open('people.txt', 'r') as text_file:          # syntax to read from a file
#     contents = text_file.read()
# print(contents)

# first exercise
# added_data = input('Enter a new to-do item ')
# poem = 'I like Python and I am not very good at poems'
# with open('todo.txt', 'r') as todo_file:          # This program reads a list, adds items to it and saves
#     todo = todo_file.read()
# todo = todo + ' \n' + added_data + '\n' + poem              # Code which writes new item plus poem into the list
# with open('todo.txt', 'w+') as todo_file:
#     todo_file.write(todo)


# import csv
# # Learning with csv
# field_names = ['name', 'age']
# data = [
#     {'name': 'Jill', 'age': 32},
#     {'name': 'Sara', 'age': 28},
# ]
# with open('team.csv', 'w+') as csv_file:        # How to write using comma separated values
#     spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
#     spreadsheet.writeheader()
#     spreadsheet.writerows(data)
#
# with open('team.csv', 'r') as csv_file:         # how to read a csv
#     spreadsheet = csv.DictReader(csv_file)
#     for row in spreadsheet:
#         print(dict(row))

# Exercise 5.2, find the shortest tree using data from the trees.csv file

# import csv
# # field_items = ['id', 'height', 'species', 'age']
# with open('trees.csv', 'r') as csv_file:         # Syntax to read the csv file
#     spreadsheet = csv.DictReader(csv_file)
#     heights = []
#
#     for row in spreadsheet:
#         tree_height = row['height']
#         heights.append(tree_height)
#
# shortest_height = min(heights)
# print(shortest_height)

# Playing with APIs
# import requests
# # from pprint import pprint         # from earlier code used to print Pokemon stats
# pokemon_number = input("What is the Pokemon's ID? ")
# url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
# response = requests.get(url)
# pokemon = response.json()
# # pprint(pokemon)           # From earlier code as well
# print(pokemon['name'])
# print(pokemon['height'])
# print(pokemon['weight'])
# # Exercise extension to grab all moves name
# move_names = (pokemon['moves'])
# for j in move_names:
#     print(j['moves']['names'])

# I want a program that can retrieve multiple Pokemon and save their names and moves to a file.
# Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each
# Pokemon. Save their names and moves into a file called 'pokemon.txt'

# import requests
# # pokemon = {}
# ids = [304, 600, 12, 7, 18, 505]
# for i in ids:
#     url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(i)
#     response = requests.get(url)
#     pokemon = response.json()
#
#     names = pokemon['name']
#     action = pokemon['moves']
#     action_list = ' '
#     # action = str(action)
#     # data = names + '\nmoves: ' + action
#     # print(data)          # Code for testing data displays
#
#     # To obtain individual moves within the specific pokemon:
#
#     for j in action:
#         pokemon_movement = j['move']['name']
#         action_list = action_list + pokemon_movement
#     data = '\n' + names + '\n' + action_list
#     print(data)
    # with open('pokemon.txt', 'a') as pokemon_file:
    #     pokemon_file.write(data)
#     with open('pokemon.txt', 'r') as pokemon_file:
#         output = pokemon_file.read()
# print(output)