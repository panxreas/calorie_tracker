from elements import *
from user_data import *
from equivalencias import equivalencia
import tkinter as tk

def main():

    ### This section has to load user data 
    if check_user_data():
        print('Loading user data...')
        user = load_user_data()
    else:
        print('No user data, create user')
        user = create_user()
        save_user_data(user)

    print(user)
    user.get_data()


    ### This section sets up the Tk GUI

    # Colors
    bgr = '#363636'
    fgr = '#A8A7A8'

    root = tk.Tk()
    root.geometry("500x900")
    root.configure(bg='#363636')
    root.title("Calorie Tracker")
    label = tk.Label(root, text=user.get_name().upper(), bg=bgr, fg=fgr, font=('Arial', 18))
    label.pack(pady=(30, 0))
    label2 = tk.Label(root, text=user.get_kcal(), bg=bgr, fg=fgr, font=('Arial', 18))
    label2.pack(pady=5)
    root.mainloop()



if __name__ == '__main__':
    main()
