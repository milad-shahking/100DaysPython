listchar = []
word = 'milad shah'
for char in word:
    if char == ' ':
        continue
    listchar.append(char)
print(listchar)
#-------------------------------------------------

listNumber = [num for num in range(101) if num % 2 == 0 if num % 5 == 0]
print(listNumber)
#-------------------------------------------------
checkEven = ['Even' if i % 2 == 0 else 'Odd' for i in range(1,21)]
print(checkEven)