# args - arguments 

def add_two(a: int, b: int) -> int:
    result = a - b
    return result

    #   a  b
add_two(1, 2)
        # being more specific -specifying the parameters names (a, b)
res0 = add_two(a = 1, b = 2)

print(res0)

res = add_two(b = 2, a = 1)

print(res)


# kwargs = key: value (dict) argument
def add_two(a: int, b: int, **numbers: dict) -> int:
    result = a - b
    for number in numbers.values():
        result -= number
    return result

res_kwargs = add_two(a = 1, b = 2, c = 3, d = 4, e = 5)
print(res_kwargs)


# args (list) = arguments (value)
def add_two(a: int, b: int, *numbers: tuple) -> int:
    result = a - b
    for number in numbers:
        result -= number
    return result

res_args = add_two(1, 2, 3, 4, 5)
print(res_args)


# some_func() - some random function

# Just arguments/args - some_func(1,2,3)

# Just key:value arguments/kwargs - some_func(a = 1, b = 2, c = 3)

# Both args and kwargs - some_func(args, kwargs)




# (..., *args)
# (1,2,3,4) -> tuple(1,2,3,4)

def some_func(a, b, *args: tuple):
    ...

some_func(1, 2, 3, 4, 5)


# (..., **kwargs)
# (..., a = 2, b = 3) -> dict('a': 2, 'b': 3)

def some_func(a, b, **kwargs: dict):
    ...


def personal_info(first_name:str, last_name:str, **additional_info: dict) -> None:
    print("First name:", first_name)
    print("Last name:", last_name)
    for key, value in additional_info.items():
        print(f'{key}: {value}')

personal_info("Yossi", "Eik", residence = "TLV", country = "Israel", phone_number = "05243434243")


# shopping list, **kwargs = 'item': amount_item ('fruit': $5)

def shopping_list(**shopping: dict):
    for item, price in shopping.items():
        print(f'{item}: {price}')

shopping_list(fruit = '$5', vegetable = '$10')



# *args - function('a', 'b', 'b', 'a') -> 'abba'

def connect_chars(*characters: tuple) -> str:
    word = "".join(characters)
    return word


word = connect_chars('a', 'b', 'b', 'a')
print(word)
    


# *args and **kwargs

def favorite_food(*food_names: tuple, **food_names_prices: dict):
    print("MY FAVORITE FOOD IS: ")
    for name in food_names:
        print(name)
    for name, price in food_names_prices.items():
        print(f'{name}: {price}')


favorite_food('Apple', 'Banana', "Fraise", tomato = '$5', cucumber = '$3', salad = '$10')

