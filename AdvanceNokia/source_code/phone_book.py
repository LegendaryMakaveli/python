class PhoneBook:
    def __init__(self):
        self.contact = []

    def add_contact(self, name, contact):
        self.contact.append({"name": name, "contact": contact})
