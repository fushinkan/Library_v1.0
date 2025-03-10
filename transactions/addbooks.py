#This code adds the books to the storage
from models import BookWrapper, Library


class AddBook:
    
    def __init__(self, library: Library) -> None:
        """Initializer"""
        self.library = library
        
    def add_books(self, dct: BookWrapper) -> None:
        """Adds the books to the storage"""
        book = dct.to_dict()
        self.library.storage.append(book)