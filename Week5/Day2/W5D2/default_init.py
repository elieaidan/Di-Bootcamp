class Player:
    def __init__(self, name: str, player_class: str, strength: int, health: int):

        self.name = name
        self.player_class = player_class
        self.strength = strength
        self.health = health

    def fight(self):
        print(f'{self.name} is fighting !')
    
    def add_health(self, health: int):
        self.health += health
        print(f'{self.name} increased health to {self.health}')
