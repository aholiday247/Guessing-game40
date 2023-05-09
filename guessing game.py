# this is a guess the number game

import random

print('hello, what is your name')
name=input()

print('well,' + name +  ', I am thinking of a number between 1 and 20')
secretnumber=random.randint(1, 20)

for guessestaken in range(1,7):
    print('take a guess')
    guess= int(input())

    if guess < secretnumber:
        print('your guess is to low.')
    elif guess >secretnumber:
        print('your guess is too high.')
    else:
        break  # condition is for the correct guess

if guess == secretnumber:
    print('Good job, '  + name + '! you guessed the correct number!' + str(guess))
else:
    print( 'Nope. The number I was thinking of was ' + str(secretnumber))
