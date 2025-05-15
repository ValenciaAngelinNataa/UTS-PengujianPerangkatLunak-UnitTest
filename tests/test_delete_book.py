import unittest
from entity.book import Book
from domain.use_cases.delete_book import DeleteBook
from entity.book_repository_in_memory import BookRepositoryInMemory

class TestDeleteBook(unittest.TestCase):
    def setUp(self):
        self.repo = BookRepositoryInMemory()
        self.use_case = DeleteBook(self.repo)

    def test_delete_existing_book(self):
        book = Book("Sapiens", "Yuval Noah Harari", 2011)
        self.repo.add(book)

        deleted_book = self.use_case.execute(book.id)
        self.assertEqual(deleted_book.id, book.id)
        self.assertNotIn(book, self.repo.books)

    def test_delete_nonexistent_book(self):
        # Trying to delete a book that doesn't exist
        result = self.use_case.execute(999)  # ID yang belum ada
        self.assertIsNone(result)

    def test_delete_from_empty_repository(self):
        # Trying to delete a book from an empty repository
        result = self.use_case.execute(1)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()