# This is a sample Python script.
from library import BookLibrary
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from book_recorder.library import BookLibrary

if __name__ == '__main__':
    book_recorder = BookLibrary()

    book_response = book_recorder.create_book("The Evil King", False, ["Terrible Book", "very Tragic"])
    book_recorder.create_book("The Mad King", False, "Manageable")
    book_recorder.create_book("The Wicked King", False, 404)

    get_book_response = book_recorder.borrow_book("The Evil King")
    print("The response is: ",get_book_response)
    for book in book_recorder.book_list:
        print(book)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
