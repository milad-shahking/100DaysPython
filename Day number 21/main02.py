myset = set()
yourset = set()
myset.add(4)
myset.add(12.5)
myset.add('milad')
myset.add(True)
yourset.add(45)
yourset.add('lili')
yourset.add(12.5)

sumset = myset.union(yourset)
print(myset)
print(yourset)
print(sumset)
intersectionset = myset.intersection(yourset)
print(intersectionset)

#print(myset + yourset) doesn't work

