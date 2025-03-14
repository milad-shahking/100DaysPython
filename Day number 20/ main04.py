fruit_price = {
    'apple' : 1500,
    'benana' : 1000,
    'orange' : 1200
}

fruit_price['benana'] = 1100
print(fruit_price)
del fruit_price['apple']
print(fruit_price)
#------------ OR
fruit_price['apple'] = ''
print(fruit_price)
