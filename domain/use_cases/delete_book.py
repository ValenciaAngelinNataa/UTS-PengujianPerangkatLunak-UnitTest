from domain.book_repository import BookRepository

class DeleteBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book_id: int):
        book = self.repository.get_by_id(book_id)
        if book:
            self.repository.delete(book)
            return book
        return None