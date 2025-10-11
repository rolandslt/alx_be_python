import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1,1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 1), 2)
        self.assertEqual(self.calc.multiply(2, 5), 10)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(6,2), 3)
        self.assertEqual(self.calc.divide(10, 2), 5)
if  __name__ == "__main__":
    unittest.main()