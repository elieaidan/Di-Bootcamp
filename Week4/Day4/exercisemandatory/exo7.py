import random


def get_random_temp():
    celsiusrandom = random.choice(range(-10, 40))
    return celsiusrandom


a = get_random_temp()



def main():
    number = get_random_temp()
    print(f'The temperature right now is {get_random_temp()} degrees Celsius')
    if number < 0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif number < 16 and number > 0:
        print('Quite chilly! Don’t forget your coat')
    elif number < 32 and number > 16:
        print('Psartek temps de folie')
    elif number < 32 and number > 24: 
         print('chhana')
    elif number < 40 and number > 32: 
         print('Chaud, tres chaud , il faut boirrrre')
        



main()

