a = 56
res2 = 'Fard' if a % 2 != 0 else 'Zoge'

print(res2)



my_list = [1,5,4,85,95,3,6,44,78]

res = [num for num in my_list if num % 2 == 0 ]

res3 = ['Zoj' if num % 2 == 0 else 'Fard' for num in my_list]
print(res)
print(res3)