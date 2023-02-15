from translate import Translator

translate = Translator(from_lang="french", to_lang="english")

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt", "Je t'aime", "coucou"] 

dict ={}

for word in french_words:
    dict [translate.translate(word)] = word

print(dict)
