# ZIP CONNECTS VALUES BY THEIR INDEX

ages = [31, 28, 15, 12, 1]
names = ['Brad', 'Lea', 'Moti', 'Yakov', 'Yaron']
cities = ['TLV', 'PARIS', 'MARSEILLE', 'Lyon', 'STRASBOURG']

names_ages: list = list(zip(names, ages, cities))

print(names_ages)