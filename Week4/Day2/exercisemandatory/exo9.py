total = 0 

while True:
    ages = input('What is your age?:  ' )
    if len(ages) == 0:
        break
    elif int(ages) < 3:
        pass
    elif int(ages) < 12 and int(ages)> 3:
        total += 10
    else:
        total+= 15


print(total)





