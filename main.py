total = float(input('what was the total bill?'))
tip = int(input('How much tip would you like to give?'))
split = int(input('How many people to split the bill?'))

tipPerson = (tip / 100) * total
tipPersonTotal = total + tipPerson
totalPay = tipPersonTotal / split
print(f'Each person should: {round(totalPay,1)}')

