class BookController:
    def __init__(self, add_book, browse_book, delete_book, edit_book, read_book):
        self.add_book = add_book
        self.browse_book = browse_book
        self.delete_book = delete_book
        self.edit_book = edit_book
        self.read_book = read_book

    def add_book_controller(self, title, author, year):
        return self.add_book.execute(title, author, year)

    def browse_books_controller(self):
        return self.browse_book.execute()

    def delete_book_controller(self, book_id):
        return self.delete_book.execute(book_id)

    def edit_book_controller(self, book_id, title, author, year):
        return self.edit_book.execute(book_id, title, author, year)

    def read_book_controller(self, book_id):
        return self.read_book.execute(book_id)

#Entity/data => repository implementation, data class
#domain => repository abstract, usecase
# UI => controller (pisahkan UI function)