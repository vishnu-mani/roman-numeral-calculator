import unittest
from roman_numeral_calculator import roman_numeral_calculator

class TestRomanCalculator(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(roman_numeral_calculator('IX', 'L', '+'), 'LIX')
		self.assertEqual(roman_numeral_calculator('iii', 'v', '+'), 'VIII')

	def test_subtraction(self):
		self.assertEqual(roman_numeral_calculator('CX', 'L', '-'), 'LX')
		self.assertEqual(roman_numeral_calculator('L', 'L', '-'), 0)
		self.assertEqual(roman_numeral_calculator('L', 'M', '-'), 0)

	def test_multiplication(self):
		self.assertEqual(roman_numeral_calculator('X', 'L', '*'), 'D')
		self.assertEqual(roman_numeral_calculator('M', 'V', '*'), 'MMMMM')

	def test_division(self):
		self.assertEqual(roman_numeral_calculator('L', 'X', '/'), 'V')
		self.assertEqual(roman_numeral_calculator('X', 'L', '/'), 0)
		self.assertEqual(roman_numeral_calculator('X', 'X', '/'), 'I')

	def test_value_error(self):
		self.assertRaises(ValueError, roman_numeral_calculator,'F', 'X', '+')
	
	def test_type_error(self):
		self.assertRaises(TypeError, roman_numeral_calculator, 'D', 'X', '&')
