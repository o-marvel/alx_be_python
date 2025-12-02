# Attributes: title (str) and author (str).
# Method: __init__(self, title, author) for initializing book attributes.
class Book:
    def __init__(self, title, author):
        self.title:str = title
        self.author:str  = author
        print(f"Book : {self.title} by {self.author}")
#
#  EBook and PrintBook:
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size:int = file_size  # in MB
        print(f"EBook : {self.title} by {self.author} of size {file_size}MB")

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count:int = page_count # in kg
        print(f"PrintBook : {self.title} by {self.author} of pages {page_count}")


#     Attributes: books (a list to store instances of Book, EBook, and PrintBook).
# Methods:
# add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
# list_books(self): Prints details of each book in the library.
class Library:
    def __init__(self):
        self.books:list = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
            #   Book: Pride and Prejudice by Jane Austen
            # if isinstance(book, EBook):
            #     print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}MB")
            # elif isinstance(book, PrintBook):
            #     print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            # else:
            #     print(f"Book: {book.title} by {book.author}")