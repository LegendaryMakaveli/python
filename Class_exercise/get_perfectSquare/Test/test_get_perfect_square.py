from unittest import TestCase

from source_code import get_perfect_square


class TestTheFunctionThatCalculatePerfectSquare(TestCase) :
    def test_that_the_function_exist(self) :
        get_perfect_square.get_perfect_squares([3, 34, 4])

    def test_that_the_function_only_accept_list(self):
        self.assertRaises(ValueError, get_perfect_square.get_perfect_squares, 3)

    def test_that_the_list_dont_dont_have_invalid_input_like_float(self):
        self.assertRaises(ValueError, get_perfect_square.get_perfect_squares, [3.5,4,3,2])

    def test_that_the_list_dont_accept_string_input(self):
        self.assertRaises(ValueError, get_perfect_square.get_perfect_squares, ["come",4,3,2])

    def test_that_the_function_sort_out_the_only_perfect_square(self):
        result = get_perfect_square.get_perfect_squares([2,3,4,9,6,25])
        self.assertEqual(result, [False,False,True,True,False,True])

    def test_confirm_the_function_functionality(self):
        result = get_perfect_square.get_perfect_squares([2,3,4,9,6,25])
        self.assertNotEqual(result, [True,False,True,True,False,True])