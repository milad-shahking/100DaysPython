def calc_factorial(x):
    answer = 1
    for i in range(1, x + 1):
        answer = answer * i
    return answer


print(calc_factorial(100))

print('--------------------------------------------------')

def calc_factorial2(y):
    if y == 1:
        return 1
    else:
        return(y * calc_factorial2(y - 1))
    
print(calc_factorial2(100))