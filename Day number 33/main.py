

def divish(a , b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f'b can not be 0')
        return None
    except Exception as e:
        print(f'Another error : {e}')

print(divish(45,4))
print(divish(4,0))
print(divish('s', False))

print('---------------------')


def divi(a, b):
    try:
        r = a / b
    except Exception as e:
        print(f'had error : {e}')
        r = None
    else:
        print(r)
    finally:
        return r
divi(1,2)