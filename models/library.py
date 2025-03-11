#This is a book storage
import json
from models import BookWrapper

class Library:
    
    def __init__(self) -> None:
        """Initializer"""
        self.storage = []
    
    def add_books(self, dct: BookWrapper, filename='./storage/storage.json') -> None:
        """Adds the books to the storage"""
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.storage = json.load(file)
        except FileNotFoundError:
            self.storage = []
            
        book = dct.to_dict()
        self.storage.append(book)
        
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.storage, file, indent=4)
    
    def display_books(self, filename='./storage/storage.json') -> None:
        """Displays books in the storage"""
        try: 
            with open(filename, 'r', encoding='utf-8') as file:
                storage = json.load(file)
        except FileNotFoundError:
            print('File not found. Make sure the file exists')
            return

        if not storage:
            print('Books not found')
            return
        
        for i, item in enumerate(storage, start=1):
            print(f'{i}. {item['author']} - {item['title']}, published in {item['year']}')