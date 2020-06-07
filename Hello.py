# Python begins

# print('Hello World!')
# #print('spaghetti')
# food='spaghetti'
# print(food)
# oranges=12
# cost_per_orange=0.5
# total_cost=oranges*cost_per_orange
# print(str(oranges) + ' oranges')
# print('costs '+ str(total_cost))
# output ="{} oranges costs ${}".format(oranges, total_cost)
# print(output)
# name = input('What is your name? ')
# print('Hello {}, Your name is {}'.format(name,name))
# fav_color = input('Tell me your fav color')
# dress = input('What is your dress size')
# print('Would you like a {} gown in size {}?'.format(fav_color,dress))


# Code Lagos Exercises

# Even Odd Number Test
# value = int(input('Enter any number: '))        # We want to check if the number is odd or even
# if value % 2 == 0:
#     print('Number is even')
# elif value % 2 == 1:
#     print('Number is odd')

# Area Calculator
# print('Welcome to the area calculator designed by IJ, pick a choice from the menu:')
#
# print('Triangle\n Square\n Circle')
# shape = input('Select a shape: ')
#
#
# def triangle():
#     breadth = int(input('what is its breadth:'))
#     height = int(input('what is its height: '))
#     area = 0.5 * breadth * height
#     return area
#
#
# def square():
#     length = int(input('Enter a length: '))
#     area_square = length**2
#     return area_square
#
#
# def circle():
#     radius = int(input('Enter a radius: '))
#     circle_area = 3.142 * (radius**2)
#     return circle_area
#
# if shape == 'triangle':
#     print('The area = {}cm'.format(triangle()))
# elif shape == 'square':
#     print('Area = {}cm'.format(square()))
# elif shape == 'circle':
#     print('Area = {}cm'.format(circle()))
# else:
#     print('Sorry, I cannot calculate this area.')

# # Program to get the factorial
# number = int(input('Enter any number '))
# if number < 0:
#     print('Error, Input a positive number')
# elif number == 0:
#     print('The factorial equals 1')
# else:
#     result = 1
#     for i in range(1, (number + 1)):       # Loop to iterate through the range and multiple descending values together
#         result = result * i
#         print(result)

# Finding all prime numbers in a range
value = int(input('Enter any number '))
if value <= 2:
    print('Error, try a new value')
else:
    count = []
    for num in range(2, (value + 1)):
        # if num % 2 > 2:
        for i in range(2, num):
            if num%i == 0:
                count.append(i)
                print('List of prime numbers: ', count)     # Something is wrong with this but i'll ignore for now
