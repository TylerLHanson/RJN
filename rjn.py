import random

class RecJet:

    def __init__(self):
        self.recipe_list = []
        self.filtered_list = []

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
        for x in self.recipe_list:
            if x[0] == "dinner" or x[0] == "smoothie":
                print(x[0], x[1])

    def show_all_names(self):
        pass

    def random_selection_shakes(self, num):
        pass

    def random_selection_dinners(self, num):
        pass

    def specific_selection_any(self):
        pass

    def generate_shopping_list(self):
        self.aggregated_list = {}
        for x in self.recipe_list:
            for a,b in x[2].items():
                if a not in self.aggregated_list:
                    self.aggregated_list[a] = b
                else:
                    self.aggregated_list[a] += b
                    
        return self.aggregated_list
