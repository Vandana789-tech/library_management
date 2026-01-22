class Library:
    def __init__(self):
        # Store books using Book ID as key
        # Each book = {title, author, status}
        self.books = {}

    # -------- Sprint 1 --------
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Book ID already exists")

        self.books[book_id] = {
            "title": title,
            "author": author,
            "status": "Available"
        }

    # -------- Sprint 2 --------
    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")

        if self.books[book_id]["status"] == "Borrowed":
            raise ValueError("Book already borrowed")

        self.books[book_id]["status"] = "Borrowed"

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")

        self.books[book_id]["status"] = "Available"

    # -------- Sprint 3 --------
    def generate_report(self):
        report = "BookID | Title | Author | Status\n"
        report += "-" * 40 + "\n"

        for book_id, data in self.books.items():
            report += f"{book_id} | {data['title']} | {data['author']} | {data['status']}\n"

        return report
print("successful")
