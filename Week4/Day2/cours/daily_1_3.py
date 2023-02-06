import random

# 1
user_in: str = input("Your input: ")

if len(user_in) < 10:
    print("string not long enough")
elif len(user_in) > 10:
    print("string is too long")
else:
    print("10 characters long string!")

# 2 
first_char: str = user_in[0]
last_char: str = user_in[-1]

print(f"First character: {first_char} | Last character: {last_char}")

# 3
result: str = ""
for char in user_in:
    # 1 iteration - char = S 
    # 2 iteration - char = t
    # 3 iteration - char = r
    # ... 
    result += char
    # 1 iteration - result = S 
    # 2 iteration - result = St
    # 3 iteration - result = Str 
    print(result)
