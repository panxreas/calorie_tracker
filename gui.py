import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from user_data import *

class GUI:

    def __init__(self):

        # Colors
        self.bgr = '#363636'
        self.fgr = '#A8A7A8'
        self.contrast = '#474747'
        self.hilight = '#E8175D'
        self.color = '#CC527A'

        # Set window
        self.root = tk.Tk()
        self.root.geometry("500x900")
        self.root.configure(bg=self.bgr)
        self.root.title("Calorie Tracker")

        # Set user
        self.user = None

    def user_creation_page(self):

        def enter_data():
            first_name = first_name_entry.get().strip()
            last_name = last_name_entry.get().strip()
            kcal_value = user_kcal_entry.get()
            fruit = user_fruit_entry.get()
            vegetable = user_vegetable_entry.get()
            cereal = user_cereal_entry.get()
            legume = user_legume_entry.get()
            dairy = user_dairy_entry.get()
            fat = user_fat_entry.get()
            protein = user_protein_entry.get()

            user_data = {
                    'First name': first_name,
                    'Last name': last_name,
                    'Kcal': kcal_value,
                    'Fruit': fruit,
                    'Vegetables': vegetable,
                    'Cereal': cereal,
                    'Legume': legume,
                    'Dairy': dairy,
                    'Fat': fat,
                    'Protein': protein,
                    }

            flag = True
            for var, value in user_data.items():
                print(value.isalpha())
                if value == '':
                    tk.messagebox.showwarning(title='Missing values', message=f'The {var} parameter is empty.')
                    flag = False
                    break
                elif (var == 'First name' and not value.isalpha()) or (var == 'Last name' and not value.isalpha()):
                    tk.messagebox.showwarning(title='Invalid Name', message='Name must be only letters')
                    flag = False
                    break
                elif (var != 'First name' and var != 'Last name' and var != 'Kcal') and  value == 'Free':
                    continue
                elif (var != 'First name' and var != 'Last name') and not value.isdigit():
                    tk.messagebox.showwarning(title='Invalid value', message=f'{var} amount must be whole numbers.')
                    flag = False
                    break
            if flag:
                return user_data

        def create_user():
            data = enter_data()
            if data:
                user = generate_user(data)
                self.user = user
                save_user_data(user)
                self.switch_main_page()

        ###   Main Frame ----------
        frame = tk.Frame(self.root, bg=self.bgr)
        frame.pack(pady=(15, 0))

        ###   Saving user info --------------------------------------------------------------------------------------

        ## User Name Frame
        user_info_frame = tk.LabelFrame(frame, text='User Information', bg=self.bgr, fg=self.fgr, font=('Arial', 14))
        user_info_frame.grid(row=0, column=0, sticky='news', pady=(18,0))

        # Titles
        first_name_label = tk.Label(user_info_frame, text='Fist Name', bg=self.bgr, fg=self.fgr, font=('Arial', 12))
        first_name_label.grid(row=0, column=0)
        last_name_label = tk.Label(user_info_frame, text='Last Name', bg=self.bgr, fg=self.fgr, font=('Arial', 12))
        last_name_label.grid(row=0, column=1)

        # Info Boxes
        first_name_entry = tk.Entry(user_info_frame)
        last_name_entry = tk.Entry(user_info_frame)
        first_name_entry.grid(row=1, column=0, padx=(6,3), pady=(1,3))
        last_name_entry.grid(row=1, column=1, padx=(3,6), pady=(1,3))

        ## User Diet Frame
        diet_info_frame = tk.LabelFrame(frame, text='Diet Information', bg=self.bgr, fg=self.fgr, font=('Arial', 14))
        diet_info_frame.grid(row=1, column=0, sticky='news', pady=(18,0))
        diet_info_frame.grid_columnconfigure(0, weight=1)
        diet_info_frame.grid_columnconfigure(1, weight=1)

        # Diet Kcal
        user_kcal_label = tk.Label(diet_info_frame, text='Daily Calories', bg=self.bgr, fg=self.fgr, font=('Arial', 12))
        user_kcal_label.grid(row=0, column=0, sticky='w', padx=(6,3), pady=(9,3))
        user_kcal_entry = tk.Entry(diet_info_frame)
        user_kcal_entry.grid(row=0, column=1, sticky='e', padx=(3,6), pady=(9,3))

        # Diet Amounts
        food_values = [x for x in range(11)]
        food_values.insert(0, 'Free')
  
        user_fruit_label = tk.Label(diet_info_frame, text='Fruit Amount', bg=self.bgr, fg=self.fgr, font=('Arial', 12))
        user_fruit_label.grid(row=1, column=0, sticky='w', padx=(6,3), pady=(1,3))
        user_fruit_entry = ttk.Combobox(diet_info_frame, values=food_values)
        user_fruit_entry.grid(row=1, column=1, sticky='e', padx=(3,6), pady=(1,3))

        user_vegetable_label = tk.Label(diet_info_frame, text='Vegetable Amount', bg=self.bgr, fg=self.fgr, font=('Arial', 12))
        user_vegetable_label.grid(row=2, column=0, sticky='w', padx=(6,3), pady=(1,3))
        user_vegetable_entry = ttk.Combobox(diet_info_frame, values=food_values)
        user_vegetable_entry.grid(row=2, column=1, sticky='e', padx=(3,6), pady=(1,3))

        user_cereal_label = tk.Label(diet_info_frame, text='Cereal Amount', bg=self.bgr, fg=self.fgr, font=('Arial', 12))
        user_cereal_label.grid(row=3, column=0, sticky='w', padx=(6,3), pady=(1,3))
        user_cereal_entry = ttk.Combobox(diet_info_frame, values=food_values)
        user_cereal_entry.grid(row=3, column=1, sticky='e', padx=(3,6), pady=(1,3))

        user_legume_label = tk.Label(diet_info_frame, text='Legume Amount', bg=self.bgr, fg=self.fgr, font=('Arial', 12))
        user_legume_label.grid(row=4, column=0, sticky='w', padx=(6,3), pady=(1,3))
        user_legume_entry = ttk.Combobox(diet_info_frame, values=food_values)
        user_legume_entry.grid(row=4, column=1, sticky='e', padx=(3,6), pady=(1,3))

        user_dairy_label = tk.Label(diet_info_frame, text='Dairy Amount', bg=self.bgr, fg=self.fgr, font=('Arial', 12))
        user_dairy_label.grid(row=5, column=0, sticky='w', padx=(6,3), pady=(1,3))
        user_dairy_entry = ttk.Combobox(diet_info_frame, values=food_values)
        user_dairy_entry.grid(row=5, column=1, sticky='e', padx=(3,6), pady=(1,3))

        user_fat_label = tk.Label(diet_info_frame, text='Fat Amount', bg=self.bgr, fg=self.fgr, font=('Arial', 12))
        user_fat_label.grid(row=6, column=0, sticky='w', padx=(6,3), pady=(1,3))
        user_fat_entry = ttk.Combobox(diet_info_frame, values=food_values)
        user_fat_entry.grid(row=6, column=1, sticky='e', padx=(3,6), pady=(1,3))

        user_protein_label = tk.Label(diet_info_frame, text='Protein Amount', bg=self.bgr, fg=self.fgr, font=('Arial', 12))
        user_protein_label.grid(row=7, column=0, sticky='w', padx=(6,3), pady=(1,3))
        user_protein_entry = ttk.Combobox(diet_info_frame, values=food_values)
        user_protein_entry.grid(row=7, column=1, sticky='e', padx=(3,6), pady=(1,3))

        ## Submit button frame
        button_frame = tk.LabelFrame(frame, text='Create User', bg=self.bgr, fg=self.fgr, font=('Arial', 14))
        button_frame.grid(row=2, column=0, sticky='news', pady=(18,0))
        button_frame.grid_columnconfigure(0, weight=1)

        # Button
        create_user_button = tk.Button(button_frame, text='Confirm', command=create_user)
        create_user_button.grid(row=0, column=0, sticky='news', pady=(9,9), padx=(21,21))

    def switch_main_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.main_page()

    def main_page(self):
        # Widget Layout
        self.label = tk.Label(self.root, text=self.user.get_name().upper(), bg=self.bgr, fg=self.fgr, font=('Arial', 18))
        self.label.pack(pady=(10, 5))

    def start(self):
        self.root.mainloop()
