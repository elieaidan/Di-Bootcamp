from game import Game

def get_user_menu_choice():
    choice = input('tape 1 Play a new game, tape 2 to Show scores or tape 3 to quit:  ')
    while choice not in ['1','2','3']:
        choice= input('tape 1 Play a new game, tape 2 to Show scores or tape 3 to quit:  ')
    return choice

def print_results(results):
    print(f"Result of the Game: You won {results['win']} time(s), You lost {results['lose']} times, Equality for {results['equal']} times")   


def main():
    scoreboard = {
        'win': 0,
        'lose': 0,
        'equal': 0
    }
    choice = get_user_menu_choice()
    while choice != "3":
        if choice == "1":
            new_game = Game()
            scoreboard[new_game.play()]+=1
        else:
            print_results(scoreboard)
        choice = get_user_menu_choice()
    print("thx for playing")

main()

        


