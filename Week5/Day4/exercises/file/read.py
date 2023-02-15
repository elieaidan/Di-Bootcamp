file_location1 = 'file/file.txt'

file_list = []

with open(file_location1, 'r') as f:
    file_list= f.readlines()

print(file_list)    

print(file_list[4])



file_text = ""

with open(file_location1, 'r') as f:
    file_text= f.read()



print(file_text[5])

