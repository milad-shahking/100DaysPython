class ClassName():
    def __init__(self, param1):
        self.param1 = param1
        print('object created')
    def say_hello(self):
        print('hello')

t = ClassName(5)
print(t.param1)

