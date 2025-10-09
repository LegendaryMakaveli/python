from unittest import TestCase
from data_structures.set_behaviour import SetBehaviour


class TestSetBehaviour(TestCase):

    def test_that_set_is_empty_on_creation(self):
        my_set = SetBehaviour()
        self.assertTrue(my_set.is_empty())

    def test_that_one_element_is_added_and_cannot_duplicate(self):
        my_set = SetBehaviour()
        my_set.add_element(5)
        my_set.add_element(5)
        self.assertEqual(1, my_set.size)

    def test_that_add_many_elements_at_once_in_set_and_no_duplicate(self):
        my_set = SetBehaviour()
        my_set.add_many_elements([1, 2, 3, 4])
        self.assertEqual(4, my_set.size)

    def test_that_remove_all_the_elements_in_a_set(self):
        my_set = SetBehaviour()
        my_set.add_many_elements([1, 2, 3, 4])
        my_set.clear_element()
        self.assertTrue(my_set.is_empty())

    def test_the_method_that_search_for_an_element_in_a_set(self):
        my_set = SetBehaviour()
        my_set.add_many_elements([1, 2, 3, 4])
        self.assertTrue(my_set.search_element(3))
        self.assertFalse(my_set.search_element(5))

    def test_that_set_contains_all_elements(self):
        my_set = SetBehaviour()
        my_set.add_many_elements([1, 2, 3, 4])
        self.assertTrue(my_set.search_all([1, 2, 3, 4]))
        self.assertFalse(my_set.search_all([1, 2, 5]))

    def test_that_remove_element_by_value(self):
        my_set = SetBehaviour()
        my_set.add_many_elements([1, 2, 3, 4])
        my_set.remove_element_by_value(3)
        self.assertFalse(my_set.search_element(3))
        self.assertEqual(3, my_set.size)

    def test_that_return_the_size_of_a_set(self):
        my_set = SetBehaviour()
        my_set.add_many_elements([1, 2, 3, 4])
        self.assertEqual(4, my_set.size)
