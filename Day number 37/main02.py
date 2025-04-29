import math
import random

print(math.e)
print(math.inf)
print(math.pow(4,85))
print(round(45.245))
print(math.ceil(4.8))
print(math.degrees(3.14 / 2))
print(random.randint(1,6))

print('------------------------------------')
numbers = range(45)
numbers = list(numbers)
print(numbers)
print('------------------------------------')

game = random.choice(['sang', 'kagaz', 'geychi'])
print(game)
print('------------------------------------')

game_two = random.choices(['sang', 'kagaz', 'geychi'], k = 2)
print(game_two)
print('------------------------------------')

game_three = random.sample(['sang', 'kagaz', 'geychi'], k = 2)
print(game_three)
print('------------------------------------')

random.shuffle(numbers)
print(numbers)