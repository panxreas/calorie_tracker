import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from user_data import *
from calculator import *
from equivalencias import equivalencia

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
        self.root.geometry("550x900")
        self.root.configure(bg=self.bgr)
        self.root.title("Calorie Tracker")

        # Set user
        self.user = None
        self.meals = None
        self.amount_of_meals = 0

        # Set Equi
        self.equi = Alimentos(equivalencia)

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
        self.meals = Meal_sets(self.user)

        ### Widget Layout
        ### --- Main Frame ---
        frame = tk.Frame(self.root, bg=self.bgr)
        frame.pack()

        ## User Info Frmae
        user_menu = tk.LabelFrame(frame, text=self.user.get_name().upper(), bg=self.bgr, fg=self.fgr, font=('Arial', 18))
        user_menu.grid(row=0, column=0, pady=(10, 5))
        
        title = f'Daily calories for {self.user.get_name().title() }: '
        user_name = tk.Label(user_menu, text=title, bg=self.bgr, fg=self.fgr, font=('Arial', 12))
        user_name.grid(row=0, column=0, sticky='news')
        user_kcals = tk.Label(user_menu, text=self.user.get_kcal(), bg=self.bgr, fg=self.fgr, font=('Arial', 12))
        user_kcals.grid(row=0, column=1, sticky='news')

        counter = 1
        for groups in list(self.user.__dict__.items())[2:]:
            food = tk.Label(user_menu, text=groups[0].title(), bg=self.bgr, fg=self.fgr, font=('Arial', 12), anchor='w')
            food.grid(row=counter, column=0, sticky='nws')
            amount = tk.Label(user_menu, text=groups[1], bg=self.bgr, fg=self.fgr, font=('Arial', 12))
            amount.grid(row=counter, column=1, sticky='nes')
            counter += 1
            print(groups)

        ## User Meal Sets Frmae
        meals_frame = tk.LabelFrame(frame, text='Daily meals', bg=self.bgr, fg=self.fgr, font=('Arial', 18))
        meals_frame.grid(row=1, column=0, pady=(10,5))
        meals_frame.grid_columnconfigure(0, weight=1)

        def add_meal():

            submited = False

            ## Food group combobox display items
            def display_options(event):
                selection = add_portion_entry.get()
                display_amount_entry['values'] = []
                display_amount_entry.set('')
                amount_label.config(text='')
                if selection.lower() == 'frutas':
                    display_amount_entry['values'] = list(self.equi.get_frutas().keys())
                elif selection.lower() == 'verduras':
                    display_amount_entry['values'] = list(self.equi.get_verduras().keys())
                elif selection.lower() == 'cereales':
                    display_amount_entry['values'] = list(self.equi.get_cereales().keys())
                elif selection.lower() == 'leguminosas':
                    display_amount_entry['values'] = list(self.equi.get_leguminosas().keys())
                elif selection.lower() == 'lacteos':
                    display_amount_entry['values'] = list(self.equi.get_lacteos().keys())
                elif selection.lower() == 'grasas':
                    display_amount_entry['values'] = list(self.equi.get_grasas().keys())
                elif selection.lower() == 'proteinas':
                    display_amount_entry['values'] = list(self.equi.get_proteinas().keys())
           
            ## Combo box display items
            def display_amount(event):
                group = add_portion_entry.get()
                selection = display_amount_entry.get()
                value = getattr(self.equi, group.lower())
                amount = value[selection]
                amount_label.config(text=f'{amount}')
            
            def delete_item(touple, button):
                touple[0].destroy()
                touple[1].destroy()
                group = touple[2]
                dictionary = touple[3]
                if dictionary in meal.get_food()[group]:
                    meal.del_food(group, dictionary)
                else:
                    print('ERROR')
                button.destroy()
                update_menu()

            def update_menu():
                children = [label.cget('text').lower() for label in menu_display.winfo_children() if isinstance(label, tk.Label)]
                for child in menu_display.winfo_children():
                    child.destroy()

                row_counter = 0
                for food_group in meal.get_food():
                    if food_group not in children:
                        group_label = tk.Label(menu_display, text=food_group.capitalize(), bg=self.bgr, fg=self.fgr, font=('Arial', 12), width=11, anchor='w')
                        group_label.grid(row=row_counter, column=0)
                        group_no = 1
                        group_no_label = tk.Label(menu_display, text=str(group_no), bg=self.bgr, fg=self.fgr, font=('Arial', 12), width=2, anchor='w')
                        group_no_label.grid(row=row_counter, column=1, sticky='ew')
                    else:
                        group_label = tk.Label(menu_display, text=food_group.capitalize(), bg=self.bgr, fg=self.fgr, font=('Arial', 12), width=11, anchor='w')
                        group_label.grid(row=row_counter, column=0)
                        group_no = len(meal.get_food()[food_group])
                        group_no_label = tk.Label(menu_display, text=str(group_no), bg=self.bgr, fg=self.fgr, font=('Arial', 12), width=2, anchor='w')
                        group_no_label.grid(row=row_counter, column=1, sticky='ew')

                    for food_elements in meal.get_food()[food_group]:
                        key = list(food_elements.keys())
                        value = list(food_elements.values())
                        food_label = tk.Label(menu_display, text=key[0], bg=self.bgr, fg=self.fgr, font=('Arial', 10), width=24)
                        food_label.grid(row=row_counter, column=3)
                        amount_label = tk.Label(menu_display, text=value[0], bg=self.bgr, fg=self.fgr, font=('Arial', 10), width=24)
                        amount_label.grid(row=row_counter, column=4)
                        item = (food_label, amount_label, food_group, {key[0]: value[0]})
                        delete_button = tk.Button(menu_display, text='DEL -', font=('Arial', 10), width=3, command=lambda item=item: delete_item(item, delete_button))
                        delete_button.grid(row=row_counter, column=2)
                        row_counter += 1

            def check_input():
                if amount_label['text'] != '':
                    key = add_portion_entry.get().lower()
                    selection = display_amount_entry.get()
                    value = getattr(self.equi, key)
                    meal.add_food(key, {selection: value[selection]})
                    update_menu()

            def submit_meal():
                if len(meal.get_food()) == 0:
                    tk.messagebox.showwarning(title='Meal is empty', message='Please add food element to your meal')
                else:
                    self.meals.add_meal(meal)
                    submited = True
                    for children in new_meal_frame.winfo_children():
                        children.destroy()
                    new_meal_frame.destroy()
                    print(self.meals)


            ## Meal class
            meal = Meal()

            for widget in meals_frame.winfo_children():
                widget.destroy()
            new_meal_frame = tk.Frame(meals_frame, bg=self.bgr)
            new_meal_frame.pack()
            info = tk.Label(new_meal_frame, text='', bg=self.bgr, fg=self.fgr, font=('Arial', 12), anchor='w')
            info.grid(row=0, column=0, columnspan=2)

            # Menu Entry
            add_portion = tk.Button(new_meal_frame, text='ADD +', command=check_input, bg=self.bgr, fg=self.fgr, font=('Arial', 10), anchor='w')
            add_portion.grid(row=1, column=0, padx=(10,5))
            add_portion_entry = ttk.Combobox(new_meal_frame, values=list(equivalencia.keys()), state='readonly', width=12)
            add_portion_entry.grid(row=1, column=1)
            add_portion_entry.bind("<<ComboboxSelected>>", display_options)
            display_amount_entry = ttk.Combobox(new_meal_frame, state='readonly', width=16)
            display_amount_entry.grid(row=1, column=2)
            display_amount_entry.bind("<<ComboboxSelected>>", display_amount)
            amount_label = tk.Label(new_meal_frame, text='', bg=self.bgr, fg=self.fgr, font=('Arial', 8), anchor='e', width=14, wraplength=90, justify='left')
            amount_label.grid(row=1, column=3, padx=(5,10), sticky='news')
            menu_display = tk.LabelFrame(new_meal_frame, text='Current meal', bg=self.bgr, fg=self.fgr, font=('Arial', 10))
            menu_display.grid(row=2, column=0, padx=(10,10), pady=(10,10), columnspan=4, sticky='ew')
            menu_display.grid_columnconfigure(0, weight=1)
            menu_display.grid_columnconfigure(3, weight=1)
            menu_display.grid_columnconfigure(4, weight=1)
            submit_button = tk.Button(new_meal_frame, text='Save Meal', command=submit_meal)
            submit_button.grid(row=3, column=0, columnspan=6, sticky='ew', padx=(10,10), pady=(10,10))
            print(self.meals.meal_sets)

            if submited:
                for children in new_meal_frame.winfo_children():
                    children.destroy()
                new_meal_frame.destroy()
                return

        def display_meals():
            # Meals
            for i in self.meals.meal_sets:
                print(i)

            # Button
            add_meal_button = tk.Button(meals_frame, text='Add meal', command=add_meal)
            add_meal_button.grid(row=self.amount_of_meals, column=0, sticky='news')
        
        display_meals()

    def start(self):
        self.root.mainloop()
