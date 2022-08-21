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
        self.smoothies = [x for x in self.recipe_list if x[0] == "smoothie"]
        self.selected_smoothies = random.sample(self.smoothies, num)
        # TODO add option parameter
        if not self.filtered_list:
            self.tmp = [x for x in self.recipe_list if x[0] != "smoothie"]
        else:
            self.tmp = [x for x in self.filtered_list if x[0] != "smoothie"]
        self.tmp.extend(self.selected_smoothies)
        self.filtered_list = self.tmp
        for x in self.selected_smoothies:
            print(x[1])

    def random_selection_dinners(self, num):
        self.dinners = [x for x in self.recipe_list if x[0] == "dinner"]
        self.selected_dinners = random.sample(self.dinners, num)
        # TODO add option parameter
        if not self.filtered_list:
            self.tmp = [x for x in self.recipe_list if x[0] != "dinner"]
        else:
            self.tmp = [x for x in self.filtered_list if x[0] != "dinner"]
        self.tmp.extend(self.selected_dinners)
        self.filtered_list = self.tmp
        for x in self.selected_dinners:
            print(x[1])

    def specific_selection_any(self, *args):
        for x in self.recipe_list:
            if x[1] in args:
                self.filtered_list.append(x)

    def generate_shopping_list(self):
        self.aggregated_list = {}
        if not self.filtered_list:
            for x in self.recipe_list:
                for a,b in x[2].items():
                    if a not in self.aggregated_list:
                        self.aggregated_list[a] = b
                    else:
                        self.aggregated_list[a] += b
        else:
            for x in self.filtered_list:
                for a,b in x[2].items():
                    if a not in self.aggregated_list:
                        self.aggregated_list[a] = b
                    else:
                        self.aggregated_list[a] += b
                    
        return self.aggregated_list
