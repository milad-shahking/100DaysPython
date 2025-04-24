def add(a, b):
    result = a+b
    return result
def calculate(a, b, f):
    return f(a, b)
print(calculate(1, 2 , add))


def say_hello():
    print('Hello')

def do(what_to_call):
    what_to_call()

do(say_hello)

print('-----------------------')

def calculates(a, b, what_to_do):
    def sum(a,b):
        return a + b
    def multi(a , b):
        return a * b
    
    if what_to_do == 'jam':
        return sum(a,b)
    if what_to_do == 'zarb':
        return multi(a,b)
    

result_one = calculates(4, 5, 'jam')
result_two = calculates(7, 6, 'zarb')


print(result_one)
print(result_two)