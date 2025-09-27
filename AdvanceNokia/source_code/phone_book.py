class PhoneBook:
    def __init__(self):
        self.contact = []

    def add_contact(self, name, contact):
        self.contact.append({"name": name, "contact": contact})

    def search(self, name):
        for log in self.contact:
            if log["name"] == name:
                return f"{log['name']}, {log['contact']}"
        else :
            raise NameError("Name not found")


        

