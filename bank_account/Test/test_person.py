from unittest import TestCase
from person import Person

class TestBankAccountRegistration(TestCase):

    def test_valid_person_creation(self):
        self.person = Person(
            name="John Doe",
            address="123 Main St",
            email="john@gmail.com",
            phone_number="08022345678"
        )
        self.assertEqual(self.person.name, "John Doe")
        self.assertEqual(self.person.address, "123 Main St")
        self.assertEqual(self.person.email, "john@gmail.com")
        self.assertEqual(self.person.phone_number, "08022345678")

    def test_name_must_be_string(self):
        with self.assertRaises(TypeError):
            Person(123, "123 Main St", "john@gmail.com", "08022345678")

    def test_name_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            Person("", "123 Main St", "john@gmail.com", "08022345678")

    def test_address_must_be_string(self):
        with self.assertRaises(ValueError):
            Person("John Doe", 12345, "john@gmail.com", "08022345678")

    def test_address_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            Person("John Doe", "", "john@gmail.com", "08022345678")

    def test_email_must_be_string(self):
        with self.assertRaises(ValueError):
            Person("John Doe", "123 Main St", 123, "08022345678")

    def test_email_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            Person("John Doe", "123 Main St", "", "08022345678")

    def test_invalid_email_format(self):
        self.assertRaises(ValueError, Person, "John Doe", "123 Main St", "john_at_gmail.com", "08022345678")

    def test_valid_email_format(self):
        self.person = Person("John Doe", "123 Main St", "john@gmail.com", "08022345678")
        self.assertEqual("john@gmail.com", self.person.email)

    def test_phone_must_be_string(self):
        with self.assertRaises(ValueError):
            Person("John Doe", "123 Main St", "john@gmail.com", 1234567890)

    def test_phone_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            Person("John Doe", "123 Main St", "john@gmail.com", "")

    def test_invalid_phone_format(self):
        with self.assertRaises(ValueError):
            Person("John Doe", "123 Main St", "john@gmail.com", "12abc")

