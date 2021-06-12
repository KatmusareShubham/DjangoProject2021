from django.test import TestCase

from app.calc import add,substract

class CalcTest(TestCase):

    def test_addition(self):
        """test for the addition of two numbers"""
        self.assertEqual(add(3,8),11)
    
    def test_substract(self):
        """ subtraction of two numbers"""
        self.assertEqual(substract(5,11),-6)


