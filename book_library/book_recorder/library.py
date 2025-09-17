from book_recoder import Book


class BookLibrary:
    book_list = []

    def create_book(self, title, is_borrowed,description):
        key = "name"
        book = {key: title, "status": is_borrowed, "description": description}
        self.book_list.append(book)
        return f"The book:\n {book}\n has been added."

    def borrow_book(self,title):
        for book in self.book_list:
            if book["name"] == title:
                book["status"] = True
                return f"The book {book} has been borrowed successfully."
            else:
                return f"The book {book} is unavailable."

        return f"The book {title} is not found."


