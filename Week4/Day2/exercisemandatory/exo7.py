favorite_fruits = input('What is your favorite fruits(separate the fruits with a single space) : ').lower()
favorite_fruits_list = favorite_fruits.split(" ")
print(favorite_fruits_list)
 
fruit = input('input a name of any fruit:').lower()

if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
     print("You chose a new fruit. I hope you enjoy")

