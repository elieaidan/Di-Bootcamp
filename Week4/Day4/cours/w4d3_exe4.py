# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {}

for i, name in enumerate(users):

    disney_users_A[name] = i

print(disney_users_A)



disney_users_B = {}

for i, name in enumerate(users):

    disney_users_B[i] = name

print(disney_users_B)



disney_users_C = {}

users.sort() # sort the users list

for i, name in enumerate(users):
    disney_users_C[name] = i

print(disney_users_C)
