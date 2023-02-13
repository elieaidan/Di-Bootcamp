while True:
    try:
        player_choice = int(input("YOUR CHOICE: "))
        break
    except ValueError as e:
        print(e)

