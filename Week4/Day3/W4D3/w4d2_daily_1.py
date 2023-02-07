# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
                          # 1, 2, 3, 4, 5
# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

user_number: int = int(input("Your number: "))
user_length: int = int(input("Your length: "))

result = []

# 1, 2, 3, 4 (5 not included)
# 1, 2, 3, 4, 5 (6 not included)

user_number = 3
user_length = 3

for multipler in range(1, user_length + 1):
    result.append(user_number * multipler)

print(result)


