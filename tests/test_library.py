import unittest
from src.library import Library


class TestLibrary(unittest.TestCase):

    # -------- Sprint 1 Tests --------
    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B1", "Python Basics", "Guido")
        self.assertIn("B1", lib.books)

    def test_add_duplicate_book(self):
        lib = Library()
        lib.add_book("B1", "Python Basics", "Guido")
        with self.assertRaises(ValueError):
            lib.add_book("B1", "AI", "OpenAI")

    # -------- Sprint 2 Tests --------
    def test_borrow_book_success(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        lib.borrow_book("B1")
        self.assertEqual(lib.books["B1"]["status"], "Borrowed")

    def test_borrow_unavailable_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        lib.borrow_book("B1")
        with self.assertRaises(ValueError):
            lib.borrow_book("B1")

    def test_return_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        lib.borrow_book("B1")
        lib.return_book("B1")
        self.assertEqual(lib.books["B1"]["status"], "Available")

    # -------- Sprint 3 Tests --------
    def test_report_contains_header(self):
        lib = Library()
        report = lib.generate_report()
        self.assertIn("BookID | Title | Author | Status", report)

    def test_report_contains_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        report = lib.generate_report()
        self.assertIn("B1 | Python | Guido | Available", report)


if __name__ == "__main__":
    unittest.main()
print("successful")
