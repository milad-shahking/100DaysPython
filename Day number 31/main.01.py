class Book():
    def __init__(self, name, page):
        self.pages = page
        self.name = name
    def open(self):
        print(f'opened th {self.name} which has {self.pages} pages')
    def __len__(self):
        return self.pages
    def __str__(self):
        r = f'{self.name} and {self.pages}'
        return r
    def __del__(self):
        print(f'Oh the {self.name} was deleted')




b = Book('c Programming', 455)

print(len(b))
print(str(b))

del(b)
print(len(b))
print('milad')
