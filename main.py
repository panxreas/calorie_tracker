from elements import *
from user_data import *
from equivalencias import equivalencia

def main():

    if check_user_data():
        print('Loading user data...')
    else:
        print('No user data, create user')
        create_user()

if __name__ == '__main__':
    main()
