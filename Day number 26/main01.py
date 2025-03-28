def hello(name, count):
    for i in range(count):
        print(f'salam {name} of indent: {i}')


hello('miladshah', 5)



def sum_of_two_numbers(number_one, number_two):
    answer = number_one + number_two
    return answer

print(sum_of_two_numbers(15, 25))


def chandta_toshe(text, char):
    counter = 0
    for all_char in text:
        if all_char == char:
            counter = counter + 1
    return (counter)


print(chandta_toshe('milad shahkarami', 'i'))