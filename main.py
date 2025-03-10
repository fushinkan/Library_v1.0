#This is the main file of the Library Management console application

from models import Book, BookWrapper, Library

def main():
    
    book = Book(author="Pushkin", title="Captain's daughter", year=1836)
    print(book)
    dct = BookWrapper(book)
    library = Library()
    book_n = dct.to_dict()
    library.add_books(book_n)
    library.display_books() 
    

if __name__ == "__main__":
    main()