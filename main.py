from book import Book
from member import Member
from library import Library

# Initialize library
library = Library()

# Add books
book1 = Book(1, "1984", "George Orwell", "Dystopian", 3)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", "Fiction", 2)
library.add_book(book1)
library.add_book(book2)

# Register members
member1 = Member(101, "Alice", "Regular")
member2 = Member(102, "Bob", "Premium")
library.register_member(member1)
library.register_member(member2)

# Borrow book
transaction = library.borrow_book(101, 1)
if transaction:
    print(f"Book borrowed! Transaction ID: {transaction.transaction_id}")

# Return book
if library.return_book(101, 1):
    print("Book returned successfully!")
