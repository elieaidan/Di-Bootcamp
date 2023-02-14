class Dog:
    def __init__(self, name, age, weight) :
        self.name = name
        self.age = age
        self.weight = weight

    def bark (self):
        answer = f'{self.name} is barking'
        print (answer)

    def run_speed(self):
        speed = self.weight/self.age*10
        return speed

    def fight(self, other_dog):
        winner = None
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            print(f"{self.name}")
        else:
            print(f"{other_dog.name}") 



noa = Dog('noa', 20, 15)
coucou = Dog('coucou', 15, 10)
baba = Dog('coucou', 10, 20)

noa.bark()
noa.run_speed()
noa.fight(coucou)

coucou.bark()
coucou.run_speed()
coucou.fight(noa)

baba.bark()
baba.run_speed()
baba.fight(coucou)



        