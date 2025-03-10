#This file contains information about an instance of the Book class

from transactions import generate_id
class Book:
    
    def __init__(self, author: str, title: str, year: int) -> None:
        """Initializer"""
        self.id = generate_id()
        self.author = author
        self.title = title
        self.year = year
        self.status = 'Available'
        
    def __str__(self) -> str:
        """Displays information about an instance of the Book class"""
        return f"{self.author} - {self.title}, published in {self.year}"