import random


def number ():
    numberinput = int(input('Chose a number : '))
    numbersrandom = random.choice(range(10, 101))
    
    if numberinput == numbersrandom:
        print('YOU WIN !!!!!')
    else:
        print(f'you lost because {numberinput} and {numbersrandom} are not the same number')    


a = number()

print(a)

