class Myclass:
    x = 5

p1 = Myclass()

print(p1.x)

# self will always be included when initializing a class // very much like a constructor class in javascript
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# name = input('Enter your name: ')
# age = int(input('Enter your age: '))

# p2 = Person(name, age)

p2 = Person('Mark', 33)

# add a new key to created object
p2.favorite_food = 'steak'

print(p2)
print(p2.name)
print(p2.age)
print(p2.favorite_food)

# delete a property from object
del p2.age

# how to create an class with no keys // use pass to prevent error when declaring class
class Animal:
    pass

class Student():
    name = 'Mark'
    age = 33
    gender = 'male'