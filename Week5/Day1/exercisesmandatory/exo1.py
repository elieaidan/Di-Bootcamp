# class Cat:
#     def __init__(self, cat_name, cat_age, cate_size):
#         self.name = cat_name
#         self.age = cat_age
#         self.size = cate_size


# thecat1 = Cat('Sacha' , 3, 35)
# thecat2 = Cat('Fred' , 2, 20)
# thecat3 = Cat('Bernard' , 1, 10)

# def oldest_cat ():
#     if thecat1.age > thecat2.age and thecat1.age > thecat3.age:
#         print('Thecat1 is the oldest')
#     elif thecat2.age > thecat3.age and thecat2.age > thecat1.age:
#         print('Thecat2 is the oldest')
#     elif thecat3.age > thecat1.age and thecat3.age > thecat2.age:
#         print('Thecat3 is the oldest')

# oldest_cat()

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

shlomo = Cat(cat_name='Shlomo', cat_age=4)
mizzy = Cat(cat_name='Mizzy', cat_age=3)
batya = Cat(cat_name='Batya', cat_age=5)

def oldest_cat(*cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat

    print(f"Oldest cat: {oldest_cat.name}")

oldest_cat(batya, shlomo, mizzy)







