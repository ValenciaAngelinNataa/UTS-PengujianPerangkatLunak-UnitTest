import unittest
from entity.book import Book
from domain.use_cases.add_book import AddBook
from entity.book_repository_in_memory import BookRepositoryInMemory

class TestAddBook(unittest.TestCase):
    def setUp(self):
        self.repo = BookRepositoryInMemory()  # Menggunakan repository in-memory
        self.use_case = AddBook(self.repo)

    def test_add_book_success(self):
        book = self.use_case.execute("Sapiens", "Yuval Noah Harari", 2011)
        self.assertEqual(book.title, "Sapiens")
        self.assertEqual(book.author, "Yuval Noah Harari")
        self.assertEqual(book.year, 2011)

    def test_add_multiple_books(self):
        b1 = self.use_case.execute("1984", "George Orwell", 1949)
        b2 = self.use_case.execute("Brave New World", "Aldous Huxley", 1932)
        self.assertEqual(b1.id, 1)  # ID pertama seharusnya 1
        self.assertEqual(b2.id, 2)  # ID kedua seharusnya 2

    def test_add_book_with_empty_title(self):
        with self.assertRaises(ValueError):
            self.use_case.execute("", "Author", 2000)

if __name__ == '__main__':
    unittest.main()