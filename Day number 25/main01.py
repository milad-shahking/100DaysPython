#for i in range(12,32):
    #print(i)

for i in range(5):
    for j in range(5):
        print(i,j)


print('--------------------------')

for i in range(6):
    for j in range(6):
        print(i * j , end=('\t'))
    print()
print('--------------------------')

for i in range(1, 10, 2):
    print(i, end=' ')
print()

print('--------------------------')

for i in range(10, 1 , -2):
    print(i, end=' ')
print()
print('--------------------------')
char = 'milad'
for i in range(len(char)):
    print(i, char[i])
# OR ------
print('----------------------')
for i, a in enumerate(char):
    print(i ,a)
print('--------------------------')

names = ['milad', 'lili', 'kashayar']
family = ['shah', 'poor', 'shah']
age = [35, 35, 12]

for fullname in zip(names, family, age):
    print(fullname)
print('--------------------------')

print('milad' in names)
print('--------------------------')

if 'poor' in family:
    print('yes')
else:
    print('No')
print('--------------------------')

people = {
    'milad' : {'age' : 35, 'gad' : 170},
    'lili' : {'age' : 35, 'gad' : 170},
    'kashayar' : {'age' : 12, 'gad' : 125}
}

for name in names:
    if name in people:
        print(f'i have {name} and sen is {people[name]['age']}')

print('--------------------------')

print(max(1,4,8,98,589,45))
print(min(1,4,8,98,589,45))
print('--------------------------')

from random import randint

print(randint(1, 5))

a = int(input('enter your age: '))
print()
print(a, type(a))

