# cells

    ################
    # 1 #  2  #  3 #
    ################
    # 4 #  5  #  6 #
    ################
    # 7 #  8  #  9 #
    ################

# rows and columns

#      1    2    3
    ################
#1  #    #   #     #
    ################
#2  #    #   #     #
    ################
#3  #    #   #     #
    ################

# 9 choices - 
 
# dict I - {1(cell): , 2: , 3: ,4: ...}

# dict II - {1(row): {1(column): ,2(column):, 3(column):},
#            2(row): {1: , 2: , 3:},
#            3(row): {1:, 2:, 3:}}

# list - [1(cell), 2, 3, 4, 5, 6, 7, 8, 9]


choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def display_board(choices):
    board_gui = f"""
    #############
    # {choices[0]} # {choices[1]} # {choices[2]} #
    #############
    # {choices[3]} # {choices[4]} # {choices[5]} #
    #############
    # {choices[6]} # {choices[7]} # {choices[8]} #
    #############
    """
    print(board_gui)

def switch_players(player: str):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def player_input(player):

    player_choice = None

    while player_choice not in choices:
        player_choice = int(input(f"Player {player} Your choice: "))

    print("Player chose:", player_choice)

    choices[player_choice] = current_player

    display_board(choices)

current_player = 'X'



def player_win():

    choices1a = ['O', 'O', 'O', 2, 3, 5, 6, 7, 8]
    choices2a = [0, 1, 2, 'O', 'O', 'O', 6, 7, 8]
    choices3a = [0, 1, 2, 3, 4, 5, 'O', 'O', 'O']
    choices1 =  ['X', 'X', 'X', 2, 3, 5, 6, 7, 8]
    choices2 =  [0, 1, 2, 'X', 'X', 'X', 6, 7, 8]
    choices3 =  [0, 1, 2, 3, 4, 5, 'X', 'X', 'X']
    choices4 =  ['X', 1, 2, 3, 'X', 5, 6, 7, 'X']
    choices4a = ['O', 1, 2, 3, 'O', 5, 6, 7, 'O']

    if choices == choices1 or choices == choices2 or choices == choices3 or choices == choices4 or choices == choices1a or choices == choices2a or choices == choices3a or choices == choices4a :
        print('You win !!') 
        return True
    else:
        return False

       


    


while not player_win():

    player_input(current_player)
    winner = player_win(current_player)

    if winner : 
    current_player = switch_players(current_player)

    player_input(current_player)


    



