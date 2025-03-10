#This is the main file of the Library Management console application

from models import Book, BookWrapper, Library
from transactions import AddBook

def main():
    
    book = Book(author="Pushkin", title="Captain's daughter", year=1836)
    print(book)
    dct = BookWrapper(book)
    library = Library()
    book_n = AddBook(library)
    book_n.add_books(book)
    
    library.display_books()
    

if __name__ == "__main__":
    main()