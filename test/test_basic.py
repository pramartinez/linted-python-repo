'''
Very basic module to test infrastructure
'''
from unittest import TestCase
from fuu import ShoppingList

ITEM1 = "bread"
ITEM2 = "water"
ITEM3 = "cheese"

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
        assert ShoppingList(ITEM1, ITEM2, ITEM3).args() == (ITEM1, ITEM2, ITEM3,)
        assert ShoppingList(ITEM1, ITEM2, ITEM3).first_arg() == ITEM1
        assert ShoppingList(ITEM1, ITEM2, ITEM3).list_length() == 3
