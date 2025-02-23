a = {1, 2 ,3 ,4}
b = {5, 7, 6, 4, 3}


print(a| b)
# or
print(a.union(b))

# =================

print(a & b)
# or
print(a.intersection(b))

# =================

print(a - b)
# or
print(a.difference(b))

# =================

print(a ^ b)
# or
print(a.symmetric_difference(b))