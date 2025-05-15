from abc import ABC, abstractmethod

class BookRepository(ABC):
    @abstractmethod
    def add(self, book):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_all_books(self):
        pass

    @abstractmethod
    def delete(self, book):
        pass
