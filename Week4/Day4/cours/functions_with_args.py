def multiply_10(num: int) -> None:
    return num * 10

numbers = list(range(20, 30))

for num in numbers:
    result = multiply_10(num)
    print(result)


def full_name(first_name: str, last_name: str) -> str:
    full_name = f'{first_name} {last_name}'
    print(full_name)
    return full_name

def first_last_name(full_name: str) -> tuple[str, str]: 
    "Yossi Eikelman"
    full_name_list: list = full_name.split(" ")
    first_name: str = full_name_list[0] # Yossi
    last_name: str = full_name_list[1] # Eikelman
    return first_name, last_name

first_name, last_name = first_last_name("Noa Nakache")
print("RESULT:", last_name, first_name)

my_name = full_name("Yossi", "Eikelman")
noa_name = full_name("Noa", "Nakache")

print(my_name)
print(noa_name)

def calculate_age(year: int) -> int:
    age = 2023 - year
    return age

my_age: int = calculate_age(1992)
print(my_age)


