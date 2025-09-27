from unittest import TestCase

from phone_book import PhoneBook


class TestPhoneBookMethods(TestCase):
    def setUp(self):
        self.phonebook = PhoneBook()

    def test_that_method_that_add_contact(self):
      self.assertEqual(len(self.phonebook.contact), 0)
      self.phonebook.add_contact("Adeyemo", "09211221122")
      self.assertEqual(len(self.phonebook.contact), 1)
      self.assertEqual(self.phonebook.contact[0], {"name": "Adeyemo", "contact": "09211221122"})

    def test_the_method_that_search_contact(self):
        self.phonebook.add_contact("Adeyemo", "09211221122")
        self.assertEqual("Adeyemo, 09211221122", self.phonebook.search("Adeyemo"))