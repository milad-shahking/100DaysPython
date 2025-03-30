def is_even(num):
    return num % 2 == 0

print(is_even(4))


my_numbers = [1,8,4,6,7,2,12,58,44,95,852]


def number_of_evevns(nums):
    count = 0
    for n in nums:
        if is_even(n):
            count += 1
    return count

print(number_of_evevns(my_numbers))


def any_even_in_list(nums):
    for n in nums:
        if is_even(n):
            return True
    return False

print(any_even_in_list(my_numbers))


def largest(nums):
    largest_number = nums[0]
    for n in nums:
        if largest_number < n:
            largest_number = n
    return largest_number

print(largest(my_numbers))

def get_odds(nums):
    my_list = []
    for n in nums:
        if not is_even(n):
            my_list.append(n)
    return my_list

print(get_odds(my_numbers))
print(len(get_odds(my_numbers)))