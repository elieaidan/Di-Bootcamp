even_numbers = []
range_numbers = 100

for num in range(range_numbers):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

                    #[what to add for variable in Sequence if Condition]
even_numbers: list = [num for num in range(range_numbers) if num % 2 == 0]

print("LIST COMPREHENSION:", even_numbers)


sample_list = [num for num in range(10)]
print(sample_list)


alphabet = 'abcdefghijklmnopqrstuvwxyz'

even_letters = []
for i, letter in enumerate(alphabet):
    if i % 2 == 0:
        even_letters.append(letter)

print("Even letters:", even_letters)

even_letters = [letter for i, letter in enumerate(alphabet) if i % 2 == 0]
print("LIST COMPREHENSION:", even_letters)
