from entity.book import Book

class AddBook:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, title: str, author: str, year: int):
        if not title:
            raise ValueError("Title cannot be empty")
        
        book = Book(title, author, year)
        self.repository.add(book)
        return book
