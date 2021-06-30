'''
Very basic module to test infrastructure
'''
from unittest import TestCase
from fuu import ShoppingList

ITEMS = ("bread", "water", "cheese")

class BasicTest(TestCase):
    '''
    Tests the basic object creation functionality
    '''

    def setUp(self) -> None:
        self.to_test = ShoppingList()

    def test_different_args(self):
        '''
        tests if it gets whatever is used to initialize
        '''
        assert self.to_test.args() == ()
        assert ShoppingList(ITEMS).args() == (ITEMS,)
        assert ShoppingList(ITEMS).first_arg() == ITEMS[0]
