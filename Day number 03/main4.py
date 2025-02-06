print('welcome to the rollercoaster!')
height = int(input('what is your height in cm?'))
bill = 0

if height >= 120:
    print('you can ride the rollercoaster')
    age = int(input('enter your age'))
    if age <= 12:
        bill = 5
        print('child tickets are $5. ')
    elif age <= 18:
        bill = 7
        print('youth tickets are $7. ')
    elif age >= 45 and age <= 55:
        print('everything is going to be ok. Have a free ride on us!')
    
    else:
        print('adult tickets are $12. ')
        bill = 12
    wants_photo = input('do tou want to have a photo take? Type y for yes and Type n for no')
    if wants_photo == "y":
        bill += 3
    print(f'your final bill is : ${bill}')
else:
    print('sorry you have to grow taller before you can ride. ')
