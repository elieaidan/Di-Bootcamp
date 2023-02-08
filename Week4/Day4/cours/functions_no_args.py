def print_hello():
    print("Hello")

# '_' a variable that is not used
for _ in range(10): 
    print_hello()

num1: int = 5

# No return function
def no_return() -> None:
    print("SOMETHING")
    return

# With return function
def with_return() -> int:
    result = num1 * 10
    return result

no_return()
# print(with_return())

l: list = [6,12,3,5,3,1]

# .sort function - returns None, changes list
l.sort()
print(l)

# sorted function - returns a new sorted list, doesn't change the original
l: list = [6,12,3,5,3,1]
l_sorted = sorted(l)
print(l_sorted)