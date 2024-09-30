from elements import *
from user_data import *
from equivalencias import equivalencia
from gui import GUI
import tkinter as tk

def main():

#    print(user)
#    user.get_data()

    gui = GUI()


    ### This section has to load user data 
    if check_user_data():
        print('Loading user data...')
        user = load_user_data()
        gui.user = user
        print(user)
        gui.main_page()
    else:
        print('No user data, create user')
        gui.user_creation_page()
    
    gui.start()

if __name__ == '__main__':
    main()
