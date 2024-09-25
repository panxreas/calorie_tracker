from equivalencias import equivalencia

class Alimentos:
    def __init__(self, equivalencia):
        self.frutas = equivalencia['FRUTAS']
        self.verduras = equivalencia['VERDURAS']
        self.cereales = equivalencia['CEREALES']
        self.leguminosas = equivalencia['LEGUMINOSAS']
        self.lacteos = equivalencia['LACTEOS']
        self.grasas = equivalencia['GRASAS']
        self.proteinas = equivalencia['PROTEINAS']

    def get_frutas(self):
        return self.frutas
    def get_verduras(self):
        return self.verduras
    def get_cereales(self):
        return self.cereales
    def get_leguminosas(self):
        return self.leguminosas
    def get_lacteos(self):
        return self.lacteos
    def get_grasas(self):
        return self.grasas
    def get_proteinas(self):
        return self.proteinas

class Menu:
    def __init__(self, name, kcal):
        self.name = name
        self.kcal = kcal
        self.frutas = None
        self.verduras = None
        self.cereales = None
        self.leguminosas = None
        self.lacteos = None
        self.grasas = None
        self.proteinas = None

    def __repr__(self):
        return f'------------------------------\n| Menu for {self.name} \n------------------------------\n| Daily calories: {self.kcal}\n------------------------------'

    def get_name(self):
        return self.name
    def get_kcal(self):
        return self.kcal

    def set_frutas(self, amount):
        self.frutas = amount
    def set_verduras(self, amount):
        self.verduras = amount
    def set_cereales(self, amount):
        self.cereales = amount
    def set_leguminosas(self, amount):
        self.leguminosas = amount
    def set_lacteos(self, amount):
        self.lacteos = amount
    def set_grasas(self, amount):
        self.grasas = amount
    def set_proteinas(self, amount):
        self.proteinas = amount

    def get_data(self):
        for groups in equivalencia.keys():
            alimento = groups.lower()
            if alimento == 'frutas':
                amount = self.frutas
            elif alimento == 'verduras':
                amount = self.verduras
            elif alimento == 'cereales':
                amount = self.cereales
            elif alimento == 'leguminosas':
                amount = self.leguminosas
            elif alimento == 'lacteos':
                amount = self.lacteos
            elif alimento == 'grasas':
                amount == self.grasas
            elif alimento == 'proteinas':
                amount == self.proteinas

            print('------------------------------')
            print(f'| Cantidad de {alimento}: {amount} ')
        print('-----------------------------')




