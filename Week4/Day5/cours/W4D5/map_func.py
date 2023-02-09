multiply_two = lambda a: a * 2

numbers: list = [number for number in range(1, 11)]
# [1,2,3,4...]
# [2,4,6,8...]

# for i, number in enumerate(numbers):
#     numbers[i] = multiply_two(number)

numbers = list(map(multiply_two, numbers))

print(numbers)

words = ['abba', 'lincoln', 'rabin', 'table']

# 'abba'.capitalize() -> 'Abba'
# s.capitalize()

capitalize_func = lambda s: s.capitalize()
words = list(map(capitalize_func, words))

print(words)


def first_last_name(full_name: str) -> tuple[str, str]: 
    "Yossi Eikelman"
    # .split - inverse of "".join
    full_name_list: list = full_name.split(" ")
    first_name: str = full_name_list[0] # Yossi
    last_name: str = full_name_list[1] # Eikelman
    return first_name, last_name


full_names = ["Yossi Eikelman", "Noa Nakache"]
res = list(map(first_last_name, full_names))

print(res)