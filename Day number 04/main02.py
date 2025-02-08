import random


fruits = ['cherry', 'apple', 'pear']


print('-------------------------')
print(fruits[random.randint(0, 2)])
#or
print('-------------------------')
print(random.choice(fruits))
print('-------------------------')
random_index = random.randint(0, 2)
print(fruits[random_index])
print('-------------------------')
