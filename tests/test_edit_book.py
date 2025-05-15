import unittest
from entity.book import Book
from domain.use_cases.edit_book import EditBook
from entity.book_repository_in_memory import BookRepositoryInMemory

class TestEditBook(unittest.TestCase):
    def setUp(self):
        self.repo = BookRepositoryInMemory()
        self.use_case = EditBook(self.repo)

        # Menambahkan buku awal untuk diuji edit-nya
        self.book1 = Book("Sapiens", "Yuval Noah Harari", 2011)
        self.repo.add(self.book1)

    def test_edit_existing_book(self):
        # Edit buku yang ada
        edited_book = self.use_case.execute(self.book1.id, "Sapiens (Revised)", "Yuval Noah Harari", 2020)
        
        self.assertEqual(edited_book.title, "Sapiens (Revised)")
        self.assertEqual(edited_book.author, "Yuval Noah Harari")
        self.assertEqual(edited_book.year, 2020)

    def test_edit_nonexistent_book(self):
        # Coba edit buku yang tidak ada
        result = self.use_case.execute(999, "Nonexistent Book", "Unknown Author", 2025)
        self.assertIsNone(result)

    def test_edit_book_with_invalid_data(self):
        # Coba edit buku dengan data invalid (misalnya, title kosong)
        result = self.use_case.execute(self.book1.id, "", "Yuval Noah Harari", 2025)
        self.assertEqual(result.title, "")
        self.assertEqual(result.author, "Yuval Noah Harari")
        self.assertEqual(result.year, 2025)

if __name__ == '__main__':
    unittest.main()