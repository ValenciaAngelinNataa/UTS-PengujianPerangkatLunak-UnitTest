from domain.use_cases.add_book import AddBook
from domain.use_cases.browse_books import BrowseBook
from domain.use_cases.delete_book import DeleteBook
from domain.use_cases.edit_book import EditBook
from domain.use_cases.read_book import ReadBook
from entity.book_repository_in_memory import BookRepositoryInMemory
from ui.book_controller import BookController

def main():
    # Setup repository dan controller
    repository = BookRepositoryInMemory()
    controller = BookController(
        AddBook(repository),
        BrowseBook(repository),
        DeleteBook(repository),
        EditBook(repository),
        ReadBook(repository)
    )

    # Tambah buku
    book1 = controller.add_book_controller("Sapiens", "Yuval Noah Harari", 2011)
    book2 = controller.add_book_controller("1984", "George Orwell", 1949)
    print(f"Buku ditambahkan: {book1.title} dan {book2.title}")

    # Lihat semua buku
    books = controller.browse_books_controller()
    print("\nDaftar Buku:")
    for book in books:
        print(f"ID: {book.id}, Judul: {book.title}, Penulis: {book.author}, Tahun: {book.year}")

    # Edit buku
    updated_book = controller.edit_book_controller(book1.id, "Sapiens (Revised)", "Yuval Noah Harari", 2020)
    print(f"\nBuku diperbarui: ID {updated_book.id}, Judul: {updated_book.title}, Tahun: {updated_book.year}")

    # Lihat detail buku
    book_detail = controller.read_book_controller(book1.id)
    print(f"\nDetail Buku: ID {book_detail.id}, Judul: {book_detail.title}, Penulis: {book_detail.author}, Tahun: {book_detail.year}")

    # Hapus buku
    deleted_book = controller.delete_book_controller(book2.id)
    print(f"\nBuku dihapus: ID {deleted_book.id}, Judul: {deleted_book.title}")

    # Lihat semua buku setelah penghapusan
    books = controller.browse_books_controller()
    print("\nDaftar Buku Setelah Penghapusan:")
    for book in books:
        print(f"ID: {book.id}, Judul: {book.title}, Penulis: {book.author}, Tahun: {book.year}")

if __name__ == "__main__":
    main()
