#This code wraps an instance of the Book class into a dictionary so that it can be written to the Library

from models import Book

class BookWrapper:
    
    def __init__(self, book: Book) -> None:
        """Initializer"""
        self.book = book
        
    def to_dict(self) -> dict:
        """Wraps an instance of the Book class into a dictionary"""
        return {
            'id': self.book.id,
            'author': self.book.author,
            'title': self.book.title,
            'year': self.book.year,
            'status': self.book.status
        }