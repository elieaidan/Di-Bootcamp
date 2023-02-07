total = 0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

age = family["rick"]



for i in family:
   
    if family[i] == 0:
        break
    elif  family[i] < 3:
        pass
    elif  family[i] < 12 and  family[i]> 3:
        total += 10
    else:
        total+= 15


print(total)