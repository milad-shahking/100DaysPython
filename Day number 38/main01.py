from decimal import *



print(0.1 + 0.2 == 0.3)
print(0.1 + 0.2)
mogayese = Decimal('0.1') + Decimal('0.2') == Decimal('0.3')

print(mogayese)



list_number = '1.5 2.5 5.1 8.8'
new_list = list_number.split()
data = list(map(Decimal, new_list))
print(sum(data))
print(min(data))