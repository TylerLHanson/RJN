import random

class RecJet:
    def __init__(self):
        print('initialization is happening')
        self.recipesdict = {}

    def add_item(self, itemname, itemlink):
        self.recipesdict[itemname] = itemlink

myinst = RecJet()
myinst.add_item(
    itemname = 'tropical almond shake',
    itemlink = 'https://b-m.facebook.com/PTSquaredLLC/photos/a.601421479929449/5439076966163852/?type=3&source=48',
)

print(myinst.recipesdict)
