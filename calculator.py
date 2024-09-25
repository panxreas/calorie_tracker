class Meal_sets:
    def __init__(self, user_menu):

        # USER limit values
        self.fruit_limit = user_menu.get_frutas()
        self.vegetable_limit = user_menu.get_verduras()
        self.cereal_limit = user_menu.get_cereales()
        self.legume_limit = user_menu.get_leguminosas()
        self.dairy_limit = user_menu.get_lacteos()
        self.fat_limit = user_menu.get_grasas()
        self.protein_limit = user_menu.get_protinas()

        # Array containing all meal objects
        self.meal_sets = []

    # Method for adding meals 
    def add_meal():
        pass

    # Method for setting the current meal amount
    def calc_total():
        pass

class Meal:
    def __init__(self, food, name='Meal'):
        self.name = name
        self.food = food
        self.fruit = []
        self.vegetable = []
        self.cereal = []
        self.legume = []
        self.dairy = []
        self.fat = []
        self.protein = []

    def add_fruits():
        pass



