import json, os
from elements import *
from equivalencias import equivalencia

def check_user_data():
    path = './users.json'
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        print('No file or Empty file')
        return False
    try:
        with open(path, 'r') as file:
            data = json.load(path)
            return True
    except Exception as e:
        print(f'Invalid Json file error: {e}')
        return False

def get_input():
    check_name = True
    check_kcal = True
    while check_name:
        try:
            name = str(input('Type user name: '))
            if len(name) > 0 and len(name) < 100:
                check_name = False
        except TypeError:
            print('Error use letters to choose a user name.')
    while check_kcal:
        try:
            kcal = int(input('Type daily Kcal: '))
            check_kcal = False
        except TypeError:
            print('Error, use whole numbers.')
    return name, kcal

def set_user_values(user):
    check = True
    while check:
        try:
            amount = int(input(f'Type amount of fruits: '))
            user.set_frutas(amount)
            check = False
        except TypeError:
            print('Please type only whole numbers')

    check = True
    while check:
        try:
            amount = int(input(f'Type amount of vegetables: '))
            user.set_verduras(amount)
            check = False
        except TypeError:
            print('Please type only whole numbers')

    check = True
    while check:
        try:
            amount = int(input(f'Type amount of cerals: '))
            user.set_cereales(amount)
            check = False
        except TypeError:
            print('Please type only whole numbers')

    check = True
    while check:
        try:
            amount = int(input(f'Type amount of legumes: '))
            user.set_leguminosas(amount)
            check = False
        except TypeError:
            print('Please type only whole numbers')

    check = True
    while check:
        try:
            amount = int(input(f'Type amount of dairy: '))
            user.set_lacteos(amount)
            check = False
        except TypeError:
            print('Please type only whole numbers')

    check = True
    while check:
        try:
            amount = int(input(f'Type amount of fats: '))
            user.set_grasas(amount)
            check = False
        except TypeError:
            print('Please type only whole numbers')

    check = True
    while check:
        try:
            amount = int(input(f'Type amount of proteins: '))
            user.set_proteinas(amount)
            check = False
        except TypeError:
            print('Please type only whole numbers')
    return 

def create_user():
    user_input = get_input()
    user = Menu(user_input[0], user_input[1])
    set_user_values(user)

    print(user)
    user.get_data()
