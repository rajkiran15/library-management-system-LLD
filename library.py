from book import Book
from member import Member
from transaction import Transaction
from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_id, book_id):
        member = self.get_member(member_id)
        book = self.get_book(book_id)

        if member and book and book.borrow():
            if member.borrow_book(book):
                due_date = datetime.now() + timedelta(days=14)
                transaction = Transaction(member, book, datetime.now(), due_date)
                return transaction
        return None

    def return_book(self, member_id, book_id):
        member = self.get_member(member_id)
        book = self.get_book(book_id)

        if member and book and book.return_book():
            if member.return_book(book):
                return True
        return False

    def get_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def get_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
