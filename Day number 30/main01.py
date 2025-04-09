class Book():
    book_type = 'Action'
    def __init__(self, page):
        self.pages = page
    def open(self):
        print(f'open the book {self.pages}')

b = Book(120)
print(b.pages)
print(b.open())
print(b.book_type)
c = Book(522)
c.book_type = 'fun'

print(c.book_type)

print('---------------------------')

class Circle():
    pi = 3.1415926
    def __init__(self, r):
        self.r = r
    def masahat(self):
        m = self.r * self.r * Circle.pi
        return m
    
ci = Circle(14)
print(ci.masahat())
