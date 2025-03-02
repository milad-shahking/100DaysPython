def personinfo(*args , **kwargs):
    print(args)
    print(kwargs)


personinfo('married', 'developer', name = 'milad', age = 35)

info1 = ['single', 'operator']
info2 = {'name' : 'lili', 'age' : 35}

print(personinfo(*info1, **info2))