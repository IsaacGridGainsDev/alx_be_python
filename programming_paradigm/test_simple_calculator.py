import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
	def setUp(self):
		"""Set up the SimpleCalculator instance before each test"""
		self.calc = SimpleCalculator()
	
	def test_addition(self):
		"""Test the addition method."""
		self.assertEqual(self.calc.add(2,3), 5)
#		 self.assertEqual(self.calc.add(2,3), 5)
		self.assertEqual(self.calc.add(-1,1), 0)
		self.assertEqual(self.calc.add(3,-5), -2)
		self.assertEqual(self.calc.add(-1,-3), -4)
	
	def test_subtraction(self):
		"""Test the subtraction method."""
		self.assertEqual(self.calc.subtract(2,3), -1)
		self.assertEqual(self.calc.subtract(-1,1), -2)
#		 self.assertEqual(self.calc.subtract(-1,1), -2)
		self.assertEqual(self.calc.subtract(3,-5), 8)
		self.assertEqual(self.calc.subtract(-1,-3), 2)
	
	def test_multiplication(self):
		"""Test the multiplication method."""
		self.assertEqual(self.calc.multiply(2,3), 6)
#		 self.assertEqual(self.calc.multiply(2,3), 6)
		self.assertEqual(self.calc.multiply(-1,1), -1)
		self.assertEqual(self.calc.multiply(3,-5), -15)
		self.assertEqual(self.calc.multiply(-1,-3), 3)
	
	def test_division(self):
		"""Test the division method."""
		self.assertEqual(self.calc.divide(6,3), 2.0)
#		 self.assertEqual(self.calc.divide(6,3), 2.0)
		self.assertEqual(self.calc.divide(-1,1), -1.0)
		self.assertEqual(self.calc.divide(15,0), None)
		self.assertEqual(self.calc.divide(-9,-3), 3.0)


