a = 1

def add():
    global a
    a = a + 5
    return a

print(add())

def changeName(name):
    name = 'milad'
    print(name)

x = 'lili'

changeName(x)