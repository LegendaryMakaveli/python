from unittest import TestCase
from decimal import Decimal
from bank_account import Bank


class TestBank(TestCase):
    def setUp(self):
        self.bank = Bank(
            first_name="Mary",
            last_name="Johnson",
            address="Lagos",
            email="mary@example.com",
            phone_number="08022345678",
            bvn="12345678901"
        )
    def test_account_initialization(self):
        self.assertEqual(self.bank.first_name, "Mary")
        self.assertEqual(self.bank.last_name, "Johnson")
        self.assertEqual(self.bank.bvn, "12345678901")
        self.assertTrue(self.bank.account_number.startswith("14"))
        self.assertEqual(len(self.bank.account_number), 10)
        self.assertEqual(self.bank.balance, Decimal("0.0"))

    def test_invalid_first_name_type_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank.first_name = 1234

    def test_empty_first_name_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank.first_name = ""

    def test_invalid_last_name_type_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank.last_name = None

    def test_invalid_bvn_with_letters_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank.bvn = "1234AB78901"

    def test_incomplete_bvn_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank.bvn = "12345"

    def test_valid_bvn_passes(self):
        self.bank.bvn = "12345678901"
        self.assertEqual(self.bank.bvn, "12345678901")


    def test_valid_nin_is_accepted(self):
        self.bank.NIN = "12345678901"
        self.assertEqual(self.bank.NIN, "12345678901")

    def test_nin_with_letters_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank.NIN = "12A45678901"

    def test_nin_incomplete_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank.NIN = "12345"

    def test_empty_nin_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank.NIN = ""

    def test_balance_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            self.bank.balance = Decimal(-100)

    def test_balance_cannot_exceed_limit(self):
        with self.assertRaises(ValueError):
            self.bank.balance = Decimal(600000)

    def test_balance_cannot_be_empty_string(self):
        with self.assertRaises(ValueError):
            self.bank.balance = ""

    def test_deposit_increases_balance(self):
        self.bank.deposit(Decimal(1000))
        self.assertEqual(self.bank.balance, Decimal(1000))

    def test_multiple_deposits_add_up(self):
        self.bank.deposit(Decimal(500))
        self.bank.deposit(Decimal(250))
        self.assertEqual(self.bank.balance, Decimal(750))

    def test_deposit_negative_amount_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank.deposit(Decimal(-100))

    def test_deposit_empty_string_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank.deposit("")

    def test_withdraw_reduces_balance(self):
        self.bank.deposit(Decimal(1000))
        self.bank.withdraw(Decimal(400))
        self.assertEqual(self.bank.balance, Decimal(600))

    def test_withdraw_more_than_balance_raises_error(self):
        self.bank.deposit(Decimal(200))
        with self.assertRaises(ValueError):
            self.bank.withdraw(Decimal(500))

    def test_withdraw_negative_amount_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank.withdraw(Decimal(-50))

    def test_withdraw_zero_does_not_change_balance(self):
        self.bank.deposit(Decimal(100))
        self.bank.withdraw(Decimal(0))
        self.assertEqual(self.bank.balance, Decimal(100))
