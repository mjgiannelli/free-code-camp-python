country_file = open('C:/Users/giann/Desktop/Python Coding/free-code-camp-python/basics/country.txt', 'w')

# overwrites anything existing in the file so mainly used to write a new file
country_file.write('This is the new country file')


# need to make sure to close the file after done
country_file.close()

# change the 'w' to an 'a' in the open method to add to the file
country_file = open('C:/Users/giann/Desktop/Python Coding/free-code-camp-python/basics/country.txt', 'a')

country_file.write('\nThis is the second line')

# need to make sure to close the file after done
country_file.close()

# can create python files as well
new_python_file = open('C:/Users/giann/Desktop/Python Coding/free-code-camp-python/basics/new_python_file.py', 'w')

new_python_file.write('print("this is a new file")')

new_python_file.close()