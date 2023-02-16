from random import choice


class Game:
    def __init__(self) :
        self.user = self.get_user_item()
        self.computer= self.get_computer_item()
        
    def get_user_item(self):
        user = input("select r, p, s: ")
        while user not in list("rps"):
            user=  input("Please enter a valid input:  ")
        return user
        
    def get_computer_item(self):
            return choice(["p","r","s"])
    
    def get_game_result(self):
         if self.user== "r" and self.computer== "s" or self.user=='p' and self.computer=='r':
              return 'win'
         if self.user== self.computer:
              return 'equal' 
         return 'lose'
         
    def play(self):
        print(f'You chose: {self.user}. The computer chose: {self.computer}. Result: {self.get_game_result()}')
        return self.get_game_result()




            
         



