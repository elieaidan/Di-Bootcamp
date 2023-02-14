from random import *

def game ():
    number = int(input('Chose number between 1 and 100: '))
    x = randint(1, 100)
    if x == number:
        print('its the same number you win !!!!!!!!!')
    else:
        pass    

game()