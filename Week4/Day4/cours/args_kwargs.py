def calculate_age(year: int, current_year: int = 2023) -> int:
    age = current_year - year
    return age

age_1 = calculate_age(year = 1991)
print(age_1)

age_2 = calculate_age(year = 1970, current_year = 1991)
print(age_2)

