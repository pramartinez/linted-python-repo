'''
Implements a boilerplate clas
'''


class Foo:
    '''
    World famous Foo class by any other name
    '''

    def __init__(self, *args):
        self._args = args

    def args(self):
        '''
        getter function
        '''
        return self._args

    def first_arg(self):
        '''
        Possibly we're only interested in this
        '''
        return self._args[0]
