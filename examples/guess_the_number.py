# This is a guess the number game.
from random import randint
from builtins import input  # needed for python 2


guesses_taken = 0
guess = -1

print('Hello! What is your name?')
name = input()

number = randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

while guesses_taken < 6:
    print('Take a guess.')  # There are four spaces in front of print.
    guess = int(input())

    guesses_taken += 1  # guess_taken = guess_taken + 1

    if guess == number:
        break
    
    if guess < number:
        print('Your guess is too low.')  # There are eight spaces in front of print.

    else:
        print('Your guess is too high.')


if guess == number:
    print('Good job, ' + name + '! You guessed my number in ' + str(guesses_taken) + ' guesses!')

if guess != number:
    print('Nope. The number I was thinking of was ' + str(number))
