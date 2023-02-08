user_in = input("Write word: ")

# Make sure the letters are the keys.


# Make sure the letters are strings.


# Make sure the indexes are stored in a list and those lists are values.

# "dodo" -> {"d": [0, 2], "o": [1, 3] }
# "froggy"
# "grapes"

result = {}

# 4 - {'d': [0, 2], 'o': [1, 3]}
# i - 3, letter - o
for i, letter in enumerate(user_in):

    if letter in result:
        result[letter].append(i)

    else:
        result[letter] = [i]

print(result)


i = 0

for letter in user_in:

    if letter in result:
        result[letter].append(i)

    else:
        result[letter] = [i]

    i += 1