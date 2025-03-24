myList = [1,2,3,4,5,6,7,8,9]

for a in myList:
    if a == 4:
        break
    print(a)

print('Edned')

print('------------------------')
for a in myList:
    if a == 5:
        continue
    print(a)
print('Is Done')
print('------------------------')

num = 0

while num < 100:
    num = num + 1
    if num % 3 == 0 and num % 5 == 0:
        print('hip hop')
        continue
    if num % 3 == 0:
        print('hop')
        continue
    if num % 5 == 0:
        print('hip')
        continue
    if num == 71:
        break
    
    print(num)
