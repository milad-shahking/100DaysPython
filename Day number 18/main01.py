myDict2 = {'a': 10, 'b': 12}
#print(myDict)
#if 'a' in myDict:
#    del myDict['a']

#print(myDict)

myDict1 = {'c': 10, 'd': 12}

for dict_key , dict_value in myDict1.items():
    print(dict_key , ' ==> ' , dict_value)

myDict = myDict1.copy()
myDict.update(myDict2)
print(myDict)



#i need to learn python part 2 section 06 lists