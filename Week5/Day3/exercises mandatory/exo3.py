import string
import random
 
N = 5
res = ''.join(random.choices(string.ascii_uppercase , k=N))

print(res)