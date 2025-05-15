from entity.book import Book
from domain.book_repository import BookRepository

class EditBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book_id: int, title: str, author: str, year: int):
        # Mencari buku berdasarkan ID
        book = self.repository.get_by_id(book_id)
        
        if not book:
            return None  # Buku tidak ditemukan

        # Edit buku
        book.title = title
        book.author = author
        book.year = year

        return book