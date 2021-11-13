# LIST BASICS

# lists can have different types just like in javascript
countries = ['USA', 'United Kingdom', 4, 'Nigeria', True, 'Australia']

names = list(('Mark', 'Mat', 'Erica', 'Chris'))

countries[0] = 'United States'
names[0] = 'Dave'

print(countries)
print(len(countries))
print(type(countries[2]))

print(names)

# LIST METHODS

list1 = [1, 2, 3, 4, 5]
list2 = ['banana', 'apples', 'mangos', 'oranges', 'mangos']

# adds list2 to the end of list1
list1.extend(list2)

print(list1)

# adds cherry to end of list2
list2.append('cherry')

#adds pineapple to list2 at index 2
list2.insert(2, 'pineapples')

#removes banana from list
list2.remove('banana')

print(list2)
print(list2.index('pineapples'))
print(list2.count('mangos'))


#empties list
list2.clear()

print(list2)

list3 = [4, 3, 5, 1, 2]
list3.sort()
print(list3)

list3.reverse()
print(list3)

#make list4 a duplicate of list3
list4 = list3.copy()

print(list4)

#remove last item from list
list4.pop()
print(list4)

#remove item at specific index
list4.pop(1)
print(list4)

#another method to remove an item of a list

del list4[0]
print(list4)

#delete variable entirely
del list4
