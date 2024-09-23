def add_book(library, new_book):
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} is already in the library.")
    else:
        library.append(new_book)
        print(f"Added '{new_book[0]}' by {new_book[1]} to the library.")

# Existing Library Data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Example usage
new_books = [("1984", "George Orwell"), ("To Kill a Mockingbird", "Harper Lee")]

for book in new_books:
    add_book(library, book)

# Display the updated library
print("\nUpdated Library:")
for book in library:
    print(f"'{book[0]}' by {book[1]}")
