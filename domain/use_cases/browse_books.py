from domain.book_repository import BookRepository

class BrowseBook:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self):
        return self.book_repository.get_all_books()