import mysql.connector
from datetime import date

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Root@@3131",
    database="library"
)

cursor = conn.cursor()


# Add Book
def add_book(title, author, copies):
    query = "INSERT INTO books(title, author, copies) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, author, copies))
    conn.commit()
    print("✅ Book added successfully")


# Update Book
def update_book(book_id, title, author, copies):
    query = "UPDATE books SET title=%s, author=%s, copies=%s WHERE id=%s"
    cursor.execute(query, (title, author, copies, book_id))
    conn.commit()
    print("✅ Book updated successfully")


# Delete Book
def delete_book(book_id):
    query = "DELETE FROM books WHERE id=%s"
    cursor.execute(query, (book_id,))
    conn.commit()
    print("✅ Book deleted successfully")


# Search Book
def search_book(keyword):
    query = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
    cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
    results = cursor.fetchall()

    if results:
        print("\n📚 Search Results:")
        print("-" * 50)
        for row in results:
            print(
                f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Copies: {row[3]}")
    else:
        print("❌ No book found")


# Display All Books
def display_books():
    query = "SELECT * FROM books"
    cursor.execute(query)
    books = cursor.fetchall()

    if books:
        print("\n📚 Available Books:")
        print("-" * 60)
        for book in books:
            print(
                f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Copies: {book[3]}")
    else:
        print("❌ No books available")


# Issue Book
def issue_book(book_id, student_name):
    cursor.execute(
        "SELECT copies FROM books WHERE id=%s",
        (book_id,)
    )

    result = cursor.fetchone()

    if result and result[0] > 0:

        cursor.execute(
            "UPDATE books SET copies=copies-1 WHERE id=%s",
            (book_id,)
        )

        query = """
        INSERT INTO issued_books
        (book_id, student_name, issue_date)
        VALUES (%s, %s, %s)
        """

        cursor.execute(
            query,
            (book_id, student_name, date.today())
        )

        conn.commit()
        print("✅ Book issued successfully")

    else:
        print("❌ Book not available")


# Return Book
def return_book(issue_id):

    cursor.execute(
        "SELECT book_id FROM issued_books WHERE id=%s",
        (issue_id,)
    )

    result = cursor.fetchone()

    if result:

        book_id = result[0]

        cursor.execute(
            "UPDATE books SET copies=copies+1 WHERE id=%s",
            (book_id,)
        )

        cursor.execute(
            "UPDATE issued_books SET return_date=%s WHERE id=%s",
            (date.today(), issue_id)
        )

        conn.commit()
        print("✅ Book returned successfully")

    else:
        print("❌ Invalid Issue ID")


# View Issued Books
def view_issued_books():
    query = """
    SELECT id, book_id, student_name,
           issue_date, return_date
    FROM issued_books
    """

    cursor.execute(query)
    records = cursor.fetchall()

    if records:
        print("\n📖 Issued Books:")
        print("-" * 70)

        for row in records:
            print(
                f"Issue ID: {row[0]}, "
                f"Book ID: {row[1]}, "
                f"Student: {row[2]}, "
                f"Issue Date: {row[3]}, "
                f"Return Date: {row[4]}"
            )
    else:
        print("❌ No issued books found")


# Main Menu
while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. Search Book")
    print("5. Display All Books")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. View Issued Books")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        copies = int(input("Enter number of copies: "))

        add_book(title, author, copies)

    elif choice == "2":

        book_id = int(input("Enter book ID: "))
        title = input("Enter new title: ")
        author = input("Enter new author: ")
        copies = int(input("Enter new copies: "))

        update_book(book_id, title, author, copies)

    elif choice == "3":

        book_id = int(input("Enter book ID to delete: "))
        delete_book(book_id)

    elif choice == "4":

        keyword = input("Enter title or author keyword: ")
        search_book(keyword)

    elif choice == "5":

        display_books()

    elif choice == "6":

        book_id = int(input("Enter book ID to issue: "))
        student_name = input("Enter student name: ")

        issue_book(book_id, student_name)

    elif choice == "7":

        issue_id = int(input("Enter issue ID to return: "))
        return_book(issue_id)

    elif choice == "8":

        view_issued_books()

    elif choice == "9":

        print("👋 Exiting Library Management System...")
        break

    else:
        print("❌ Invalid choice. Try again.")


# Close Connection
cursor.close()
conn.close()