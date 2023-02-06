toppings = []

while True:
    pizza = input("enter a series of pizza topping:  ").lower()
    if pizza != "quit":
        toppings.append(pizza) 
    else:
        break

