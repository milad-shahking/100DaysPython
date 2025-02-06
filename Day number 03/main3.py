print('welcome to python pizza deliveries!')

size = input("what size pizza do you want? S, M or L: ")
pepperoni = input("do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("do you want extra cheese? Y or N: ")
bill = 0
S = 15
M = 20
L = 25
pepp_S = 2
pepp_M_L = 3
add_cheese = 1
#Small pizza(S) = $15
#Medium pizza(M) = $20
#Large pizza(L) = $25
#add pepp S = $2
#add pepp M & L = $3
#add extra cheese for any size = $1
if size == "S":
    bill += S
elif size == 'M':
    bill += M
elif size == "L":
    bill += L
else:
    print('you typed the wrong inputs. ')

#------------------------------

if pepperoni == "Y":
    if size == "S":
        bill += pepp_S
    else:
        bill += pepp_M_L

#------------------------------
if extra_cheese == "Y":
    bill += add_cheese

print(f'your final bill is: ${bill}')
