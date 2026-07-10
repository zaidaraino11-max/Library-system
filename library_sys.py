import json
import os


class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }


class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self):
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()

        for book in self.books:
            if book.isbn == isbn:
                print("A book with this ISBN already exists.")
                return

        self.books.append(Book(title, author, isbn))
        self.save_books()
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("\nNo books in the library.")
            return

        print("\n------ BOOK LIST ------")
        for i, book in enumerate(self.books, start=1):
            status = "Available" if book.available else "Borrowed"
            print(f"\nBook {i}")
            print(f"Title : {book.title}")
            print(f"Author: {book.author}")
            print(f"ISBN  : {book.isbn}")
            print(f"Status: {status}")

    def search_book(self):
        keyword = input("Enter title or author: ").lower()

        found = False

        for book in self.books:
            if keyword in book.title.lower() or keyword in book.author.lower():
                status = "Available" if book.available else "Borrowed"

                print("\nBook Found")
                print(f"Title : {book.title}")
                print(f"Author: {book.author}")
                print(f"ISBN  : {book.isbn}")
                print(f"Status: {status}")

                found = True

        if not found:
            print("No matching book found.")

    def borrow_book(self):
        isbn = input("Enter ISBN of the book: ")

        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    self.save_books()
                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed.")
                return

        print("Book not found.")

    def return_book(self):
        isbn = input("Enter ISBN of the book: ")

        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    self.save_books()
                    print("Book returned successfully!")
                else:
                    print("This book was not borrowed.")
                return

        print("Book not found.")

    def remove_book(self):
        isbn = input("Enter ISBN to remove: ")

        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books()
                print("Book removed successfully!")
                return

        print("Book not found.")

    def save_books(self):
        data = []

        for book in self.books:
            data.append(book.to_dict())

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_books(self):
        if not os.path.exists("books.json"):
            return

        with open("books.json", "r") as file:
            try:
                data = json.load(file)

                for item in data:
                    book = Book(
                        item["title"],
                        item["author"],
                        item["isbn"],
                        item["available"]
                    )
                    self.books.append(book)

            except json.JSONDecodeError:
                pass

    def statistics(self):
        total = len(self.books)
        available = 0
        borrowed = 0

        for book in self.books:
            if book.available:
                available += 1
            else:
                borrowed += 1

        print("\n------ LIBRARY STATISTICS ------")
        print("Total Books    :", total)
        print("Available      :", available)
        print("Borrowed       :", borrowed)


def menu():
    library = Library()

    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Remove Book")
        print("7. Statistics")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.borrow_book()

        elif choice == "5":
            library.return_book()

        elif choice == "6":
            library.remove_book()

        elif choice == "7":
            library.statistics()

        elif choice == "8":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()

