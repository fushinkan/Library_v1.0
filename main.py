#This is the main file of the Library Management console application

from models import Book

def main():
    
    book = Book(author="Pushkin", title="Captain's daughter", year=1836)
    print(book)
    

if __name__ == "__main__":
    main()