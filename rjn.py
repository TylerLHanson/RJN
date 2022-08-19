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

    def insert_snack(self, name):
        self.recipe_list.append((name, name, {name: 1.0}))

    def show_recipe_names(self):
        for x in self.recipe_list:
            if x[0] == "dinner" or x[0] == "smoothie":
                print(x[0], x[1])

    def show_all_names(self):
        for x in self.recipe_list:
            print(x[1])

    def random_selection_smoothies(self, num):
        self.filtered_smoothies = [x for x in self.recipe_list if x[0] == "smoothie"]
        self.filtered_smoothies = random.sample(self.filtered_smoothies, num)
        # TODO add option parameter
        self.filtered_list.extend(self.filtered_smoothies)
        for x in self.filtered_smoothies:
            print(x[1])

    def random_selection_dinners(self, num):
        self.filtered_dinners = [x for x in self.recipe_list if x[0] == "dinner"]
        self.filtered_dinners = random.sample(self.filtered_dinners, num)
        # TODO add option parameter
        self.filtered_list.extend(self.filtered_dinners)
        for x in self.filtered_dinners:
            print(x[1])

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
