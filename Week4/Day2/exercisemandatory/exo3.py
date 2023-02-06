basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove( "Blueberries")

basket.append('Kiwi')

basket.insert(0, 'Apples')

counts = basket.count("Apples")


from collections import Counter

print(Counter(basket))

c = Counter(basket) 
print(c["Apples"])


basket.clear()

print(basket)