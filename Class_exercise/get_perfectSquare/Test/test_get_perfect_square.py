from unittest import TestCase

from source_code import get_perfect_square


class TestTheFunctionThatCalculatePerfectSquare(TestCase) :
    def test_that_the_function_exist(self) :
        get_perfect_square.get_perfect_squares([3,34,4])