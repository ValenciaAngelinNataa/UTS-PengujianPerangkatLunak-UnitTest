import unittest
from entity.book import Book
from domain.use_cases.browse_books import BrowseBook
from entity.book_repository_in_memory import BookRepositoryInMemory  # Import InMemory Repository

class TestBrowseBook(unittest.TestCase):
    def setUp(self):
        self.repo = BookRepositoryInMemory()  # Implementasi dari BookRepository
        self.use_case = BrowseBook(self.repo)  # Inject repository ke use case

    def test_browse_books_empty(self):
        # Test when no books are in the repository
        books = self.use_case.execute()
        self.assertEqual(len(books), 0)  # Should return empty list

    def test_browse_books_with_data(self):
        # Test when books are present in the repository
        book1 = Book("Sapiens", "Yuval Noah Harari", 2011)
        book2 = Book("1984", "George Orwell", 1949)
        self.repo.add(book1)
        self.repo.add(book2)

        books = self.use_case.execute()
        self.assertEqual(len(books), 2)  # Should return 2 books
        self.assertIn(book1, books)
        self.assertIn(book2, books)

    def test_browse_books_after_deletion(self):
        # Test browsing after deleting a book
        book1 = Book("Sapiens", "Yuval Noah Harari", 2011)
        book2 = Book("1984", "George Orwell", 1949)
        self.repo.add(book1)
        self.repo.add(book2)
        self.repo.delete(book1)  # Delete the first book

        books = self.use_case.execute()
        self.assertEqual(len(books), 1)  # Should return only 1 book
        self.assertNotIn(book1, books)  # Ensure book1 is removed

if __name__ == '__main__':
    unittest.main()