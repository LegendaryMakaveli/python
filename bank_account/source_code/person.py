import re


class Person :
    def __init__(self, name, address, email, phone_number):
        self.name = name
        self.address = address
        self.email = email
        self.phone_number = phone_number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) :
            raise TypeError('name must be a string')
        if value == "" :
            raise ValueError('name cannot be empty')
        self._name = value


    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not isinstance(value, str) :
            raise ValueError("address must be a string")
        if value == "" :
            raise ValueError('address cannot be empty')
        self.__validate_address(value)
        self._address = value

    @property
    def phone_number(self):
        return self._phone

    @phone_number.setter
    def phone_number(self, value):
        if not isinstance(value, str):
            raise ValueError("Number is collected as a string")
        if value == "":
            raise ValueError("phone number cannot be empty")
        self.__validate_phone(value)
        self._phone = value


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) :
            raise ValueError("email must be a string")
        if value == "" :
            raise ValueError("email cannot be empty")
        self.__validate_email(value)
        self._email = value



    @staticmethod
    def __validate_address(address):
        pattern = r"^[A-Za-z0-9\s,.-]{5,100}$"
        if not re.match(pattern, address):
            raise ValueError(
                "Address must be 5–100 characters and contain only letters, numbers, spaces, commas, dots, or hyphens")

    @staticmethod
    def __validate_phone(phone):
        phone_pattern = (
            r"^(?:0(70[1-9]|80[2-9]|81[0-9]|90[1-9]|91[2-6])\d{7}"
            r"|\+234(70[1-9]|80[2-9]|81[0-9]|90[1-9]|91[2-6])\d{7})$"
        )
        if not re.match(phone_pattern, phone):
             raise ValueError("Invalid Nigerian phone number format")

    @staticmethod
    def __validate_email(email):
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        if not re.fullmatch(pattern, email):
            raise ValueError("Invalid email pattern")


