PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('What is your password? ')

        if password == PASSWORD:
            return func()
        else:
            print('Invalid password')
    
    return wrapper

@password_required
def needs_password():
    print('Correct Password')    


if __name__ == '__main__':
    needs_password()