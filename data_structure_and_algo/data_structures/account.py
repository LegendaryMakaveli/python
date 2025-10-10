from decimal import Decimal
from random import randrange


class Account :
    def __init__(self, name, phone):
        self.name = name
        self.balance = Decimal(0.0)
        self.phone = phone
        self.account_number = self.__generate_account_number()

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            if value == "":
                raise ValueError("Name cannot be an empty string")
            self._name = value

        @property
        def phone(self):
            return self._phone

        @phone.setter
        def phone(self, value):
            if len(value) != 11 :
                raise ValueError("Phone number must be 10 digits")
            self._phone = value

    @staticmethod
    def __generate_account_number():
        return "33" + str(randrange(10000000, 99999999))
    
