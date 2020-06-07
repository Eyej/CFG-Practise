#Rock, Paper, Scissors
import random
def random_guess():
    guess = random.randint(1, 3)
    if guess == 1:
        choice = 'rock'
    elif guess == 2:
        choice = 'paper'
    else:
        choice = 'scissors'
    return choice


my_choice = input('Choose rock, scissors or paper: ')
opponent_choice = random_guess()
print('Your opponent chose {}'.format(opponent_choice))
if my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')
elif my_choice == opponent_choice:
    print('You draw!')
elif my_choice == 'paper' and opponent_choice == 'rock':
    print('You win!')
elif my_choice == 'scissors' and opponent_choice == 'paper':
    print('You win!')
else:
    print('You lose!')
