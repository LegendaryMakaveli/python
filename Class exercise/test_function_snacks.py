from unittest import TestCase
import function_snacks
import math

class TestFunctionSnacks(TestCase) :
	def test_that_the_divide_or_square_exist(self) :
		function_snacks.divide_or_square(5)

	def test_that_no_string_exist(self) :
		self.assertRaises(ValueError, function_snacks.divide_or_square, " ")
	def test_that_no_float_number_in_argument(self) :
		self.assertRaises(ValueError, function_snacks.divide_or_square, 278.9088)

	def test_that_the_sum_return_float(self) :
		result = function_snacks.divide_or_square(10)
		self.assertEqual(result, 3.16)