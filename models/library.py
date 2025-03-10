#This is a book storage
from models import BookWrapper

class Library:
    
    def __init__(self) -> None:
        """Initializer"""
        self.storage = []
    
    def add_books(self, book: BookWrapper) -> None:
        """Adds the books to the storage"""
        if book not in self.storage:
            self.storage.append(book)
        else:
            print('Book already exists')  
                
    def display_books(self) -> None:
        """Displays books"""
        if not self.storage:
            print('Books not found')
            
        else:
            for i, dct in enumerate(self.storage, start=1):
                print(f"{i}. {dct['author']} - {dct['title']}, published in {dct['year']}")