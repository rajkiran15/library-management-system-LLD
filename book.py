
class Book:
    def __init__(self, book_id, title, author, genre, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.copies = copies
        self.available_copies = copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        if self.available_copies < self.copies:
            self.available_copies += 1
            return True
        return False
