print('Create your account')

try:
    username = input('Input username: ')
    password = input('Input password: ')
except:
    print('Invalid inputs')
else:
    print('user \'' + username + '\' created successfully')

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

account_one = Account(username, password)

print('Login now')

login_username = input('Input username: ')
login_password = input('Input password: ')

def check_credentials(username, password):
    if username == account_one.username and password == account_one.password:
        print('User logged in successfully')
    else:
        print('Invalid credentials')

check_credentials(login_username, login_password)