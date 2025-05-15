from domain.use_cases.add_book import AddBook
from domain.use_cases.browse_books import BrowseBook
from domain.use_cases.delete_book import DeleteBook
from domain.use_cases.edit_book import EditBook
from domain.use_cases.read_book import ReadBook
from entity.book_repository_in_memory import BookRepositoryInMemory
from ui.book_controller import BookController

def main():
    repository = BookRepositoryInMemory()
    controller = BookController(
        AddBook(repository),
        BrowseBook(repository),
        DeleteBook(repository),
        EditBook(repository),
        ReadBook(repository)
    )

    while True:
        print("\n--- MENU ---")
        print("1. Tambah Buku")
        print("2. Lihat Semua Buku")
        print("3. Hapus Buku")
        print("4. Edit Buku")
        print("5. Lihat Detail Buku")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            controller.add_book_controller()
        elif pilihan == '2':
            controller.browse_books_controller()
        elif pilihan == '3':
            controller.delete_book_controller()
        elif pilihan == '4':
            controller.edit_book_controller()
        elif pilihan == '5':
            controller.read_book_controller()
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
