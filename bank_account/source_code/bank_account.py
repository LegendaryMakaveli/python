from decimal import Decimal
from random import randrange

from .person import Person


class Bank(Person):
    def __init__(self, first_name, last_name, address, email, phone_number, bvn):
        full_name = f"{first_name} {last_name}"
        super().__init__(full_name, address, email, phone_number)
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = self.__generate_account_number()
        self.balance = Decimal(0.0)
        self.NIN = "39393939393"
        self.bvn = bvn


    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.__validate_name_input(value)
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.__validate_name_input(value)
        self._last_name = value


    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value == "":
            raise ValueError("Balance cannot be an empty string")
        if not isinstance(value, (int, float, Decimal)):
            raise ValueError("Balance must be a number")

        if value < 0:
            raise ValueError("Balance cannot be negative")
        if value > 500000:
            raise ValueError("Balance cannot be greater than 500000")
        self._balance = value


    @property
    def NIN(self):
        return self._NIN

    @NIN.setter
    def NIN(self, value):
        self.__validation(value)
        self._NIN = value


    @property
    def bvn(self):
        return self._bvn

    @bvn.setter
    def bvn(self, value):
        self.__validation(value)
        self._bvn = value

    def deposit(self, amount):
        if amount == "":
            raise ValueError("Balance cannot be an empty string")
        if not isinstance(amount, (int, float, Decimal)):
            raise ValueError("Balance must be a number")

        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Withdraw amount cannot be greater than the balance")
        if amount < self.balance and amount != 0 :
            self.balance -= amount







    @staticmethod
    def __validate_name_input(value):
        if not isinstance(value, str):
            raise ValueError("First Name must be a string")
        if value == "":
            raise ValueError("First Name cannot be an empty string")

    @staticmethod
    def __generate_account_number():
        return "14" + str(randrange(10000000,99999999))

    @staticmethod
    def __validation(value):
        if not value.isdigit():
            raise ValueError("NIN cannot contain letters")
        if len(value) != 11:
            raise ValueError("NIN is not complete")
        if value == "":
            raise ValueError("NIN cannot be empty")

