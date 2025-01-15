
class Member:
    def __init__(self, member_id, name, membership_type):
        self.member_id = member_id
        self.name = name
        self.membership_type = membership_type
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) < self.get_borrow_limit():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        return False

    def get_borrow_limit(self):
        return 5 if self.membership_type == "Premium" else 3
