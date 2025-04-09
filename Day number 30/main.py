l = [1,2,3,5,6,4,8,9]

print(l.index(4))

class Test():
    pass

t = Test()
print(type(t))

class Book():
    def __init__(self, pages):
        self.page = pages

myBook = Book(100)

print(myBook.page)
print(type(myBook))
