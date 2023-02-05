string = input("Write a string with 10 characters: ")

if len(string) < 10:
    print('string not long enough')
elif len(string) > 10:
    print('string too long')  
else: print(string[0],string[9])



for i in range(1, len(string)+1):
    print(string[:i])

