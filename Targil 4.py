#create a function that generates a random number between 1-100 (=lucky number).
# input numbers from the user until the use will guess the lucky number.
# if the user guesses lower than the lucky number- print: “too low”,
# if the user guesses higher than the lucky number- print “too high”.
# if the user guesses correctly- print “bingo”.
# print how many guesses were made until the “bingo”

import random

def randomNum(usernum):
    luckynum=random.randint(1,100)
    print(luckynum)
    guess=1
    while usernum!=luckynum:
        if usernum>luckynum:
            print(f'{usernum} is TOO HIGH')
            guess+=1
            usernum=int(input('plz enter your  NEW number'))
        else:
            print(f'{usernum} is TOO LOW')
            guess+=1
            usernum=int(input('plz enter your  NEW number'))

    print(f'BINGOOOOOOOO.....the number that you entered {usernum} is the Lucky Number :), you do it in {guess} guess')

usernum=int(input('plz enter your number'))
randomNum(usernum)
