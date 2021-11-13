def greeting():
    print('Welcome User')

greeting()

def dynamic_greeting(name):
    print('Welcome', name)

dynamic_greeting('Mark')

def wish_happy_bday(name, age):
    print('Happy ' + str(age) + 'th Birthday, ' + name + '!')

wish_happy_bday('Mark', 34)

#accept multiple names and choose an index to greet
def greeting_multiple_people(*names):
    print('Welcome', names[2])

greeting_multiple_people('Mark', 'John', 'Joe')

name = input('What is your name: ')
age = input('What is your age next year: ')

wish_happy_bday(name, age)