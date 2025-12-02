# Attributes: title (str) and author (str).
# Method: __init__(self, title, author) for initializing book attributes.
class Book:
    def __init__(self, title, author):
        self.title:str = title
        self.author:str  = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

#  EBook and PrintBook:
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size:int = file_size  # in MB
        # print(f"EBook : {self.title} by {self.author} of size {file_size}MB")

    def __str__(self):
        return f"EBook: {self.title} by {self.author} of size {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count:int = page_count # in kg

    def __str__(self):
       print(f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count} kg")


#     Attributes: books (a list to store instances of Book, EBook, and PrintBook).
# Methods:
# add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
# list_books(self): Prints details of each book in the library.
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            print(book)
        return None