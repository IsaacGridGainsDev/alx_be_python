DROP DATABASE IF EXISTS Students_Info;
CREATE DATABASE Students_Info;
USE Students_Info;

CREATE TABLE Students (
	StudentID INT AUTO_INCREMENT PRIMARY KEY,
	FirstName VARCHAR(50) NOT NULL,
	LastName VARCHAR(50) NOT NULL,
	Email VARCHAR(100) UNIQUE,
	EnrollmentDate DATE
);

CREATE TABLE Orders (
	OrderID INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
	StudentID INT,
	OrderDate DATE,
	Total INT,
	FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO Students VALUES (1, 'Jacob', 'Millins', 'jake@ea.org.us', '2021-05-04'), (2, 'Favor', 'Amarachi', 'favamarachi@ea.org.ng', '2020-09-09'), (3, 'Abubakar', 'Suleiman', 'abuleiman@ea.org.ng', '2020-09-09');

INSERT INTO Orders VALUES (1, 1, '2025-08-14', 300), (2, 2, '2025-08-14', 240), (3, 3, '2025-08-14', 990);

SELECT * FROM Orders;

SELECT
	S.FirstName,
	S.LastName,
	S.Email,
	O.Total
FROM Students AS S
JOIN Orders AS O ON O.StudentID = S.StudentID
WHERE S.FirstName = 'Jacob'; 


