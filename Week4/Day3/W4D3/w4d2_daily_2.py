# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon

in_str: str = "hello"

result_str = in_str[0]

# result_str = "c"
# INSIDE LOOP
# 1 - result_str = "c" , result_str[-1] = 'c'
# 2 - result_str = "c" , result_str[-1] = 'c'
# 3 - result_str = "c" , result_str[-1] = 'c'
# 4 - result_str = "c" , result_str[-1] = 'c'
# 5 - result_str = "c" , result_str[-1] = 'c'


for char in in_str[1:]:

    if result_str[-1] != char:
        result_str += char

print(result_str)
    