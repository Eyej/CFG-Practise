# chairs = 15
# nails = 4
# total_nails = chairs*nails
# message = '{} nails'.format(total_nails)
# print('You need to buy {}.'.format(message))
#
# my_name = 'Penelope'
# my_age = 29
# message = 'My name is {} and I am {} years old.'.format(my_name, my_age)
# print(message)
#
# box = 6
# omelette = 4
# total_omelettes = box*omelette
# message = 'You can make {} omelettes with {} boxes of eggs.'.format(total_omelettes, box)
# print(message)


# Week 3 Homework
# Umbrella Reminder
# rain = input('Is it raining? y/n: ')
# if rain == 'y':
#    print('Take an umbrella')
# elif rain == 'n':
#     print('You do not need an umbrella')

# my_money = float(input('How much money do you have? '))
# boat_cost = 20 + 5
# if my_money <= boat_cost:
#     print('You can afford the boat hire')
# else:
#     print('You cannot afford the board hire')

# Book Categories

# def catalog():
#     year = int(input('What year was this book written?: '))
#
#     if year in range(1800, 1810):
#         output = "Early Eighteenth Century"
#     elif year in range(1810, 1820):
#         output = "Eighteenth Century, Tens"
#     elif year in range(1820, 1830):
#         output = "Eighteenth Century, Twenties"
#     elif year in range(1830, 1840):
#         output = "Eighteenth Century, Thirties"
#     elif year in range(1840, 1850):
#         output = "Eighteenth Century, Forties"
#     elif year in range(1850, 1860):
#         output = "Eighteenth Century, Fifties"
#     elif year in range(1860, 1870):
#         output = "Eighteenth Century, Sixties"
#     elif year in range(1870, 1880):
#         output = "Eighteenth Century, Seventies"
#     elif year in range(1880, 1890):
#         output = "Eighteenth Century, Eighties"
#     elif year in range(1890, 1900):
#         output = "Eighteenth Century, Nineties"
#     # Now in the 90s
#     elif year in range(1900, 1910):
#         output = "Early Nineteenth Century"
#     elif year in range(1910, 1920):
#         output = "Nineteenth Century, Tens"
#     elif year in range(1920, 1930):
#         output = "Nineteenth Century, Twenties"
#     elif year in range(1930, 1940):
#         output = "Nineteenth Century, Thirties"
#     elif year in range(1940, 1950):
#         output = "Nineteenth Century, Forties"
#     else:
#         output = "Unsure"
#     print(output)
# catalog()

# Week 4 Homework

# Shop till to display chocolate price
# chocolates = {  #dictionary holding chocolate prices
# 'white': 1.50,
# 'milk': 1.20,
# 'dark': 1.80,
# 'vegan': 2.00,
# }
# chocolate_type = input('What price is this kind of chocolate? ')
# if chocolate_type in chocolates:
#     print(chocolates[chocolate_type])

# Lottery Program
import random

ticket = [23, 4, 35, 7, 10, 25, 1]
random_ticket = [random.randint(1, 35) for value in range(7)]       # How-to generate a list with multiple random numbers
print(ticket)
print(random_ticket)

matching_numbers_count = 0
for number in ticket:
    if number in random_ticket:
        matching_numbers_count = matching_numbers_count +1

if matching_numbers_count == 3:
    print('Congrats! You won $20')
elif matching_numbers_count == 4:
    print('Congrats! You won $40')
elif matching_numbers_count == 5:
    print('Congrats! You won $100')
elif matching_numbers_count == 6:
    print('Congrats! You won $10,000')
elif matching_numbers_count == 7:
    print('Congrats! You won $1,000,000')
else:
    print('You don\'t win any money')