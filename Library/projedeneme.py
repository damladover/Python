def read_books():
    with open('books.txt', 'r') as file:
        lines = file.readlines()
        books = [line.strip().split(',') for line in lines]
    return books

# Function to read students from file
def read_students():
    with open('students.txt', 'r') as file:
        lines = file.readlines()
        students = [line.strip().split() for line in lines]
    return students

# Function to save books to file
def save_books(books):
    with open('books.txt', 'w') as file:
        for book in books:
            file.write(','.join(book) + '\n')

# Function to save students to file
def save_students(students):
    with open('students.txt', 'w') as file:
        for student in students:
            file.write(' '.join(student) + '\n')

# Function to display menu
def display_menu():
    print("\nMenu:")
    print("1. List all books in the library")
    print("2. List all checked out books")
    print("3. Add a new book")
    print("4. Delete a book")
    print("5. Search a book by ISBN number")
    print("6. Search a book by name")
    print("7. Check out a book to a student")
    print("8. List all students with checked out books")
    print("9. Exit")

# Function to list all books in the library
def list_all_books(books):
    print("All Books in Library:")
    for book in books:
        print(', '.join(book))

# Function to list checked out books
def list_checked_out_books(books):
    print("\nChecked Out Books:")
    for book in books:
        if book[3] == 'T':
            print(', '.join(book))

# Function to add a new book
def add_book(books):
    isbn = input("Enter ISBN number: ")
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    checked = 'F'  # Initially set as False
    books.append([isbn, name, author, checked])
    print("Book added successfully!")

# Function to delete a book
def delete_book(books):
    isbn = input("Enter ISBN number of the book to delete: ")
    for book in books:
        if book[0] == isbn:
            if book[3] == 'T':
                print("Cannot delete. Book is checked out.")
            else:
                books.remove(book)
                print("Book deleted successfully!")
            return
    print("Book not found.")

# Function to search book by ISBN number
def search_book_by_isbn(books):
    isbn = input("Enter ISBN number to search: ")
    found_books = [book for book in books if book[0] == isbn]
    if found_books:
        print("Book(s) with ISBN {}: ".format(isbn))
        for book in found_books:
            print(', '.join(book))
    else:
        print("Book not found.")

# Function to search book by name
def search_book_by_name(books):
    name = input("Enter a keyword to search book by name: ")
    found_books = [book for book in books if name.lower() in book[1].lower()]
    if found_books:
        print("Book(s) with name containing '{}': ".format(name))
        for book in found_books:
            print(', '.join(book))
    else:
        print("Book not found.")

# Function to check out a book to a student
def checkout_book(books, students):
    isbn = input("Enter ISBN number of the book to check out: ")
    student_id = input("Enter student ID: ")
    for book in books:
        if book[0] == isbn:
            if book[3] == 'T':
                print("Book is already checked out.")
                return
            else:
                book[3] = 'T'
                for student in students:
                    if student[0] == student_id:
                        if len(student) == 3:
                            student.append(', '.join(book[1:3]))
                        else:
                            student[-1] += ', ' + ', '.join(book[1:3])
                        print("Book checked out successfully!")
                        return
                print("Student ID not found.")
                return
    print("Book not found.")

# Function to list all students with checked out books
def list_students_with_books(students):
    print("Students with Checked Out Books:")
    for student in students:
        if len(student) > 3:
            print(f"{student[0]} - {student[1]} {student[2]}: {student[3]}")

# Main function
def main():
    books = read_books()
    students = read_students()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_books(books)
        elif choice == '2':
            list_checked_out_books(books)
        elif choice == '3':
            add_book(books)
        elif choice == '4':
            delete_book(books)
        elif choice == '5':
            search_book_by_isbn(books)
        elif choice == '6':
            search_book_by_name(books)
        elif choice == '7':
            checkout_book(books, students)
        elif choice == '8':
            list_students_with_books(students)
        elif choice == '9':
            save_books(books)
            save_students(students)
            print("Changes saved. Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()