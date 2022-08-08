import random

class RecJet:

    def __init__(self):
        self.recipe_list = []

    def insert_single_recipe(self, category, name, ingredients):
        # needs errors and exception handling
        self.newrecipe = (category, name, ingredients)
        self.recipe_list.append(self.newrecipe)

    def insert_multiple_recipes(self, recipes):
        # needs errors and exception handling
        self.recipe_list.extend(recipes)

    def insert_snack(self):
        pass

    def show_recipe_names(self):
        pass

    def show_all_names(self):
        pass

    def random_selection_shakes(self, num):
        pass

    def random_selection_dinners(self, num):
        pass

    def specific_selection_any(self):
        pass

    def generate_shopping_list(self):
        pass
