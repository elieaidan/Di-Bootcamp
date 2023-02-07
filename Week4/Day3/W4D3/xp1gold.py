# Create a variable called birthdays. Its value should be a dictionary.

# Initialize this variable with birthdays of 5 people of your choice.
#  For each entry/key in the dictionary, the key should be the person’s name, and the value should be their birthday.
#  Tip : Use the format “YYYY/MM/DD”.

birthdays = { 'Yossi': '1991/11/06',
                'Eli': '2002/07/22',
                'Ran': '1987/04/13'}

# Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“

print("You can look up the birthdays of the people in the list!")

# Ask the user to give you a person’s name and store the answer in a variable.
name = input("Person name: ")
# Get the birthday of the name provided by the user.
# name = 'Yossi'

birthday = birthdays.get(name, f'THERE is no {name} in the data')

# Print out the birthday with a nicely-formatted message.
print(birthday)
