def re_print(name = 'please enter a name', count = 1):
    '''
        print name as count times
    '''
    for i in range(count):
        print(name)



print('-----')
re_print('milad',3)
print('-----')
re_print('lili')
print('-----')
re_print() 
print('-----')

def tavan(num , tav):
    answer = 1
    for i in range(tav):
        answer = answer * num
    return answer


print(tavan(2,5))

print('-----')

def sum_of_two(num_one = 1, num_two = 1):
    answer = num_one + num_two
    return answer

print(sum_of_two(45, 4))
print(sum_of_two(23))