from unittest import TestCase
from array_list_behaviour import ArrayList


class TestArrayListBehaviour(TestCase):
    def test_that_my_array_list_is_empty(self):
        self.array_list = ArrayList(int, 3)
        self.assertTrue(self.array_list.get_isEmpty)

    def test_that_element_can_be_added_into_my_list_and_isEmpty_is_false(self):
        self.array_list = ArrayList(int,3)
        self.array_list.add_element(1)

        self.assertEqual([1,None,None], self.array_list.get_element())
        self.assertFalse(self.array_list.get_isEmpty)

    def test_that_remove_element_from_my_list_and_list_isEmpty(self):
        self.array_list = ArrayList(int,3)
        self.array_list.add_element(1)
        self.array_list.add_element(2)
        self.array_list.add_element(3)

        self.array_list.remove_element()
        self.assertTrue(self.array_list.get_isEmpty)

    def test_that_remove_element_from_my_list_by_index_and_shift_the_remaining_element_list_empty_is_false(self):
        self.array_list = ArrayList(int,3)
        self.array_list.add_element(1)
        self.array_list.add_element(2)
        self.array_list.add_element(3)

        self.array_list.remove_element_by_index(1,2)

        self.assertEqual(1, self.array_list.get_element_by_index(0))
        self.assertEqual(3, self.array_list.get_element_by_index(1))


    def test_that_add_element_by_index_and_list_is_not_empty(self):
        self.array_list = ArrayList(int,4)
        self.array_list.add_element_by_index(0,45)
        self.array_list.add_element_by_index(1,20)
        self.array_list.add_element_by_index(2,22)
        self.array_list.add_element_by_index(0,10)

        self.assertEqual(10, self.array_list.get_element_by_index(0))
        self.assertEqual(45, self.array_list.get_element_by_index(1))
        self.assertEqual(20, self.array_list.get_element_by_index(2))
        self.assertEqual(22, self.array_list.get_element_by_index(3))


    def test_method_that_search_for_an_element_in_list(self):
        self.array_list = ArrayList(int, 3)
        self.array_list.add_element(1)
        self.array_list.add_element(2)
        self.array_list.add_element(3)

        self.assertTrue(self.array_list.search_element(3))
        self.assertTrue(self.array_list.search_element(2))
        self.assertTrue(self.array_list.search_element(1))


    def test_method_that_search_for_all_the_elements_in_list(self):
        self.array_list = ArrayList(int, 3)
        self.array_list.add_element(1)
        self.array_list.add_element(2)
        self.array_list.add_element(3)

        other_list = ArrayList(int, 3)
        other_list.add_element(1)
        other_list.add_element(2)
        other_list.add_element(3)

        self.assertTrue(self.array_list.search_all_element(other_list))


    def test_the_method_that_return_the_index_of_element(self):
        self.array_list = ArrayList(int,3)
        self.array_list.add_element(1)
        self.array_list.add_element(2)
        self.array_list.add_element(3)

        self.assertEqual(0,self.array_list.get_index(1))
        self.assertEqual(0,self.array_list.get_index(1))
        self.assertEqual(0,self.array_list.get_index(1))


    def test_the_method_that_return_the_size_of_my_list(self):
        self.array_list = ArrayList(int,3)
        self.array_list.add_element(1)
        self.array_list.add_element(2)
        self.array_list.add_element(3)

        self.assertEqual(3, self.array_list.get_size())

    def test_that_sort_elements_in_the_list(self):
        self.array_list = ArrayList(int, 4)
        self.array_list.add_element(50)
        self.array_list.add_element(10)
        self.array_list.add_element(30)
        self.array_list.add_element(20)

        self.array_list.sort_my_list()

        self.assertEqual(10, self.array_list.get_element_by_index(0))
        self.assertEqual(20, self.array_list.get_element_by_index(1))
        self.assertEqual(30, self.array_list.get_element_by_index(2))
        self.assertEqual(50, self.array_list.get_element_by_index(3))


    def test_that_my_list_can_expand_its_size(self):
        self.array_list = ArrayList(int, 3)
        for element in range(20) :
            self.array_list.add_element(element)

        self.assertEqual(20, self.array_list.get_size())
        self.assertEqual(10, self.array_list.get_element_by_index(10))

