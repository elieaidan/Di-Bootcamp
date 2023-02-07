# Create a variable called birthdays. Its value should be a dictionary.
# Initialize this variable with birthdays of 5 people of your choice.
#  For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. 
#  Tip : Use the format “YYYY/MM/DD”.

birthday = {
   "elie": "22/07/2002",
   "noa": "24/08/2002",
   "yaron": "6/12/2004",
   "yossi": "12/07/1991",
   "kaki": "10/01/2000",
   }

print("You can look up the birthdays of the people in the list")

name = input('Chose a name:').lower()

print(birthday.get(name, f'there is no {name} in the list')) 





