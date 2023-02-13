from exo2 import Dog
import random

class PetDog (Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    
    def train (self):

        self.trained = True
        return self.bark
    
    def play (self, *args):
        print(f'{self.name} all play togethe ')


    def do_a_trick (self, ):
        if self.trained == True:
            X = random.randint(0,3)
            if X== 0:
                print(f'{self.name} does a barrel roll')
            elif X==1:
                print(f'{self.name} stands on his back legs')  
            elif X==2:
                print(f'{self.name} shakes your hand')
            elif X==3:
                print(f'{self.name} plays dead')

                  
        



         
            








