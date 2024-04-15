# [Single-Responsibility Principle (SRP)] Implement a simple program to interact with the library catalog system. Create a Python class Book to represent a single book with attributes: Title, Author, ISBN, Genre, Availability (whether the book is available for borrowing or not). Create another Python class LibraryCatalog to manage the collection of books with following functionalities:

## Add books by storing each book objects (Hint: Create an empty list in constructor and store book objects)
## get book details and get all books from the list of objects

# Lets say, we need a book borrowing process (what books are borrowed and what books are available for borrowing). Implement logics to integrate this requirement in the above system. Design the classes with a clear focus on adhering to the Single Responsibility Principle(SRP) which represents that "A module should be responsible to one, and only one, actor."

class Book:
    def __init__(self, title, author, isbn, genre, availability):
        self.title = title
        self.author = author
        self.isbn = isbn 
        self.genre = genre 
        self.availability = availability
    
    def get_detail(self):
        return (self.title, self.author, self.isbn, self.genre, self.availability)
    

class LibraryCatalog:
    def __init__(self):
        self.books_list = []
    
    def add_book(self, book):
        self.books_list.append(book)
    
    def get_book_details(self, title):
        for book in self.books_list:
            if book.title == title:
                return book.get_detail()
        return "Book not found in library catalog"
    
    def get_all_books(self):
        if len(self.books_list) == 0:
            return "No books available in the catalog"
        return [book.get_detail() for book in self.books_list]

class BookManager:
    """
    class for borrowing and returning book
    """
    def __init__(self, library_catalog:LibraryCatalog):
        self.books_list = library_catalog.books_list
    
    def borrow_book(self, title):
        for book in self.books_list:
            if book.title == title:
                if book.availability:
                    book.availability = False 
                    print(f"{title} is borrowed.")
                else:
                    print(f"{title} is not available")

        print("f{title} is not found in library catalog")

    def return_book(self, title):
        for book in self.books_list:
            if book.title == title:
                if not book.availability:
                    book.availability = True 
                    print(f"{title} is returned.")
                else:
                    print(f"{title} is already available")

        print("f{title} is not found in library catalog")


catalog = LibraryCatalog()
book_manager = BookManager(catalog)

book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "9780747532743", "Fantasy", True)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Classic", True)
catalog.add_book(book1)
catalog.add_book(book2)

print()
print("get all books")
print(catalog.get_all_books())

print()
print("get individual book detail")
book_title = "The Great Gatsby"
print(catalog.get_book_details(title=book_title))

print()
print("BORROW BOOK")
book_manager.borrow_book(book_title)
print(catalog.get_book_details(title=book_title))

print("\n")
print("RETURN BOOK")
book_manager.return_book(book_title)
print(catalog.get_book_details(title=book_title))
