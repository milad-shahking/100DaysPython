# lists

a = ['milad', 12, '@#', 10.2]

b = [12, 25, 45, 7, 3]

c = ['milad', 'shah', 'lilipoo']

d = ('a', 11, '34', '@#')

e = 'milad shah'

print(a[2])

print(10.2 in a)

a[3] = 12.5

b.sort()

print(b)

print(a)

print(10.2 in a)

print(len(a))

print(max(b))

print(max(c,key=len))

print(list(d))

print(list(e))

c.append(444)

print(c)

b.extend(a)

print(b)

a.insert(2, 'lili')

print(a)

a.remove(12)

print(a)

