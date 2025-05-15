class Book:
    def __init__(self, title: str, author: str, year: int):
        if not title:
            raise ValueError("Title cannot be empty")
        self.id = None
        self.title = title
        self.author = author
        self.year = year
