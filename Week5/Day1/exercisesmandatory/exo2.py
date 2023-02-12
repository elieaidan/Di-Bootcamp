class Dog :
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def  bark(self):
        print(f'{self.name} goes woof!') 

    def jump(self):
        x = self.height*2
        print(f'{self.name} jumps {x} cm high ')



davids_dog = Dog('Rex', dog_height= 50)

print(davids_dog.name)
print(davids_dog.height)

davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', dog_height= 20)

print(sarahs_dog.name)
print(sarahs_dog.height)

sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height > davids_dog.height:
    print(f'Sarah has a bigger dog')
else:
    print(f'David has a bigger dog')
    




     
     