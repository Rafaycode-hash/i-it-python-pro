import os

# Function to load library from file
def load_library(file_name="library.txt"):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            library = [eval(line.strip()) for line in file.readlines()]
        return library
    return []

# Function to save library to a file
def save_library(library, file_name="library.txt"):
    with open(file_name, "w") as file:
        for book in library:
            file.write(str(book) + "\n")

# Function to add a book to the library
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"

    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read_status
    }
    library.append(book)
    print(f"Book '{title}' added to the library.")

# Function to remove a book from the library
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            print(f"Book '{title}' removed from the library.")
            return
    print("Book not found!")

# Function to search for a book by title or author
def search_book(library):
    search_term = input("Enter a book title or author to search: ").lower()
    results = [book for book in library if search_term in book["Title"].lower() or search_term in book["Author"].lower()]
    if results:
        print("\nFound books:")
        for book in results:
            print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year']}, Genre: {book['Genre']}, Read: {'Yes' if book['Read'] else 'No'}")
    else:
        print("No books found.")

# Function to display all books in the library
def display_books(library):
    if library:
        print("\nLibrary:")
        for book in library:
            print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year']}, Genre: {book['Genre']}, Read: {'Yes' if book['Read'] else 'No'}")
    else:
        print("No books in the library.")

# Function to display statistics about the library
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books to show statistics.")
    else:
        read_books = len([book for book in library if book["Read"]])
        percentage_read = (read_books / total_books) * 100
        print(f"\nTotal books: {total_books}")
        print(f"Books read: {read_books}")
        print(f"Percentage read: {percentage_read:.2f}%")

# Main function to handle the menu
def main():
    library = load_library()
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
