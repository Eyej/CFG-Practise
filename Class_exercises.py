# first lessons using Turtle
# import turtle
#
# # side_length = 250
# # angle = 240
# # turtle.color('gold', 'blue') #first is line color and second is fill color
# # turtle.begin_fill()
# # turtle.speed('slowest')
# #
# # turtle.forward(side_length)
# # turtle.right(angle)
# # turtle.forward(side_length)
# # turtle.right(angle)
# # turtle.forward(side_length)
# # turtle.right(angle)
# #
# # turtle.end_fill()
# # turtle.done()
# # length = input('How long do you want it?')
# # color = input('Which color should t have?')
# def shape(length, colour):
#     angle = 240
#     turtle.color(colour, colour)
#     # length = 150
#     # turtle.color('gold', 'grey')
#     turtle.begin_fill()
#     turtle.speed('slowest')
#     for sides in range(3):
#         turtle.forward(length)
#         turtle.right(angle)
#     turtle.end_fill()
#
# shape(12, 'pink')
# turtle.forward(100)
# shape(16, 'yellow')
# turtle.forward(50)
# shape(20, 'blue')
# turtle.done()


# # learning conditionals and comparisons
# temp = float(input('what is the oven temperature? '))
# too_hot = temp >= 200.0
# print('Temperature is super hot {} '.format(too_hot))

# # Burger Exercise
# burger_price = input('How much does the burger cost? ')
# vegetarian_meals = input('Any vegetarian meals available? y/n ')
# affordable = float(burger_price) <= 10.00
# veggie = vegetarian_meals == 'y'
# if affordable and veggie:
#     print('This restaurant is a great choice!')
# if not affordable or not veggie:
#     print

# #Pay the bill Program
# meal_price = float(input('How much is your total? '))
# discountable = meal_price >= 20.00
# has_discount = input('Do you have a discount? y/n ')
# use_discount = has_discount == 'y'
#
# total = meal_price * 0.9
#
# bill = discountable and use_discount
# if bill:
#     print('Discount Applied! You should pay ${} '.format(total))
# else:
#     print('No discount applicable, you are to pay ${} '.format(meal_price))

# #Check oven temp for pizza
# temp = float(input('Tell me the oven temperature' ))
# if temp > 200:
#     print('The oven is too hot')
# elif temp < 150:
#     print('The oven is too cold')
# elif temp == 180:
#     print('The oven is at the perfect temperature')
# else:
#     print('The temperature is close enough')


# #Playing with Random Numbers
# import random
# def coin_flip():
#     coin = random.randint(1, 2)
#     if coin == 1:
#         assign = 'Heads'
#     else:
#         assign = 'Tails'
#     return assign
# player = input('Heads or Tails: ')
# result = coin_flip()
# print(result)
# # if player == result:
# #     print('You got it! {} '.format(result))
# # else:
# #     print('Try again sucker! It was {}'.format(result))

# # Not Quite Roulette
# import random
#
# def roll():
#     dice = random.randint(1, 2)
#     if dice == 1:
#         colour = 'red'
#     else:
#         colour = 'black'
#     return colour
#
#
# amount = float(input('How much will you bet? $'))
# my_color = input('What color? red or black ')
# my_number = int(input('Enter a number from 1-100: '))
# random_number = random.randint(1, 100)
# computer = roll()
#
# print('Computer Result = {} and number {}' .format(computer, random_number))
#
# if my_color == computer and my_number != random_number:
#     print('You can keep your ${} '.format(amount))
# elif my_number == random_number and my_color != computer:
#     print("You've won double! Your total = ${} ".format(amount*2))
# elif (my_number == random_number) and (my_color == computer):
#     print('You have won 100 times! Your amount = ${} '.format(amount * 100))
# else:
#     print('You lose. Your amount = 0')


# Week 4
# clothes = [
#     "shorts",
#     "shoes",
#     "T-shirt"
# ]
# if clothes[0] == "shorts":
#     clothes[0] = "Winter jackets"
# print(clothes)
#
# scores = [3,  5, 20, 35, 100, 200, 79, 43, 21, 7]
# print(len(scores))
# print(max(scores))
# print(min(scores))
# print(sorted(scores))
# print(list(reversed(sorted(scores))))

# shop_list = ["bread", "rice", "milk"]
# if 'bread' in shop_list:
#     shop_list.append("butter")
# print(shop_list)
#
# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# total_cost = 0
# for gross in costs:
#     total_cost = total_cost + gross
#     # Another solution is to use   total_cost += gross
#     # Or                           print(sum(costs))
#     print(total_cost)
#
# place = {
#         'name': 'The Anchor',
#         'post_code': 'E14 6HY',
#         'street_number': '54',
#         'location': {
#             'longitude': 127,
#             'latitude': 63,
#         }
#     }
# print(place['name'])
# print(place['post_code'])
# # Ways to access values within a list's dictionary
# # print(place['location']['longitude'])
# # print(place['location']['latitude'])
#
# map_location = place['location']
# print(map_location['longitude'])
# print(map_location['latitude'])
#
#
# fruits = [
#     {'name': 'apple', 'colour': 'red', 'price': 0.12},
#     {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
#     {'name': 'pear', 'colour': 'green', 'price': 0.19},
# ]
# for item in fruits:
#     print(item['name'] + ' ' + item['colour'])
#     # print(item['colour'])
#     print(item['price'])

import random
first_names = ['Taylor', 'Shane', 'Abed', 'Wood']
last_names = ['Breen', 'LeQuisha', 'Bush', 'Monica', 'Elue']

chosen_first_names = random.choice(first_names)
chosen_last_names = random.choice(last_names)
print(chosen_first_names + ' ' + chosen_last_names)

# Extension
nouns = ['The girl', 'that boy', 'Cats', 'Greece', 'books', 'shop', 'IJ']
verbs = ['eats', 'shopping', 'cycles', 'showers', 'steals', 'enjoys gossip', 'sings']
sentences = random.choice(nouns) + ' ' + random.choice(verbs)
print(sentences)