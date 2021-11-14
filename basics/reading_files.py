#import file to read: param 1 = file path, param 2 = action
    # r = read
    # w = write
    # a = append
    # r+ = reading and writing

country_file = open('C:/Users/giann/Desktop/Python Coding/free-code-camp-python/basics/countries.txt', 'r')

# checks if file can be read
print(country_file.readable())

#  can use a for loop to read through all the lines
for line in country_file.readlines():
    print(line)

#prints every line in a list/ if index specified it will read that line
# print(country_file.readlines())

# prints next line - will not run after the readlines command runs
print(country_file.readline())
# prints next line
print(country_file.readline())




# need to make sure to close the file after done
country_file.close()