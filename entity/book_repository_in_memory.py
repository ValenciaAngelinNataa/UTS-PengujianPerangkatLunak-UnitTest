from domain.book_repository import BookRepository

class BookRepositoryInMemory(BookRepository):
    def __init__(self):
        self.books = []
        self._next_id = 1

    def add(self, book):
        if book.id is None:
            book.id = self._next_id
            self._next_id += 1
        self.books.append(book)

    def get_by_id(self, id):
        for book in self.books:
            if book.id == id:
                return book
        return None

    def get_all_books(self):
        return self.books

    def delete(self, book):
        self.books = [b for b in self.books if b.id != book.id]
