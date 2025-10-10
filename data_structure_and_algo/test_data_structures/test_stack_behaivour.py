from unittest import TestCase
from data_structures.stack_behaviour import StackStructure

class TestStackStructure(TestCase):

    def test_stack_is_empty_on_creation(self):
        stack = StackStructure(3)
        self.assertTrue(stack.is_empty())

    def test_add_one_element_stack_is_not_empty(self):
        stack = StackStructure(3)
        stack.push_element(5)
        self.assertFalse(stack.is_empty())

    def test_add_one_element_and_remove_it_stack_is_empty(self):
        stack = StackStructure(3)
        stack.push_element(5)
        stack.pop_element()
        self.assertTrue(stack.is_empty())

    def test_add_two_elements_stack_is_not_empty(self):
        stack = StackStructure(3)
        stack.push_element(5)
        stack.push_element(10)
        self.assertFalse(stack.is_empty())

    def test_remove_two_elements_stack_is_empty(self):
        stack = StackStructure(3)
        stack.push_element(5)
        stack.push_element(10)
        self.assertFalse(stack.is_empty())
        stack.pop_element()
        stack.pop_element()
        self.assertTrue(stack.is_empty())

    def test_add_two_elements_remove_one_stack_is_not_empty(self):
        stack = StackStructure(3)
        stack.push_element(5)
        stack.push_element(10)
        self.assertFalse(stack.is_empty())
        stack.pop_element()
        self.assertFalse(stack.is_empty())

    def test_peek_returns_top_element_without_removing(self):
        stack = StackStructure(3)
        stack.push_element(5)
        stack.push_element(10)
        self.assertEqual(stack.peek(), 10)
        self.assertEqual(stack.size(), 2)  # peek should not change size

    def test_size_returns_correct_number_of_elements(self):
        stack = StackStructure(3)
        self.assertEqual(stack.size(), 0)
        stack.push_element(5)
        self.assertEqual(stack.size(), 1)
        stack.push_element(10)
        self.assertEqual(stack.size(), 2)
        stack.pop_element()
        self.assertEqual(stack.size(), 1)