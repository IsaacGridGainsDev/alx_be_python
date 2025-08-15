import mysql.connector
from mysql.connector import Error

#writing a function to take book details as input and insert new record  into the books table
def insert_record(cursor, title: str, author:str, ISBN):
	table = input("Enter the table you want to insert the values into: ")
	Query = f"INSERT INTO {table} (title, author, isbn) VALUES (%s, %s, %s)"
	Values = (title, author, ISBN)
	
	cursor.execute(Query, Values)
	print("✅ Record Inserted")

#searching records
def search_record(cursor, title):
	table = input("Enter the table that you want to search through: ")
	Query = f"SELECT * FROM {table} WHERE title = %s"
	cursor.execute(Query, (title,))
	results = cursor.fetchall()
	for row in results:
		print(row) 

#printing out all records
def show_records(cursor):
	table = input("Enter the table you want to list: ")
	cursor.execute(f"SELECT * FROM {table}")
	for row in cursor.fetchall():
		print(row)
#deleting by ID
def delete_record(cursor, record_id):
	table = input("Enter the table you want to delete data off of: ")
	cursor.execute(f"SELECT * FROM {table}")
	for row in cursor.fetchall():
		print(row)
	#record_id = int(input("Enter the ID of the record you want to delete: "))
	cursor.execute(f"DELETE FROM {table} WHERE book_id = %s", (record_id,))
	print("✅ Record deleted")

#cleaning things up for modularity
def main(cursor, connection):
	choice = int(input("""
	1. Show Tables
	2. Insert New Record
	3. Search Records
	4. List Records
	5. Delete Records by ID
	
	Enter choice 1-5: 	
"""))
	match choice:
		case 1:
			cursor.execute("SHOW TABLES")
			print(cursor.fetchall())
		case 2:
			title = input("Enter Title: ")
			author = input("Enter Author: ")
			ISBN = input("Enter ISBN: ")
			insert_record(cursor, title, author, ISBN)
			connection.commit()
		case 3:
			title = input("Enter title you are searching for: ")
			search_record(cursor, title)
		case 4:
			show_records(cursor)
		case 5:
			record_id = int(input("Enter the ID you want to delete: "))
			delete_record(cursor, record_id)
			connection.commit()
		case _:
			print("Error, Re-run program")

#creating a new database
try:
	connection = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "pword"
)
	a_cursor = connection.cursor()
	a_cursor.execute("CREATE DATABASE IF NOT EXISTS library_info")

except Error as e:
	print(f"❌ Error creating Database: {e}")
	
else:
	print(f"✅ Successfully created Database")
finally:
	a_cursor.close()
	connection.close()

#creating the tables
try:
	library_db = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "pword",
		database = "library_info"
)
	b_cursor = library_db.cursor()
	b_cursor.execute("CREATE TABLE IF NOT EXISTS books(book_id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(255), author VARCHAR(255), ISBN VARCHAR(255));")

	print("✅ Table ready")
except Error as e:
	print(f"❌ Error connecting to Database: {e}")
else: 
	main(b_cursor, library_db)
finally:
	b_cursor.close()
	library_db.close()	
