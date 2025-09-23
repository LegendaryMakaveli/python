from unittest import TestCase

from access_bank_account import AccessBank


class TestAccessBankAccountFunctions(TestCase):
    def setUp(self):
        self.my_bank = AccessBank("Makaveli", "Abc123!@#", "08034322112", 23)

    def test_that_name_is_set_and_get(self) :
        self.assertEqual("Makaveli", self.my_bank.get_name())

    def test_that_phone_is_set_and_get(self) :
        self.assertEqual("08034322112", self.my_bank.get_phone())

    def test_that_age_is_set_and_get(self) :
        self.assertEqual(23, self.my_bank.get_age())

    def test_password_is_set_and_get(self) :
        self.assertEqual("Abc123!@#", self.my_bank.get_password())

class TestAccessBankAccountFunctionsDontAcceptInvalidInput(TestCase):
    def setUp(self):
        self.my_bank = AccessBank("Makaveli", "Abc123!@#", "08034322112", 23)
    def test_that_set_name_dont_accept_invalid_inputs(self):
        self.assertRaises(ValueError,self.my_bank.set_name, 90)
        self.assertRaises(ValueError,self.my_bank.set_name, 7.8)
        self.assertRaises(ValueError,self.my_bank.set_name, "")

    def test_that_password_length_condition_is_met_and_invalid_inputs(self):
        self.assertRaises(ValueError,self.my_bank.set_password, 90.45)
        self.assertRaises(ValueError,self.my_bank.set_password, "")

    def test_password_too_short(self):
        with self.assertRaises(ValueError):
            self.my_bank.set_password("Ab1!")

    def test_password_missing_uppercase(self):
        with self.assertRaises(ValueError):
            self.my_bank.set_password("ab1!abcd")

    def test_password_missing_lowercase(self):
        with self.assertRaises(ValueError):
            self.my_bank.set_password("AB1!ABCD")

    def test_password_missing_digit(self):
        with self.assertRaises(ValueError):
            self.my_bank.set_password("Abc!defg")

    def test_password_missing_special_char(self):
        with self.assertRaises(ValueError):
            self.my_bank.set_password("Abc12345")

    def test_password_validity(self):
        self.my_bank.set_password("Abc123!@#")
        self.assertEqual("Abc123!@#", self.my_bank.get_password())

    def test_password_too_long(self):
        self.assertRaises(ValueError,self.my_bank.set_password, "Abc123!@#23yumne34")


    def test_age_condition_is_valid_no_invalid_input(self):
        self.assertRaises(ValueError,self.my_bank.set_age, "Maka")
        self.assertRaises(ValueError,self.my_bank.set_age, 98.99)
        self.assertRaises(ValueError,self.my_bank.set_age, "")
        self.assertRaises(ValueError,self.my_bank.set_age, 17)
        self.assertRaises(ValueError, self.my_bank.set_age, 101)
        self.my_bank.set_age(20)
        self.assertEqual(20, self.my_bank.get_age())


    def test_that_address_is_valid_and_met_certain_condition(self):
        self.assertRaises(ValueError, self.my_bank.set_address, 90.99)
        self.assertRaises(ValueError, self.my_bank.set_address, "")

    def test_address_empty_string(self):
        with self.assertRaises(ValueError):
            self.my_bank.set_address("")

    def test_address_too_short(self):
        with self.assertRaises(ValueError):
            self.my_bank.set_address("St.")

    def test_address_invalid_chars(self):
        with self.assertRaises(ValueError):
            self.my_bank.set_address("317 Mack Street !!!")

    def test_address_must_be_string(self):
        with self.assertRaises(TypeError):
            self.my_bank.set_address(12345)

    def test_address_valid(self):
        self.my_bank.set_address("317 Herbert Macaulay Sabo, Lagos")
        self.assertEqual("317 Herbert Macaulay Sabo, Lagos", self.my_bank.get_address())





    def test_that_phone_accept_valid_input_and_meet_certain_conditions(self):
        self.assertRaises(ValueError,self.my_bank.set_phone, 90)
        self.assertRaises(ValueError, self.my_bank.set_phone, 90.77)
        self.assertRaises(ValueError,self.my_bank.set_phone, "")

    def test_valid_local_numbers(self):
        self.my_bank.set_phone("08061234567")  # This will match MTN number
        self.assertEqual("08061234567", self.my_bank.get_phone())
        self.my_bank.set_phone("08123456789")  # This will match Airtel number
        self.assertEqual("08123456789", self.my_bank.get_phone())
        self.my_bank.set_phone("09051234567")  # This will match Glo number
        self.assertEqual("09051234567", self.my_bank.get_phone())

    def test_valid_international_numbers(self):
        self.my_bank.set_phone("+2348034322112")
        self.assertEqual("+2348034322112", self.my_bank.get_phone())
        self.my_bank.set_phone("+2348123456789")
        self.assertEqual("+2348123456789", self.my_bank.get_phone())
        self.my_bank.set_phone("+2349098765432")  # This will match 9mobile number
        self.assertEqual("+2349098765432", self.my_bank.get_phone())

    def test_invalid_numbers(self):
        with self.assertRaises(ValueError):
            self.my_bank.set_phone("2348034322112")
        with self.assertRaises(ValueError):
            self.my_bank.set_phone("08012345")
        with self.assertRaises(ValueError):
            self.my_bank.set_phone("02012345678")
        with self.assertRaises(ValueError):
            self.my_bank.set_phone("+19801234567")





class TestTheFunctionThatDepositMoneyIntoAccount(TestCase) :
    def setUp(self):
        self.my_bank = AccessBank("Makaveli", "Abc123!@#", "08034322112", 23)

    def test_that_the_function_dont_accept_invalid_input(self):
        self.assertRaises(ValueError, self.my_bank.deposit, 98)
        self.assertRaises(ValueError, self.my_bank.deposit, -1)
        self.assertRaises(ValueError, self.my_bank.deposit, 0)
        self.assertRaises(ValueError, self.my_bank.deposit, '')

    def test_that_function_dont_accept_string(self):
        self.assertRaises(ValueError, self.my_bank.deposit, "Maka")

    def test_the_deposit_function(self):
        result = self.my_bank.deposit(10000.00)
        self.assertEqual(result, self.my_bank.get_balance())
        self.my_bank.deposit(10000.00)
        self.assertEqual(20000.00, self.my_bank.get_balance())

    def test_negative_deposit_raises(self):
        self.assertRaises(ValueError, self.my_bank.deposit, -100)

    def test_wrong_type_deposit_raises(self):
        self.assertRaises(TypeError, self.my_bank.deposit, None)


class TestTheFunctionThatWithDrawMoneyFromBalance(TestCase) :
    def setUp(self):
        self.my_bank = AccessBank("Makaveli", "Abc123!@#", "08034322112", 23)

    def test_that_the_function_dont_accept_invalid_input(self):
        self.assertRaises(ValueError, self.my_bank.withdraw_money, "Maka")
        self.assertRaises(ValueError, self.my_bank.withdraw_money, 98)
        self.assertRaises(ValueError, self.my_bank.withdraw_money, -1)
        self.assertRaises(ValueError, self.my_bank.withdraw_money, 0)
        self.assertRaises(ValueError, self.my_bank.withdraw_money, '')

        self.my_bank.deposit(5000.00)
        self.my_bank.withdraw_money(2000.00)
        self.assertEqual(self.my_bank.get_balance(), 3000)

