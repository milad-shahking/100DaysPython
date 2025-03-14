numbers = {'riazi': 12, 'programming': 15, 'motoon' : 4}

print(numbers['programming'])

students = {
    'milad':{
        'math' : 18,
        'art' : 17,
        'sport' : 14
    },
    'lili':{
        'math' : 20,
        'art' : 16,
        'sport' : 17
    }
    }

print(students['lili']['art'])

price = {'apple' : 450, 'benana' : 851, 'cucomber' : 400}

print(price.keys())

print(price.get('cucomber'))
print(price.get('orange', 'is not key'))

rooms = {
    'room1' : ['milad', 'lili'],
    'room2' : ['shah', 'poor']
}
rooms['room3'] = ['person1','person2']
print(rooms)
print(rooms['room1'][1].upper())