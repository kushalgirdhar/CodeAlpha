import mysql.connector
from datetime import date

conn = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Root@@3131",
  database="library"
)

cursor=conn.cursor()

def add_book(title, author, copies):
    query="INSERT INTO books(title,author,copies) VALUES (%s,%s,%s)"
    cursor.execute(query,(title,author,copies))
    conn.commit()
    print("Book added successfully")

def update_book(book_id,title,author,copies):
    query="UPDATE books SET title=%s, author=%s, copies=%s, WHERE id=%s"
    cursor.execute(query,(title,author,copies,book_id))
    conn.commit()
    print("Book updated successfully")

def delete_book(book_id):
    query="DELETE FROM books Where id=%s"
    cursor.execute(query,(book_id,))
    conn.commit()
    print("Book deleted successfully")

def search_book(keyword):
    query="SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
    cursor.execute(query,(f"%{keyword}%",f"%{keyword}%"))
    results=cursor.fetchall()
    if results:
        print("\n search Results: ")
        for row in results:
            print(row)
    else:
        print("No book found")


def issue_book(book_id,student_name):
    cursor.execute("SELECT copies FROM books WHERE id=%s",(book_id))
    result=cursor.fetchone()
    if result and result[0]>0:
        cursor.execute("UPDATE books SET copies=copies-1 WHERE id=%s",(book_id))
        query="INSERT INTO issued_books(book_id,student_name,issue_date) VALUES (%s, %s, %s)"
        cursor.execute(query,(book_id,student_name,date.today()))
        conn.commit()
        print("BOOK issued successfully")
    else:
        print("BOOK not available")

def return_book(issue_id):
    cursor.execute("SELECT book_id FROM issued_books WHERE id=%s",(issue_id,))
    result=cursor.fetchone()
    if result:
        book_id=result[0]
        cursor.execute("UPDATE books SET copies=copies+1 WHERE id=%s",(book_id,))
        cursor.execute("UPDATE issued_books SET return_date=%s WHERE id=%s",(date.today(),issue_id))
        conn.commit()
        print("BOOK returned successfully")
    else:
        print("INVALID issue ID")


while True:
    print("---Library Menu---")
    print("1. ADD BOOK")
    print("2. UPDATE BOOK")
    print("3. DELETE BOOK")
    print("4. SEARCH BOOK")
    print("5. ISSUE BOOK")
    print("6. RETURN BOOK")
    print("7. Exit")

    choice=input("Enter choice: ")

    if choice=="1":
        title=input("Enter title: ")
        author=input("Enter author: ")
        copies=int(input("Enter number of copies: "))
        add_book(title,author,copies)
    elif choice=="2":
        book_id=int(input("Enter book ID: "))
        title= input("Enter new title: ")
        author=input()
        copies=int(input("Enter new number of copies: "))
        update_book(book_id, title,author,copies)
    elif choice=="3":
        book_id=int(input("Enter book ID to delete: "))
        delete_book(book_id)
    elif choice=="4":
        keyword=input("Enter keyword to search: ")
        search_book(keyword)
    elif choice=="5":
        book_id=int(input("Enter book ID to issue: "))
        student_name=input("Enter student name: ")
        issue_book(book_id,student_name)
    elif choice=="6":
        issue_id =int(input("Enter issue ID to return: "))
        return_book(issue_id)
    elif choice=="7":
        print("Exiting... Goodbye TATAAAA.....")
        break
    else:
        print("Invalid choice, try again...")

        