
class Transaction:
    def __init__(self, member, book, borrow_date, due_date):
        self.transaction_id = f"{member.member_id}-{book.book_id}-{borrow_date.timestamp()}"
        self.member = member
        self.book = book
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = None

    def mark_returned(self):
        self.return_date = datetime.now()

    def calculate_fine(self):
        if self.return_date and self.return_date > self.due_date:
            overdue_days = (self.return_date - self.due_date).days
            return overdue_days * 3  # Assume $3 per overdue day
        return 0
