from unittest import TestCase
from my_array import Array


class TestMyOwnCustomizedArray(TestCase):

        def test_valid_initialization(self):
            myArray = Array(int, 3)
            self.assertEqual(len(myArray), 3)
            self.assertEqual(myArray.data_type, int)
            self.assertTrue(hasattr(myArray.array, "__setitem__"))

        def test_invalid_size(self):
            self.assertRaises(ValueError, Array, int, 0)
            self.assertRaises(ValueError, Array, int, -5)

        def test_invalid_data_type(self):
            self.assertRaises(TypeError, Array, list, 5)

        def test_set_and_get_array(self):
            myArray = Array(int, 3)
            myArray.set_array(0, 10)
            self.assertEqual(myArray.get_array(0), 10)

        def test_set_array_invalid_index(self):
            myArray = Array(int, 3)
            self.assertRaises(IndexError, myArray.set_array, 5, 100)


        def test_int_array(self):
            myArray = Array(int, 2)
            myArray.set_int_array(0, 5)
            self.assertEqual(myArray.get_int_array(0), 5)

        def test_float_array(self):
            myArray = Array(float, 2)
            myArray.set_float_array(0, 2.5)
            self.assertEqual(myArray.get_float_array(0), 2.5)

        def test_bool_array(self):
            myArray = Array(bool, 2)
            myArray.set_bool_array(0, True)
            self.assertEqual(myArray.get_bool_array(0), True)

        def test_string_array(self):
            myArray = Array(str, 2)
            myArray.set_string_array(0, "Hello")
            self.assertEqual(myArray.get_string_array(0), "Hello")

        def test_wrong_type_assignment(self):
            myArray = Array(int, 3)
            self.assertRaises(TypeError, myArray.set_int_array, 0, "not int")

        def test_setitem_and_getitem(self):
            myArray = Array(int, 3)
            myArray[0] = 99
            myArray[1] = 42
            self.assertEqual(myArray[0], 99)
            self.assertEqual(myArray[1], 42)


        def test_get_length_and_len(self):
            myArray = Array(str, 4)
            self.assertEqual(myArray.get_length(), 4)
            self.assertEqual(len(myArray), 4)




