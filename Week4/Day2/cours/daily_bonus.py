import random


user_in: str = input("Your input: ")

# 4

# Strings are Not Mutable - cannot be changed

# 1) Change the type of the string into a list

# LIST - Mutable, sequential collection of items
user_in: list = list(user_in)
print(user_in)
# 2) Use the list to shuffle all of the characters
random.shuffle(user_in)
print(user_in)
# 3) To bring the shuffled type back into a string
user_in: str = ''.join(user_in)
print(user_in)