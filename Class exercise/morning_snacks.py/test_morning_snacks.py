from unittest import TestCase
import morning_snacks


class TestForTheSquareOfEachNumber(TestCase) :
	def test_that_the_function_exist(makaveli) :
		morning_snacks.square_of_a_list(2)

	def test_for_zero_input(makaveli) :
		makaveli.assertRaises(ValueError, morning_snacks.square_of_a_list, 0)

	def test_for_strings_input(makaveli) :
		makaveli.assertRaises(ValueError, morning_snacks.square_of_a_list, "ikka")

	def test_for_the_function_result(makaveli) :
		result = (morning_snacks.square_of_a_list, [1,2,3,4,5])
		makaveli.assertNotEqual(result, [1,4,9,16,25])


class TestForTheLengthOfAList(TestCase) :
	def test_that_the_function_exist(makaveli) :
		morning_snacks.length_of_a_list([2,3,4,1,4,5,6,7])

	def test_for_zero_input(makaveli) :
		makaveli.assertRaises(ValueError, morning_snacks.length_of_a_list, [0,0,0,0,0])


class TestForTheListOfAllEvenNumber(TestCase) :
	def test_that_the_function_exist(makaveli) :
		morning_snacks.is_even([2,4,6,8])

	def test_for_zero_input(makaveli) :
		makaveli.assertRaises(ValueError, morning_snacks.is_even, 0)
	
	def test_for_string_input(makaveli) :
		makaveli.assertRaises(TypeError, morning_snacks.is_even, " ")

class TestForTheTheHighestCharacter(TestCase) :
	def test_the_function_exist(makaveli) :
		morning_snacks.length_of_character([2,3,4])

	def test_for_int_input(makaveli) :
		makaveli.assertRaises(TypeError, morning_snacks.length_of_character,  7)
		makaveli.assertRaises(TypeError, morning_snacks.length_of_character,  0)
		makaveli.assertRaises(TypeError, morning_snacks.length_of_character,  -1)

	def test_for_float_input(makaveli) :
		makaveli.assertRaises(TypeError, morning_snacks.length_of_character,  79.89)






