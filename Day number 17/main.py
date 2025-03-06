name = 'miladshah'
#print(name[0:4].upper())
#----------------------------
def changchar(word):
    return word[-1:] + word[1:-1] + word[:1]
print(changchar(name))
#----------------------------
inputTag = ['p' , 'milad']
def add_tag(wordList):
    return f'<{wordList[0]}>{wordList[1]}<{wordList[0]}>'

print(add_tag(inputTag))

# -------- OR 

# do mot work

#def add_tag2(tag, word):
#    return '<%c> %s </%c>'  %(tag, word , tag)

#print(add_tag2('div', 'shahkarami'))


# i need to learn python part2 => section 06 => 01 string => 04 example