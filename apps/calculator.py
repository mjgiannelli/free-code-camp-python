num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))
operator = input('Enter what operator you\'d like to perform: +, -, *, or /: ').lower()

def calculate(num1, num2, operator):
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)
    else:
        print("Invalid Operator. Please enter '+', '-', '*', or '/' only for operator input")

calculate(num1, num2, operator)
