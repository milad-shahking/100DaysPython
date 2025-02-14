import random
word_list = ['milad', 'leila', 'khashayar']
#all_letters = set("".join(word_list))

enter_letter = input('please enter your choice : ')


#if any(enter_letter in word for word in word_list): # type: ignore
#    print('Yes')
#else:
#    print('No')
# work------



#found = False
#for char in word_list:
#    if enter_letter in word_list:
#        found = True
#        break
#if found:
#    print('Yes')
#else:
#    print('No')
# Doesn't work


#if enter_letter in word_list:
#    print("Yes")
#else:
#    print('No')
# work

#found_words = []

#for word in word_list:
#    if enter_letter in word:
#        found_words.append(word)

#if found_words:
#    print(' '.join(found_words))
#else:
#    print('there is not this letter in words')


chosen_word = random.choice(word_list)
print(chosen_word)

guess = input('guess a letter: ').lower()

for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')