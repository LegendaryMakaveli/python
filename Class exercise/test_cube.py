import unittest
import cube

class TestCubeFunction(unittest.TestCase) :
	def test_that_cube_function_exists(self) :
		cube.get_cube(3)

	def test_that_cube_function(self) :
		result = cube.get_cube(3)
		self.assertEqual(result, 27)
		result = cube.get_cube(5)
		self.assertEqual(result, 125)

	def test_that_cube_functions_validate_incorrect_input (self) :
		self.assertRaises(ValueError, cube.get_cube, "Ikka")

	def test_that_cube_function_return_correct_result_with_decimal(self) :
		result = cube.get_cube(7.5)
		self.assertEqaul(result, 421.875)