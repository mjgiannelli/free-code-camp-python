# prevents an error
    # just putting except will trigger on any error. You can specify which error to print that message for

try:
    num1 = int(input('input an integer: '))
    print(num1)
except ValueError:
    print('Value not an integer.')  
#triggers if no errors
else:
    print('No errors present')
#triggers if there is an error or not
finally:
    print('try except finished')

