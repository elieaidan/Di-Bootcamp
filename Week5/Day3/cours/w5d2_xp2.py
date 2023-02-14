# 1. Create a class called Dog with the following attributes name, age, weight.
# 2. Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# 3. Create 3 dogs and run them through your class.

class Dog: 

    def __init__(self, name: str, age: int, weight: int):
        
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self) -> str:
        return f'{self.name} is barking'

    def run_speed(self) -> int:
        return self.weight/self.age*10

    def fight(self, other_dog) -> str:

        winner = None

        if self.run_speed() * self.weight > other_dog.run_speed() * self.weight:
            winner = self
        else:
            winner = other_dog

        return f'{winner.name} has won!'


# add a small piece of code which tells python what to run when we run the file directly

if __name__ == '__main__':
    
    rex = Dog('Rex', 4, 20)
    bob = Dog('Bob', 6, 15)
    laki = Dog('Laki', 5, 17)

    print("THIS IS THE DOG CLASS FILE")