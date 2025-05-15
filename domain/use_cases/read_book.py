from domain.book_repository import BookRepository

class ReadBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book_id: int):
        return self.repository.get_by_id(book_id)