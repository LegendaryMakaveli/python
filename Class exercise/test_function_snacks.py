from unittest import TestCase
import function_snacks
import math

class TestFunctionSnacks(TestCase) :
	def test_that_the_divide_or_square_exist(makaveli) :
		function_snacks.divide_or_square(5)

	def test_that_no_float_number_in_argument(makaveli) :
		makaveli.assertRaises(ValueError, function_snacks.divide_or_square, float)

	def test_that_the_sum_return_float(makaveli) :
		result = function_snacks.divide_or_square(10)
		makaveli.assertEqual(result, 3.16)

	def test_that_nagative_number_is_in_input(makaveli) :
		makaveli.assertRaises(ValueError, function_snacks.divide_or_square, -1)
		makaveli.assertRaises(ValueError, function_snacks.divide_or_square, " ")

	def test_that_no_char_in_input(makaveli) :
		makaveli.assertRaises(ValueError, function_snacks.divide_or_square,  'h')


class TestFutureInvestmentFunction(TestCase) :
	def test_that_calculate_investment_dey_first(makaveli) :
		function_snacks.calculate_investment(100, 0.5, 1999)

	def test_that_no_nagative_input(makaveli) :
		makaveli.assertRaises(ValueError, function_snacks.calculate_investment, -1, -1, -1)	

	def test_that_no_letters_in_the_input(makaveli) :
		makaveli.assertRaises(ValueError, function_snacks.calculate_investment, 'a', 'b', 'c')
		makaveli.assertRaises(ValueError, function_snacks.calculate_investment, " ", " ", "")

	def test_for_minimum_digit_in_input(makaveli) :
		makaveli.assertRaises(ValueError, function_snacks.calculate_investment, 1, 1, 2024)
	
	def test_for_maximum_digit_in_input(makaveli) :
		makaveli.assertRaises(ValueError, function_snacks.calculate_investment, 2_000_000.000, 13, 3200)		


class TestOnlyFloatFunction(TestCase) :
	def test_that_the_function_dey_first(makaveli) :
		function_snacks.only_float(5.5, 4.4)

	def test_that_the_function_do_not_accept_whole_number(makaveli) :
		makaveli.assertRaises(ValueError, function_snacks.only_float, int, int )

	def test_for_string_in_input(makaveli) :
		makaveli.assertRaises(ValueError, function_snacks.only_float, " ", " ")

	def test_for_no_nagative_input(makaveli) :
		makaveli.assertRaises(ValueError, function_snacks.only_float, -1, -1)

	def test_for_no_char_in_input(makaveli) :
		makaveli.assertRaises(ValueError, function_snacks.only_float, ' ', ' ')
	
	def test_for_minimun_input(makaveli) :
		makaveli.assertRaises(ValueError, function_snacks.only_float, 500.0, 500.0)





















