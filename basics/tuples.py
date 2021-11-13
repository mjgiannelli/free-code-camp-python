# tuples store multiple items in a single variable (sounds like a list but are immutable)

numbers = (1, 2, 3, 1)

print(numbers)
print(numbers[1])
print(len(numbers))
print(type(numbers))

strings = ('home', 'land', 'earth')
print(strings)

mixed = (1, True, 'Hello')
print(mixed)

#can also use tuple constructor
names = tuple(('Mark', 'John', 'Joe'))
print(names)
print(type(names))