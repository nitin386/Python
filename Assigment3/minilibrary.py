#Mini Library System

FILE_NAME = "library.txt"


class Book:
    def _init_(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display(self):
        """Return formatted string of book details."""
        return f"{self.title:<30} {self.author:<20} {self.isbn:<15} {self.status:<10}"

    def to_record(self):
        """Convert book to comma-separated values for saving to file."""
        return f"{self.title},{self.author},{self.isbn},{self.status}\n"

    def from_record(line):
        """Create Book object from a single line of file."""
        parts = line.strip().split(",")
        if len(parts) != 4:
            return None  # invalid line
        title, author, isbn, status = parts
        return Book(title, author, isbn, status)


# ---------------- Core operations on the library list ---------------- #

def add_book(library):
    print("\n--- Add New Book ---")
    title = input("Enter book title  : ").strip()
    author = input("Enter author name : ").strip()
    isbn = input("Enter ISBN        : ").strip()

    new_book = Book(title, author, isbn)
    library.append(new_book)
    print("Book added successfully!")


def search_book(library):
    print("\n--- Search Book ---")
    print("1. Search by Title")
    print("2. Search by ISBN")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        key = input("Enter title to search: ").strip().lower()
        results = [book for book in library if key in book.title.lower()]
    elif choice == "2":
        key = input("Enter ISBN to search : ").strip()
        results = [book for book in library if book.isbn == key]
    else:
        print("Invalid choice.")
        return

    if not results:
        print("No matching book found.")
    else:
        print("\nSearch Results:")
        print_header()
        for book in results:
            print(book.display())


def remove_book(library):
    print("\n--- Remove Book ---")
    isbn = input("Enter ISBN of book to remove: ").strip()

    for i, book in enumerate(library):
        if book.isbn == isbn:
            print("Book found and removed:")
            print_header()
            print(book.display())
            del library[i]
            return

    print("Book with given ISBN not found.")


def display_all_books(library):
    print("\n--- All Books in Library ---")
    if not library:
        print("No books in the library.")
        return

    print_header()
    for book in library:
        print(book.display())


def print_header():
    print(f"{'Title':<30} {'Author':<20} {'ISBN':<15} {'Status':<10}")
    print("-" * 80)


# ---------------- File Handling functions ---------------- #

def save_to_file(library, filename=FILE_NAME):
    print("\n--- Save Records to File ---")
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for book in library:
                f.write(book.to_record())
        print(f"All records saved to '{filename}'.")
    except IOError as e:
        print("Error while saving to file:", e)


def load_from_file(filename=FILE_NAME):
    print("\n--- Load Records from File ---")
    library = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    book = Book.from_record(line)
                    if book is not None:
                        library.append(book)
        print(f"Loaded {len(library)} book(s) from '{filename}'.")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty library.")
    except IOError as e:
        print("Error while reading file:", e)
    return library


# ---------------- Menu-Driven Interface ---------------- #

def main():
    library = []

    while True:
        print("\n===== Mini Library System =====")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Remove Book")
        print("4. Display All Books")
        print("5. Save Records to File")
        print("6. Load Records from File")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            search_book(library)
        elif choice == "3":
            remove_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            save_to_file(library)
        elif choice == "6":
            library = load_from_file()
        elif choice == "0":
            print("Exiting Mini Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if _name_ == "_main_":
    main()
