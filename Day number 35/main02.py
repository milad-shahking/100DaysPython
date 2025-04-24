def run_on_zoj(f):
    def wrapper():
        import datetime
        now = datetime.datetime.now()
        minute = now.minute
        if minute % 2 == 0:
            f()
        else:
            print('Hisssssss')
    return wrapper
@run_on_zoj
def say_hello():
    print('Hello')
@run_on_zoj
def say_bye():
    print('Bye')


print('---------------')
say_hello()
say_bye()
print('---------------')
