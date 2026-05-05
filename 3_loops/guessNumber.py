# This is a number guessing game
import random

# generate a random number to guess:
randomNumber = random.randint(1,20)

print('Please guess a number between 1 and 20.')

for guessesTaken in range(1,7):
    # guessesTaken --> 1,2,3,4,5,6
    
    print('Take a guess:')
    guess = int(input('>'))
    
    if(guess < randomNumber):
        print('Too low.')
    elif(guess > randomNumber):
        print('Too high')
    else:
        # user got the number
        break;
    
if guess == randomNumber:
    print('You got it!')
else:
    print('You did not get it. Random Number:' + str(randomNumber))