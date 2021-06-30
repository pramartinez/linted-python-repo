'''
Very basic module to test infrastructure
'''
from unittest import TestCase
from fuu import Foo

BAR = "bar"


class BasicTest(TestCase):
    '''
    Tests the basic object creation functionality
    '''

    def setUp(self) -> None:
        self.to_test = Foo()

    def test_different_args(self):
        '''
        tests if it gets whatever is used to initialize
        '''
        assert self.to_test.args() == ()
        assert Foo(BAR).args() == (BAR,)
        assert Foo(BAR).first_arg() == BAR
