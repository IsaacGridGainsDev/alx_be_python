
-- Create tables
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10, 2)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50)
);

-- Insert sample data
INSERT INTO Customers (CustomerID, FirstName, LastName, Email) VALUES
(1, 'Alice', 'Smith', 'alice@example.com'),
(2, 'Bob', 'Johnson', 'bob@example.com'),
(3, 'Carol', 'Davis', 'carol@example.com');

INSERT INTO Products (ProductID, ProductName, Price) VALUES
(1, 'Laptop', 1200.00),
(2, 'Mouse', 25.00),
(3, 'Keyboard', 75.00);

INSERT INTO Orders (OrderID, CustomerID, OrderDate, Status) VALUES
(1, 1, '2023-02-15', 'Shipped'),
(2, 2, '2022-12-20', 'Pending'),
(3, 1, '2023-04-05', 'Shipped');

INSERT INTO Employees (EmployeeID, FirstName, LastName, Department) VALUES
(1, 'John', 'Miller', 'Sales'),
(2, 'Sarah', 'Brown', 'HR'),
(3, 'David', 'Wilson', 'Sales'),
(4, 'Emma', 'Clark', 'IT');

-- Solutions

-- Q1: Retrieve the names and email addresses of all customers
SELECT FirstName, LastName, Email FROM Customers;

-- Q2: Select product names and prices where the price is greater than $50
SELECT ProductName, Price FROM Products WHERE Price > 50;

-- Q3: Orders placed after Jan 1, 2023, with 'Shipped' status
SELECT * FROM Orders WHERE OrderDate > '2023-01-01' AND Status = 'Shipped';

-- Q4: Products with price greater than the average price
SELECT * FROM Products WHERE Price > (SELECT AVG(Price) FROM Products);

-- Q5: Total number of employees in each department
SELECT Department, COUNT(*) FROM Employees GROUP BY Department;
