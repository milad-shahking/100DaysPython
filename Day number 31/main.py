class Runner():
    def __init__(self, name):
        self.name = name
    def action(self):
        print(f'{self.name} is runing')

sara = Runner('sara')

class Cyclist():
    def __init__(self, name):
        self.name = name
    def action(self):
        print(f'{self.name} is biking')

jadi = Cyclist('jadi mirmirani')


myName = Runner('miald')
herName = Cyclist('lili')

listName = [jadi, sara, myName, herName]

for person in listName:
    person.action()