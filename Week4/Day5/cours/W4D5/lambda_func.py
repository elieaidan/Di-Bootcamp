# l = [num for num in range(1, 11)]

# print(l)

# def add_two(a: int, b: int) -> int:
#     result = a + b 
#     return result

# function name = lambda parametets (a, b) : what to return
add_two = lambda a, b: a + b

res = add_two(1, 2)
print(res)

multiply_two = lambda a: a * 2

print(multiply_two(2))