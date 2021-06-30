'''
Implements a boilerplate clas
'''


class ShoppingList:
    def __init__(self, *args):
        self.items = args
        self.nitems = len(args)

    def args(self):
        return self.items

    def first_arg(self):
        return self.items[0]
