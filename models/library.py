#This is a book storage
from transactions import AddBook

class Library:
    
    def __init__(self) -> None:
        """Initializer"""
        self.storage = []
    
    def display_books(self):
        for book in self.storage:
            print(book)