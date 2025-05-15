import unittest
from entity.book_repository_in_memory import BookRepositoryInMemory
from entity.book import Book

class TestBookRepositoryInMemory(unittest.TestCase):
    def setUp(self):
        self.repo = BookRepositoryInMemory()

    def test_add_book(self):
        book = Book("Sapiens", "Yuval Noah Harari", 2011)
        self.repo.add(book)
        self.assertEqual(len(self.repo.get_all_books()), 1)
        self.assertEqual(self.repo.get_all_books()[0].title, "Sapiens")

    def test_get_by_id(self):
        book = Book("1984", "George Orwell", 1949)
        self.repo.add(book)
        found = self.repo.get_by_id(book.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.title, "1984")

    def test_delete_book(self):
        book = Book("Sapiens", "Yuval Noah Harari", 2011)
        self.repo.add(book)
        self.repo.delete(book)
        self.assertEqual(len(self.repo.get_all_books()), 0)

if __name__ == '__main__':
    unittest.main()