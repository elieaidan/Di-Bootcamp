# Créez le code nécessaire pour recevoir le résultat fourni ci-dessus. Voici quelques questions pour vous aider avec votre code :

# Créez une classe appelée Farm. Comment doit-il être mis en œuvre ?
# La classe Farm a-t-elle besoin d'une méthode __init__ ? Si oui, quels paramètres faut-il prendre ?
# De combien de méthodes la classe Farm a-t-elle besoin ?
# Avez-vous remarqué quelque chose d'intéressant dans la façon dont nous appelons la méthode add_animal ? Quels paramètres cette fonction doit-elle avoir ? Combien…?
# Testez votre code et assurez-vous d'obtenir les mêmes résultats que l'exemple ci-dessus.
# Bonus : alignez joliment le texte en colonnes comme on le voit dans l'exemple ci-dessus. Utilisez le formatage de chaîne.

class Farm:
    def __init__(self, farm_name) -> None:
        self.name = farm_name
        self.list = {}

    def add_animal(self, new_animal, amount):
        if new_animal not in self.list:
            self.list[new_animal] = amount     
        else:
            self.list[new_animal] += amount  
        
        print(self.list) 

    def get_animal_types (self):
        l = list(self.list)
        return l

    def get_short_info(self):
            print(f'Elie farm have {", ".join(self.get_animal_types())}  in here farm with her friend shone atsadik')



    # def get_info(self):

eliefarm = Farm('ElieFarm')
eliefarm.add_animal('snake', 25)
eliefarm.add_animal('tutle', 25)
eliefarm.get_animal_types()
eliefarm.get_short_info()

