-- Creating a simple library database system
DROP DATABASE IF EXISTS my_library;
CREATE DATABASE my_library;
USE my_library;


-- Books
CREATE TABLE Books (
book_isbn VARCHAR(20) PRIMARY KEY,
book_title VARCHAR(255) NOT NULL
);

-- Authors
CREATE TABLE Authors (
author_id INT PRIMARY KEY AUTO_INCREMENT,
author_name VARCHAR(255) NOT NULL
);

-- Borrowers
CREATE TABLE Borrowers(
borrowers_id INT PRIMARY KEY AUTO_INCREMENT,
borrowers_name VARCHAR(255) NOT NULL
);

-- BooksAuthors
CREATE TABLE BooksAuthors(
book_isbn VARCHAR(20),
author_id INT,
PRIMARY KEY (book_isbn, author_id),
FOREIGN KEY (book_isbn) REFERENCES Books(book_isbn) ON DELETE CASCADE,
FOREIGN KEY (author_id) REFERENCES Authors(author_id) ON DELETE CASCADE 
);

-- BooksBorrowers
CREATE TABLE BooksBorrowers(
borrow_id INT PRIMARY KEY AUTO_INCREMENT,
book_isbn VARCHAR(20),
borrowers_id INT,
borrow_date DATE,
return_date DATE,
FOREIGN KEY (book_isbn) REFERENCES Books(book_isbn) ON DELETE CASCADE,
FOREIGN KEY (borrowers_id) REFERENCES Borrowers(borrowers_id) ON DELETE CASCADE
);
