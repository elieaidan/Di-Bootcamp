import json

# Retrieve the data into the python file, inside a variable called family
file_location = 'file.json'

jane_info = {}

with open(file_location, 'r') as file:
    jane_info = json.load(file)

# Print nicely the details about Jane's children
for child in jane_info['children']:
    print(child['firstName'])
    print(child['age'])

# Inside the family variable, add to each children, a key 'favorite_color' with a value
for child in jane_info['children']:
    child['favorite_color'] = 'blue'

print(jane_info['children'])

with open(file_location, 'w') as file:
    json.dump(jane_info, file, indent=4)

    