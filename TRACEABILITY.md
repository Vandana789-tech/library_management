# Traceability Matrix – Library Book Management System

Traceability ensures that each user story is properly implemented, tested, and delivered in a specific sprint and release. It links requirements to code, tests, and Git tags.

| User Story ID | Description                         | Sprint   | Code Reference    | Test Case                                              | Git Tag |
| ------------- | ----------------------------------- | -------- | ----------------- | ------------------------------------------------------ | ------- |
| US-1          | Add new book with ID, title, author | Sprint 1 | add_book()        | test_add_book_success                                  | v0.1    |
| US-2          | Reject duplicate Book ID            | Sprint 1 | add_book()        | test_add_duplicate_book                                | v0.1    |
| US-3          | Borrow a book                       | Sprint 2 | borrow_book()     | test_borrow_book_success                               | v0.2    |
| US-4          | Prevent borrowing unavailable book  | Sprint 2 | borrow_book()     | test_borrow_unavailable_book                           | v0.2    |
| US-5          | Return a borrowed book              | Sprint 2 | return_book()     | test_return_book                                       | v0.2    |
| US-6          | Generate library status report      | Sprint 3 | generate_report() | test_report_contains_header, test_report_contains_book | v0.3    |

