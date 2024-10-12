class Meal_sets:
    def __init__(self, user_menu):

        # USER limit values
        self.fruit_limit = user_menu.get_frutas()
        self.vegetable_limit = user_menu.get_verduras()
        self.cereal_limit = user_menu.get_cereales()
        self.legume_limit = user_menu.get_leguminosas()
        self.dairy_limit = user_menu.get_lacteos()
        self.fat_limit = user_menu.get_grasas()
        self.protein_limit = user_menu.get_proteinas()

        # Array containing all meal objects
        self.meal_sets = []

    # Method for adding meals 
    def add_meal(self, meal):
        self.meal_sets.append(meal)

    # Method for setting the current meal amount
    def calc_total():
        pass

    def __repr__(self):
        return f'This meal has {self.meal_sets}'

class Meal:
    def __init__(self, name='Meal'):
        self.name = name
        self.food = {}

    def get_food(self):
        return self.food

    def add_food(self, key_food_group, value_food_and_amount):
        if key_food_group not in self.food:
            self.food[key_food_group] = [value_food_and_amount]
        else:
            self.food[key_food_group].append(value_food_and_amount)

    def del_food(self, key_food_group, value_food_and_amount):
        self.food[key_food_group].remove(value_food_and_amount)
        if self.food[key_food_group] == []:
            del self.food[key_food_group]

    def set_name(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name} has {self.food}'
