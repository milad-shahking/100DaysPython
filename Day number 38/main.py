import re


data = '''milad has a phone 3456 bits number 4 is +989379050015 and phone mode
6037-9923-4567-8910
5892-1234-5678-9012
6104-3345-6677-8899
6274-5566-7788-9900
6393-1122-3344-5566
5047-9988-7766-5544
6219-4455-6677-8890
6273-3210-4321-5432 
5022-3456-7890-1234
6362-9087-6543-2109 '''
check = 'phone' in data
print('-----------------')
print(check)
print('-----------------')
check_one = re.search(r'phone', data)
print(check_one)
print('-----------------')
print(check_one.start())
print(check_one.end())
find_char = re.findall(r'phone', data)
print(find_char)
print('----------------------------')
for match in re.finditer(r'phone', data):
    print(match)
print('----------------------------')
find_int = re.search('\d', data)
find_int_all = re.findall(r'\d', data)
print('----------------------------')
print(find_int)
print(find_int_all)
print('----------------------------')
search_phone_number = re.search(r'\+\d+', data)
print(search_phone_number)
print('----------------------------')
find_cart_number = re.findall(r'\d{4}-\d{4}-\d{4}-\d{4}', data)

print(find_cart_number)
pattern = re.compile(r'(\d{4})-\d{4}-\d{4}-\d{4}')
matches = re.finditer(pattern, data)
#for match in matches:
#    print(match)

print('-----------------------------------------')

for match_two in matches:
    print(match_two.group(1))