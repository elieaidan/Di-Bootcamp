import re


matrix = [ 
    ["7","i","3"]
    ["T","s","i"]
    ["h","%","x"]
    ["i","#"]
    ["s","M"] 
    ["$","a"] 
    ["#","t","%"]
    ["^","r","!"] 

]

ex = "^r!"
new_ex = re.sub("[^0-9a-zA-Z]+", " ", ex)
print(new_ex)