from collections import Counter
from collections import namedtuple
from collections import defaultdict


mylist = [1, 2, 3, 4, 1, 2, 8, 1]
print(Counter(mylist))
print(Counter(mylist).get(1))

Kelas = namedtuple('Kelas',['tedad', 'avg', 'ostad'])
print(Kelas)

fizik = Kelas(tedad=44, avg= 15, ostad='milad')
print(fizik.ostad)

a = dict()
a['name'] = 'milad'
print(a['name'])

d = defaultdict(lambda: 20)

d['name'] = 'shah'

print(d)
print(d['family'])