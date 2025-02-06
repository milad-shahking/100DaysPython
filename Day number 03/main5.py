print('Welcome to treasure island your mission is to find the treasure')

choose_number_one = input('left Or right? ').lower()



if choose_number_one == "right":
    choose_number_two = input('swim Or wait? ')
    if choose_number_two == "wait":
        choose_number_three = input('which door? ')
        if choose_number_three == "yellow":
            print("You Win!!")
    else:
        ('Game Over')
else:
    print('Game Over')
