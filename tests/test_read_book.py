import unittest
from domain.use_cases.read_book import ReadBook
from entity.book_repository_in_memory import BookRepositoryInMemory
from entity.book import Book

class TestReadBook(unittest.TestCase):
    def setUp(self):
        self.repo = BookRepositoryInMemory()
        self.use_case = ReadBook(self.repo)

    def test_read_existing_book(self):
        book = Book("Sapiens", "Yuval Noah Harari", 2011)
        self.repo.add(book)
        found = self.use_case.execute(book.id)
        self.assertEqual(found.title, "Sapiens")
        self.assertEqual(found.author, "Yuval Noah Harari")
        self.assertEqual(found.year, 2011)

    def test_read_non_existing_book(self):
        found = self.use_case.execute(999)  # ID tidak ada
        self.assertIsNone(found)

    def test_read_book_with_empty_repository(self):
            # Test when the repository is empty (no books added yet)
            result = self.use_case.execute(1)  # ID yang tidak ada
            self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()