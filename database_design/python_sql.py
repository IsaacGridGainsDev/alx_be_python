import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pword",
        database="my_library"
    )

    if mydb.is_connected():
        print(f"Connected to MySQL Server version: {mydb.get_server_info()}")
        
        mycursor = mydb.cursor()
        
        # Query to get books with their authors
        BooksAuthors = """SELECT B.book_title, A.author_name, booksauthors.author_id 
                         FROM Books B 
                         JOIN booksauthors ON B.book_isbn = booksauthors.book_isbn 
                         JOIN Authors A ON booksauthors.author_id = A.author_id"""
        
        mycursor.execute(BooksAuthors)
        result = mycursor.fetchall()
        
        print("\nBooks and Authors:")
        print("-" * 50)
        for row in result:
            print(f"Book: {row[0]}, Author: {row[1]}, Author ID: {row[2]}")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close database connections
    if 'mycursor' in locals() and mycursor:
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("\nMySQL connection is closed")
