class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if self.animals.count(new_animal) == 0:
            self.animals.append(new_animal)
             
    def get_animals (self):
        for animal in self.animals:
            print(animal)

    def sell_animal (self, animal_sold):
        if self.animals.count(animal_sold) != 0:
            print(f'GoodBye {animal_sold}')
            self.animals.remove(animal_sold)
        else:
            print(f'{animal_sold} isnt in the zoo') 
    

    def sort_animals(self):
        list = sorted(self.animals)
        print(list)

        
ramat_gan_safari = Zoo('Girafe')

ramat_gan_safari.add_animal('serpent')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('pomme')
ramat_gan_safari.sort_animals()

