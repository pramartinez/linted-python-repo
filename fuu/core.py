'''
Implements a boilerplate class
'''


class ShoppingList:
    '''
    ShoppingList class. It saves a list of items and how many there are
    '''
    def __init__(self, *args):
        self.items = args
        self.nitems = len(args)

    def args(self):
        '''
        Getter. It returns the list of items
        '''
        return self.items

    def first_arg(self):
        '''
        First elements of the shopping list
        '''
        return self.items[0]
