
def sumNumber(a, b, c):
    if a == b or b == c or a == c:
        print('sum is : 0')
    else:
        print(a + b + c)

sumNumber(10, 120, 120)
#-------------------------------------------
def word_count(str):
    counts = dict()
    words = str.split(' ')
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_count('my name is milad milad is my first name'))