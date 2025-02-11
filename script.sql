-- Create Database
CREATE DATABASE EmployeeManagement;
cd EmployeeManagement;


-- Create Employees Table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(100) NOT NULL, DepartmentID INT, HireDate DATE,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);


-- Create Departments Table
CREATE TABLE Departments (DepartmentID INT PRIMARY KEY AUTO_INCREMENT, DepartmentName VARCHAR(100) NOT NULL);


-- Create Salaries Table
CREATE TABLE Salaries (
    EmployeeID INT PRIMARY KEY, BaseSalary DECIMAL(10,2), Bonus DECIMAL(10,2), Deductions DECIMAL(10,2), 
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);


-- Insert Sample Data
INSERT INTO Departments (DepartmentName) VALUES ('Frontend'), ('HR'), ('Developer');

INSERT INTO Employees (Name, DepartmentID, HireDate) VALUES 
('Darsh', 1, '2025-01-05'), ('Aswin', 2, '2024-03-10'), ('Pranav', 1, '2023-06-20');

INSERT INTO Salaries (EmployeeID, BaseSalary, Bonus, Deductions) VALUES 
(1, 50000, 5000, 2000), (2, 60000, 4000, 3000), (3, 55000, 4500, 2500);


-- List all employees along with their department names.
SELECT Employees.EmployeeID, Employees.Name, Departments.DepartmentName
FROM Employees JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;


-- Calculate the net salary for each employee using the given formula Net Salary = BaseSalary + Bonus - Deductions.
SELECT e.EmployeeID, e.Name, (s.BaseSalary + s.Bonus - s.Deductions) AS NetSalary
FROM Employees e JOIN Salaries s ON e.EmployeeID = s.EmployeeID;


-- Query to Identify Department with Highest Average Salary
SELECT d.DepartmentName, AVG(s.BaseSalary + s.Bonus - s.Deductions) AS AvgSalary
FROM Employees e JOIN Salaries s ON e.EmployeeID = s.EmployeeID
JOIN Departments d ON e.DepartmentID = d.DepartmentID GROUP BY d.DepartmentName ORDER BY AvgSalary DESC LIMIT 1;



