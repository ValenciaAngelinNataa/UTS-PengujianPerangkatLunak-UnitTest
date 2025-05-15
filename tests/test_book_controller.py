import unittest
from ui.book_controller import BookController
from domain.use_cases.add_book import AddBook
from domain.use_cases.browse_books import BrowseBook
from domain.use_cases.delete_book import DeleteBook
from domain.use_cases.edit_book import EditBook
from domain.use_cases.read_book import ReadBook
from entity.book_repository_in_memory import BookRepositoryInMemory

class TestBookController(unittest.TestCase):
    def setUp(self):
        self.repo = BookRepositoryInMemory()
        self.controller = BookController(
            AddBook(self.repo),
            BrowseBook(self.repo),
            DeleteBook(self.repo),
            EditBook(self.repo),
            ReadBook(self.repo)
        )

    def test_add_book_controller(self):
        book = self.controller.add_book_controller("Sapiens", "Yuval Noah Harari", 2011)
        self.assertEqual(book.title, "Sapiens")
        self.assertEqual(len(self.repo.get_all_books()), 1)

    def test_browse_books_controller(self):
        self.controller.add_book_controller("Sapiens", "Yuval Noah Harari", 2011)
        self.controller.add_book_controller("1984", "George Orwell", 1949)
        books = self.controller.browse_books_controller()
        self.assertEqual(len(books), 2)

    def test_delete_book_controller(self):
        book = self.controller.add_book_controller("Sapiens", "Yuval Noah Harari", 2011)
        deleted_book = self.controller.delete_book_controller(book.id)
        self.assertEqual(deleted_book.title, "Sapiens")
        self.assertEqual(len(self.repo.get_all_books()), 0)

    def test_edit_book_controller(self):
        book = self.controller.add_book_controller("Sapiens", "Yuval Noah Harari", 2011)
        updated_book = self.controller.edit_book_controller(book.id, "Sapiens (Revised)", "Yuval Noah Harari", 2020)
        self.assertEqual(updated_book.title, "Sapiens (Revised)")
        self.assertEqual(updated_book.year, 2020)

    def test_read_book_controller(self):
        book = self.controller.add_book_controller("Sapiens", "Yuval Noah Harari", 2011)
        found_book = self.controller.read_book_controller(book.id)
        self.assertEqual(found_book.title, "Sapiens")
        self.assertEqual(found_book.author, "Yuval Noah Harari")

if __name__ == '__main__':
    unittest.main()