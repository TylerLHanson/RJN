from rjn import RecJet

my_rjn = RecJet()
my_rjn.insert_single_recipe('smoothie', 'tropical almond smoothie', {
        'banana': 1.0,
        'cup frozen pineapple': 0.5,
        'cup frozen mango': 0.5,
        'tbsp. almond butter': 1.0,
        'cup coconut milk': 2.0,
    })


my_rjn.insert_multiple_recipes(  [('smoothie',
    'pinch of yum green smoothie',
    {
        'cup frozen mango': 1.0,
        'cup frozen peaches': 0.5,
        'cup chopped kale': 0.25,
        'cup almond milk': 1.0,
        'tsp. ground ginger': 1.0,
        'tsp. honey': 1.0,
    }),
    ('dinner',
    'steak salad',
    {
        'steak': 1.0,
        'oz. spinach': 2.5,
        'cup salad dressing': 0.25,
    }),])

for i in my_rjn.recipe_list:
    print(i[2])

