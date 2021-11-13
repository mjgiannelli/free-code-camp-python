a = 5
b = 5

if a > b:
    print(a, 'is greater than', b)
elif a == b:
    print(a, 'is equal to', b)
else:
    print(b, 'is greater than', a)

c = False

if c == True:
    print('c is True')

if c != True:
    print('c is False')

if a >= b:
    print('True')

if a == b:
    print('a equals b')
else: 
    print('a is not equal to b')

def odd_or_even(num):
    if num % 2 == 0:
        print(num, 'is even.')
    else:
        print(num, 'is odd.')

odd_or_even(54)

boy = False
short = False

if boy == True or short == True:
    print('he is a boy or they are short')
else:
    print('she is tall')

boy = True
tall = True

if boy == False and tall == True:
    print('she is tall')
else:
    print('the person is either a boy or short')

value = int(input('Input a number: '))

if value % 5 == 0:
    print(value, 'is divisible by 5')
else:
    print(value, 'is NOT divisible by 5')

