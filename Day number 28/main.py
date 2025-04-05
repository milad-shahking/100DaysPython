numbers = [1,2,6,8,2,5,3]

def is_even(n):
    return n %2 ==0

def get_odds(nums):
    odds = []
    count = 0

    for n in nums:
        if not is_even(n):
            odds.append(n)
            count += 1
    return odds, count


print('---------------------------')

print(get_odds(numbers))
print('---------------------------')
def sum_multi(num_one, num_two):
    sum_nums = num_one + num_two
    multi_nums = num_one * num_two
    return sum_nums, multi_nums

print(sum_multi(5,8))
print('---------------------------')

donations = {
    'milad' : 511,
    'lili' : 41,
    'sara' : 580,
    'peter' : 4
}

def donations_analysis(dona):
    person = ''
    ave = 0
    total = 0
    max_dona = -1
    count =0

    for name, value in dona.items():
        total += value
        count += 1
        if value > max_dona:
            max_dona = value
            person = name
    ave = total / count
    return total, ave, person


total, ave, person = donations_analysis(donations)
print(f'total dona is : {total}')
print(f'ave dona is : {ave}')
print(f'person dona is : {person}')
print(ave)