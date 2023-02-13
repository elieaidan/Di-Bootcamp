import time

class Vehicle:

    def __init__(self, number_wheels: int) -> None:
        self.wheels = number_wheels

    def drive(self):
        print("DRIVING")

class Car(Vehicle):
    # additional attribute - trunk. We need to overwrite the __init__function
    def __init__(self, number_wheels: int) -> None:
        # super() uses the parents __init__
        super().__init__(number_wheels)
        self.trunk: list = []

    def race(self):
        print("RACING AGAINST OTHER CAR")

    def drive(self):
        super().drive()
        
class Bus(Vehicle):
    
    # additional attribute - passengers
    def __init__(self, number_wheels: int) -> None:
        super().__init__(number_wheels)
        self.passengers = []

    # pickup (passenger)
    def pickup(self, passenger: str):
        if passenger not in self.passengers:
            self.passengers.append(passenger)
        else:
            pass

class Truck(Vehicle):
    pass

class Bike(Vehicle):
    
    def ring_bell(self):
        for _ in range(10):
            print("RINGS BELL")
            time.sleep(0.2)
        print("FINISHED RINGING")

toyota = Car(number_wheels=4)

# toyota.race()
my_bike = Bike(2)

my_bike.ring_bell()

# print(toyota.trunk)