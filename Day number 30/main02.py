class Book():
    def __init__(self, name, page):
        self.pages = page
        self.name = name
    def open(self):
        print(f'opened th {self.name} which has {self.pages} pages')

b1 = Book('c programing', 450)

print(b1.open())

class History(Book):
    def __init__(self, title, sub, name, pages):
        Book.__init__(self, name, pages)
        print('a new subject')
        self.titles = title
        self.subj = sub
    def open(self):
        print(f'opened {self.name} of {self.titles} paye {self.subj}')

c = History('algebra', 2, 'aaaa', 145)

print(c)
print(c.titles)
print(c.pages)
print(c.name)

print(type(c))

