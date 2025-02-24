listNumber = [1,2,3,4,5,6]

for i in listNumber:
    print(i)
else:
    print('print items in list was done')
#-------------------------------------------------


numbers = [11,45,10,2,58,75,30,9,8,51,25,71,43]

for num in numbers:
    if num % 2 == 0:
        print(f'{num} : this number is even number')
    else:
        print(f'{num} : this number is ood number')
#-------------------------------------------------

name = 'milad shah'

for char in name:
    if char == 'd':
        break
    print(char, end='')
print()
#-------------------------------------------------
for char in name:
    if char == 'i':
        continue
    print(char,end='')
print()
#-------------------------------------------------
for char in name:
    if char == 'h':
        pass
    print(char)