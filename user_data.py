import os, pickle
from elements import *
from equivalencias import equivalencia

def check_user_data():
    path = './users.pkl'
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        print('No file or Empty file')
        return False
    try:
        with open(path, 'rb') as file:
            if pickle.load(file) == None:
                return False
            return True
    except Exception as e:
        print(f'Invalid .pkl file error: {e}')
        return False

def load_user_data():
    file_name = './users.pkl'
    with open(file_name, 'rb') as file:
        return pickle.load(file)

def save_user_data(user_data):
    print(user_data)
    file_name = './users.pkl'
    with open(file_name, 'wb') as file:
        pickle.dump(user_data, file)

def generate_user(data):
    user_input = data
    name = user_input['First name'] + ' '  + user_input['Last name']
    user = Menu(name, user_input['Kcal'])
    user.set_frutas(user_input['Fruit'])
    user.set_verduras(user_input['Vegetables'])
    user.set_cereales(user_input['Cereal'])
    user.set_leguminosas(user_input['Legume'])
    user.set_lacteos(user_input['Dairy'])
    user.set_grasas(user_input['Fat'])
    user.set_proteinas(user_input['Protein'])
    return user

"""
def get_input():
    check_name = True
    check_kcal = True
    while check_name:
        try:
            name = str(input('Type user name: '))
            if len(name) > 0 and len(name) < 100:
                check_name = False
        except ValueError:
            print('Error use letters to choose a user name.')
    
    while check_kcal:
        try:
            kcal = int(input('Type daily Kcal: '))
            check_kcal = False
        except ValueError:
            print('Error, use whole numbers.')
    return name, kcal

def set_user_values(user):
    check = True
    while check:
        try:
            amount = int(input(f'Type amount of fruits: '))
            user.set_frutas(amount)
            check = False
        except ValueError:
            print('Please type only whole numbers')

    check = True
    while check:
        try:
            amount = int(input(f'Type amount of vegetables: '))
            user.set_verduras(amount)
            check = False
        except ValueError:
            print('Please type only whole numbers')

    check = True
    while check:
        try:
            amount = int(input(f'Type amount of cerals: '))
            user.set_cereales(amount)
            check = False
        except ValueError:
            print('Please type only whole numbers')

    check = True
    while check:
        try:
            amount = int(input(f'Type amount of legumes: '))
            user.set_leguminosas(amount)
            check = False
        except ValueError:
            print('Please type only whole numbers')

    check = True
    while check:
        try:
            amount = int(input(f'Type amount of dairy: '))
            user.set_lacteos(amount)
            check = False
        except ValueError:
            print('Please type only whole numbers')

    check = True
    while check:
        try:
            amount = int(input(f'Type amount of fats: '))
            user.set_grasas(amount)
            check = False
        except ValueError:
            print('Please type only whole numbers')

    check = True
    while check:
        try:
            amount = int(input(f'Type amount of proteins: '))
            user.set_proteinas(amount)
            check = False
        except ValueError:
            print('Please type only whole numbers')
    return 
"""

