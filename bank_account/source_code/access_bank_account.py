import re

class AccessBank :
    def __init__(self, name,password,phone,age=18,balance=0):
        self.name = name
        self.password = password
        self.balance = balance
        self.age = age
        self.address = ""
        self.phone = phone

    def set_name(self,name):
        if isinstance(name, int) :
            raise ValueError("Name cannot have number in_between")
        elif isinstance(name, float) :
            raise ValueError("Name cannot have number in_between")
        elif not name.strip() :
            raise ValueError("Name cannot be empty")
        self.name = name.strip().upper()

    def get_name(self):
        return self.name





    def set_password(self, new_password):
        if not isinstance(new_password, str) :
            raise ValueError("Password must be of type str")
        elif len(new_password) < 8 or len(new_password) > 16 :
            raise ValueError("Password must be at least 8 characters long")
        elif not re.search(r"[A-Z]", new_password):
            raise ValueError("Password must contain at least one uppercase letter")
        elif not re.search(r"[a-z]", new_password):
            raise ValueError("Password must contain at least one lowercase letter")
        elif not re.search(r"\d", new_password):
            raise ValueError("Password must contain at least one digit")
        elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", new_password):
            raise ValueError("Password must contain at least one special character")
        elif not new_password.strip() :
            raise ValueError("Password cannot be empty")
        self.password = new_password

    def get_password(self):
        return self.password





    def set_age(self, new_age):
        if isinstance(new_age, str) :
            raise ValueError("Age cannot be type string")
        elif isinstance(new_age, float) :
            raise ValueError("Point number is not allowed")

        if new_age < 18 or new_age > 100:
            raise ValueError("Age must be at least 18 years old")
        elif not new_age :
            raise ValueError("Age cannot be empty")

        self.age = new_age

    def get_age(self):
        return self.age





    def set_address(self, address):
        if isinstance(address, float) :
            raise ValueError("No point number")
        elif not address :
            raise ValueError("Address cannot be empty")

        pattern = r"^[A-Za-z0-9\s,.-]{5,100}$"
        if not re.match(pattern, address):
            raise ValueError(
                "Address must be 5–100 characters and contain only letters, numbers, spaces, commas, dots, or hyphens")
        self.address = address

    def get_address(self):
        return self.address






    def set_phone(self, new_phone):
        if isinstance(new_phone, int) :
            raise ValueError("Phone cannot be type string")
        elif isinstance(new_phone, float) :
            raise ValueError("No point number")
        elif not new_phone :
            raise ValueError("Phone cannot be empty")
        self.phone = new_phone

        phone_pattern = (
            r"^(?:0(70[1-9]|80[2-9]|81[0-9]|90[1-9]|91[2-6])\d{7}"
            r"|\+234(70[1-9]|80[2-9]|81[0-9]|90[1-9]|91[2-6])\d{7})$"
        )
        if not re.match(phone_pattern, new_phone):
            raise ValueError("Invalid Nigerian phone number format")

    def get_phone(self):
        return self.phone

    def deposit(self, amount):
        if isinstance(amount, str):
            raise ValueError("No string allowed")
        elif isinstance(amount, int) :
            raise ValueError("No integer allowed")
        elif amount <= 0 :
            raise ValueError("Negative or Zero number is not allowed")
        elif not amount :
            raise ValueError("Cannot be empty")

        if amount > 0 :
            self.balance += amount

        return self.balance

    def get_balance(self):
        return self.balance




    def sum_digits(self,number):
        return sum(int(digit) for digit in str(number))

    def validate_credit_card(self, card_number):
        if card_number is None or len(card_number) == 0:
            return False
        if len(card_number) < 13 or len(card_number) > 16:
            return False

        result = 0

        for position, digit in enumerate(reversed(card_number)):
            if position % 2 == 1:
                digit *= 2
                digit = self.sum_digits(digit)
            result += digit
        return result % 10 == 0



    def withdraw_money(self, amount, card_number):
        if isinstance(amount, str):
            raise ValueError("No string allowed")
        elif isinstance(amount, int):
            raise ValueError("No integer allowed")
        elif amount <= 0:
            raise ValueError("Negative or Zero number is not allowed")
        elif not amount:
            raise ValueError("Cannot be empty")

        if not self.validate_credit_card(card_number):
            raise ValueError("Invalid credit card")

        if self.balance >= amount :
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

        return float(self.balance)

