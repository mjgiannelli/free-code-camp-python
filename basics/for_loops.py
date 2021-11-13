for letter in 'Hello':
    print(letter)

mylist = ['Mark', 'John', 'Paul']

for name in mylist:
    print(name)
    if name == 'John':
        break

my_dict = {
    'name': 'Mark',
    'name': 'Pauly',
    'age': 33,
    'nationality': 'American',
    'qualification': 'Grad School',
    'friends': ['Peter', 'John', 'Geoff']
}

for key, value in my_dict.items():
    print(key, ':', value)

for x in range(4, 8):
    print(x)
else:
    print('Finished looping.')