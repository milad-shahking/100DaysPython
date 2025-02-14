word_list = ['milad', 'leila', 'khashayar']


enter_letter = input('please enter your choice : ')


if any(enter_letter in word for word in word_list): # type: ignore
    print('Yes')
else:
    print('No')


