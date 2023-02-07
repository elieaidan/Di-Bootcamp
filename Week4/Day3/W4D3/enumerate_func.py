alphabet = 'abcdefghijklmnopqrstuvwxyz'

enumerated_alpha: dict = dict(enumerate(alphabet))

print(enumerated_alpha[2])

tasks = ['cleanup the apartments', 'cooking', 'go outside', 'jogging']

to_do = dict(enumerate(tasks, 1))

print(to_do)


# loop through index and value inside list
for i, value in enumerate(tasks):
    print(f"INDEX {i} : {value}")