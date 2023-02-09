word = input('Write word:  ')


lot = {}

for i, letter in enumerate(word):

    if letter in lot:
        lot[letter].append(i)
    else:
        lot[letter] = [i]

print(lot)  