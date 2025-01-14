import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
 
  def setUp(self):
    self.calculator = Calculator()
 
  def test_calc_sum(self):
    self.assertEqual(self.calculator.calc_sum(4,7), 11)

  def test_calc_subtract(self):
    self.assertEqual(self.calculator.calc_subtract(10,5), 5)

  def test_calc_multiply(self):
    self.assertEqual(self.calculator.calc_multiply(3,7), 21)

  def test_calc_divide(self):
    self.assertEqual(self.calculator.calc_divide(10,2), 5)

if __name__ == "__main__":
  unittest.main()
