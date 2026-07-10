# Library Management System

A command-line **Library Management System** built with **Python** using **Object-Oriented Programming (OOP)** and **JSON** for persistent data storage. This project allows users to manage a collection of books by adding, searching, borrowing, returning, and removing books through an interactive menu.

---

## Features

* Add new books
* Search books by title or author
* View all books
* Borrow books
* Return borrowed books
* Remove books
* Display library statistics
* Automatic data saving with JSON
* Automatic data loading on startup
* Prevents duplicate ISBN entries

---

## Built With

* Python 3
* Object-Oriented Programming (Classes & Objects)
* JSON
* File Handling
* Standard Python Libraries (`json`, `os`)

---

## Project Structure

```text
Library-Management-System/
│
├── library.py        # Main application
├── books.json        # Stores library data (created automatically)
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/zaidaraino11-max/Library-system.git
```

### 2. Navigate to the project directory

```bash
cd Library-Management-System
```

### 3. Run the application

```bash
python library.py
```

> **Note:** Make sure Python 3 is installed on your computer before running the program.

---

## Menu

```text
========== LIBRARY MANAGEMENT SYSTEM ==========

1. Add Book
2. View All Books
3. Search Book
4. Borrow Book
5. Return Book
6. Remove Book
7. Statistics
8. Exit
```

---

## Data Storage

Book information is stored in a local `books.json` file.

Example:

```json
[
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "isbn": "9780735211292",
        "available": true
    }
]
```

The data is automatically updated whenever changes are made.

---

## Concepts Demonstrated

This project demonstrates:

* Object-Oriented Programming (OOP)
* Classes and Objects
* Constructors (`__init__`)
* Lists of Objects
* Functions and Methods
* Loops
* Conditional Statements
* File Handling
* JSON Serialization
* Exception Handling

---

## Future Improvements

* User authentication
* Borrow due dates
* Late return fines
* Book categories
* Search by ISBN
* Sorting and filtering
* GUI using Tkinter
* SQLite/MySQL database support
* Flask web application
* Barcode scanner integration

---

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License.

---

## Author

**Zaid Ahmed**

If you found this project useful, consider starring the repository.
