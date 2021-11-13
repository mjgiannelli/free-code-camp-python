# dictionaries are a list with key value pairs that are mutable and DO NOT allow duplicate keys. It will take the last declaration of said key

my_dict = {
    'name': 'Mark',
    'name': 'Pauly',
    'age': 33,
    'nationality': 'American',
    'Qualification': 'Grad School',
    'friends': ['Peter', 'John', 'Geoff']
}

print(my_dict)
print(my_dict['name'])
print(len(my_dict))
print(my_dict['friends'])
print(my_dict['friends'][0])
print(type(my_dict))

x = my_dict['name']
print(x)