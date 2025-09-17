class Book :
    title = ""
    author = ""
    isbn = ""
    description = ""
    is_borrowed = False

    def __init__(self, title, isbn, author="Makaveli"):
        self.title = title
        self.author = author
        self.isbn = isbn


    def get_book_title(self):
        return self.title


    def check_book_availability(self):
       return self.is_borrowed

    def add_description(self, description):
        self.description = description
        return f"Description added..."

    def borrow_book(self):
        if not self.check_book_availability():
            self.is_borrowed = True


    def __str__(self):
        return f"{self.title}\n{self.author}\n{self.isbn}\n{self.description}"