DROP DATABASE IF EXISTS Employee_data;
CREATE DATABASE Employee_data;
USE Employee_data;

CREATE TABLE Employees (
	employee_ID INT PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	department VARCHAR(20) NOT NULL,
	hireDate DATE
);

INSERT INTO Employees(first_name, last_name, department, hireDate) VALUES ('John', 'Mounty', 'Police', '2025-08-13'), ('Jacob', 'Posey', 'Forensics', '2025-08-12');
