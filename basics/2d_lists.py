# nested lists - 2d list means there are rows and columns in the list

my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(my_list)
print(my_list[0])
#get value of 5
print(my_list[1][1])

#nested loops
for lists in my_list:
    for num in lists:
        print(num)