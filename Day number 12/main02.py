price = 1500

if price < 500:
    discount = price * 0.05
    print(f'your price is : {discount}')
elif price > 1200:
    discount = price * 0.35
    print(f'your price is : {discount}')
else:
    discount = price * 0.10
    print(f'your price is : {discount}') 