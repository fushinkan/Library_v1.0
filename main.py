#This is the main file of the Library Management console application

from models import Book, BookWrapper, Library

def main():
    
    book = Book(author="Pushkin", title="Captain's daughter", year=1836)
    book_n = Book(author="Lev Tolstoi", title="War and Peace", year=1812)
    book_n = Book(author="Lev Tolstoi", title="War and Peace", year=1813)
    dct = BookWrapper(book)
    dct_n = BookWrapper(book_n)
    library = Library()
    
    library.add_books(dct_n)
    library.display_books()
    library.add_books(dct)
    
    

if __name__ == "__main__":
    main()