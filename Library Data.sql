-- AUTHOR TABLE

INSERT INTO Author (Author_id, Author_name) VALUES
('A001', 'J.K. Rowling'),
('A002', 'George Orwell'),
('A003', 'J.R.R. Tolkien'),
('A004', 'Agatha Christie'),
('A005', 'Mark Twain'),
('A006', 'Leo Tolstoy'),
('A007', 'Jane Austen'),
('A008', 'Charles Dickens'),
('A009', 'Stephen King'),
('A010', 'Ernest Hemingway');


-- PUBLISER TABLE

INSERT INTO Publisher (Publisher_id, Publisher_name) VALUES
('P001', 'Penguin Books'),
('P002', 'HarperCollins'),
('P003', 'Simon & Schuster'),
('P004', 'Random House'),
('P005', 'Macmillan Publishers');

-- VENDOR TABLE

INSERT INTO Vendor (Vendor_id, Vendor_name) VALUES
('V001', 'BookWorld Inc.'),
('V002', 'Library Supplies Co.'),
('V003', 'Global Book Store'),
('V004', 'Classic Books'),
('V005', 'Book Depot');

-- SHELF TABLE

INSERT INTO Shelf (Shelf_id, Quantity, Shelf_floor, Shelf_rows, Shelf_cols) VALUES
('S001', 20, 1, 4, 5),
('S002', 20, 1, 4, 5),
('S003', 20, 2, 4, 5),
('S004', 20, 2, 4, 5),
('S005', 20, 3, 4, 5);

-- EMPOYEE TABLE

INSERT INTO Employee (Employee_id, Employee_name, Employee_email, Employee_phone, Gender, Date_of_Birth, Date_of_joining) VALUES
('E001', 'John Doe', 'john@example.com', 1234567890, 'Male', '1985-01-15', '2010-06-01'),
('E002', 'Emily White', 'emily@example.com', 9876543210, 'Female', '1990-07-21', '2012-04-15'),
('E003', 'Michael Smith', 'michael@example.com', 1234509876, 'Male', '1982-11-10', '2011-08-20'),
('E004', 'Anna Brown', 'anna@example.com', 1478523690, 'Female', '1992-03-19', '2013-01-12'),
('E005', 'James Taylor', 'james@example.com', 9517534568, 'Male', '1987-12-28', '2014-05-22'),
('E006', 'Sarah Johnson', 'sarah@example.com', 8523697410, 'Female', '1995-02-14', '2015-09-30'),
('E007', 'David Wilson', 'david@example.com', 7418529630, 'Male', '1989-06-17', '2016-07-18'),
('E008', 'Laura Clark', 'laura@example.com', 9632587410, 'Female', '1988-09-25', '2017-03-24'),
('E009', 'Daniel King', 'daniel@example.com', 7896541230, 'Male', '1983-05-02', '2018-12-10'),
('E010', 'Sophia Green', 'sophia@example.com', 1597534860, 'Female', '1991-04-07', '2019-11-05');

-- MEMBER TABLE

INSERT INTO Member (Member_id, Member_name, Member_Type, Date_of_birth, Date_of_joining, Member_course, Country, State, City, Street) VALUES
('M001', 'Alice Brown', 'Student', '2000-02-15', '2022-09-01', 'Literature', 'USA', 'California', 'Los Angeles', 101),
('M002', 'Bob Smith', 'Student', '1999-10-08', '2021-08-22', 'History', 'USA', 'Texas', 'Houston', 102),
('M003', 'Charlie Johnson', 'Student', '2001-06-22', '2023-01-15', 'Physics', 'Canada', 'Ontario', 'Toronto', 103),
('M004', 'Diana Clark', 'Researcher', '1995-03-19', '2020-04-10', 'Geology', 'UK', 'London', 'London', 104),
('M005', 'Ethan Lewis', 'Researcher', '1996-09-30', '2019-06-25', 'Biology', 'Australia', 'Sydney', 'Sydney', 105),
('M006', 'Fiona Walker', 'Faculty', '1985-12-11', '2017-02-17', 'Engineering', 'India', 'Delhi', 'New Delhi', 106),
('M007', 'George Harris', 'Faculty', '1988-08-05', '2016-11-08', 'Mathematics', 'Germany', 'Berlin', 'Berlin', 107),
('M008', 'Hannah Adams', 'Student', '2002-01-21', '2023-09-12', 'Art', 'France', 'Paris', 'Paris', 108),
('M009', 'Ian Robinson', 'Student', '1998-11-03', '2022-07-14', 'Chemistry', 'USA', 'New York', 'New York', 109),
('M010', 'Julia Thompson', 'Researcher', '1992-07-14', '2018-05-03', 'Physics', 'South Africa', 'Cape Town', 'Cape Town', 110);


-- FINE TABLE

INSERT INTO Fine (Fine_id, Amount, Days_Delay, Member_id) VALUES
('F001', 5.00, '2024-09-10', 'M001'),
('F002', 10.00, '2024-09-15', 'M002'),
('F003', 7.50, '2024-09-20', 'M003'),
('F004', 15.00, '2024-09-25', 'M004'),
('F005', 2.50, '2024-09-30', 'M005');


-- BOOK TABLE

INSERT INTO Book (Book_id, Author_id, Book_Title, Publisher_id, Vendor_id, Shelf_id, Category, Price, Language_name, Subject_name, Genre, Date_of_publishing, Date_of_addition, Availability, Shelf_date, Bought_on) VALUES
('B001', 'A001', 'Harry Potter and the Sorcerer\'s Stone', 'P001', 'V001', 'S001', 'Fiction', 20.50, 'English', 'Fantasy', 'Adventure', '2000-07-01', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B002', 'A002', '1984', 'P002', 'V002', 'S002', 'Dystopian', 15.75, 'English', 'Political', 'Science Fiction', '1949-06-08', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B003', 'A003', 'The Hobbit', 'P003', 'V003', 'S003', 'Fantasy', 18.00, 'English', 'Adventure', 'High Fantasy', '1937-09-21', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B004', 'A004', 'Murder on the Orient Express', 'P004', 'V004', 'S004', 'Mystery', 12.50, 'English', 'Crime', 'Detective', '1934-01-01', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B005', 'A005', 'The Adventures of Tom Sawyer', 'P001', 'V001', 'S001', 'Classic', 10.00, 'English', 'Adventure', 'Historical', '1876-04-30', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B006', 'A006', 'War and Peace', 'P002', 'V002', 'S002', 'Classic', 25.00, 'Russian', 'Historical', 'Epic', '1869-01-01', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B007', 'A007', 'Pride and Prejudice', 'P003', 'V003', 'S003', 'Classic', 9.50, 'English', 'Romance', 'Drama', '1813-01-28', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B008', 'A008', 'A Tale of Two Cities', 'P004', 'V004', 'S004', 'Classic', 14.00, 'English', 'Historical', 'Drama', '1859-04-30', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B009', 'A009', 'The Shining', 'P005', 'V005', 'S005', 'Horror', 19.99, 'English', 'Thriller', 'Psychological', '1977-01-28', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B010', 'A010', 'The Old Man and the Sea', 'P001', 'V001', 'S001', 'Classic', 12.00, 'English', 'Literature', 'Drama', '1952-09-01', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B011', 'A001', 'Harry Potter and the Chamber of Secrets', 'P002', 'V002', 'S002', 'Fiction', 21.00, 'English', 'Fantasy', 'Adventure', '1998-07-02', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B012', 'A002', 'Animal Farm', 'P003', 'V003', 'S003', 'Dystopian', 12.75, 'English', 'Political', 'Allegory', '1945-08-17', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B013', 'A003', 'The Lord of the Rings: The Fellowship of the Ring', 'P004', 'V004', 'S004', 'Fantasy', 22.50, 'English', 'Adventure', 'High Fantasy', '1954-07-29', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B014', 'A004', 'And Then There Were None', 'P005', 'V005', 'S005', 'Mystery', 16.00, 'English', 'Crime', 'Thriller', '1939-11-06', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B015', 'A005', 'The Prince and the Pauper', 'P001', 'V001', 'S001', 'Classic', 13.50, 'English', 'Adventure', 'Historical', '1881-01-01', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B016', 'A006', 'Anna Karenina', 'P002', 'V002', 'S002', 'Classic', 18.75, 'Russian', 'Romance', 'Tragedy', '1878-01-01', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B017', 'A007', 'Sense and Sensibility', 'P003', 'V003', 'S003', 'Classic', 9.99, 'English', 'Romance', 'Drama', '1811-01-01', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B018', 'A008', 'Great Expectations', 'P004', 'V004', 'S004', 'Classic', 13.99, 'English', 'Literature', 'Drama', '1861-01-01', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B019', 'A009', 'It', 'P005', 'V005', 'S005', 'Horror', 24.99, 'English', 'Thriller', 'Psychological', '1986-09-15', '2024-09-01', 1, '2024-09-01', '2024-08-25'),
('B020', 'A010', 'For Whom the Bell Tolls', 'P001', 'V001', 'S001', 'Classic', 15.50, 'English', 'Literature', 'Historical', '1940-10-21', '2024-09-01', 1, '2024-09-01', '2024-08-25');

-- BOOK ISSUE TABLE

INSERT INTO Book_Issue (Issue_id, Issue_date, Employee_id, Member_id, Book_id) VALUES
('I001', '2024-09-05 10:00:00', 'E001', 'M001', 'B001'),
('I002', '2024-09-06 11:00:00', 'E002', 'M002', 'B002'),
('I003', '2024-09-07 09:30:00', 'E003', 'M003', 'B003'),
('I004', '2024-09-07 14:15:00', 'E004', 'M004', 'B004'),
('I005', '2024-09-08 10:45:00', 'E005', 'M005', 'B005'),
('I006', '2024-09-08 13:00:00', 'E006', 'M006', 'B006'),
('I007', '2024-09-09 11:20:00', 'E007', 'M007', 'B007'),
('I008', '2024-09-09 15:00:00', 'E008', 'M008', 'B008'),
('I009', '2024-09-10 10:30:00', 'E009', 'M009', 'B009'),
('I010', '2024-09-10 12:00:00', 'E010', 'M010', 'B010');

-- BOOK RETURN TABLE

INSERT INTO Book_Return (Return_id, Return_date, Employee_id, Member_id, Book_id) VALUES
('R001', '2024-09-10 12:00:00', 'E001', 'M001', 'B001'),
('R002', '2024-09-11 12:00:00', 'E002', 'M002', 'B002'),
('R003', '2024-09-12 14:30:00', 'E003', 'M003', 'B003'),
('R004', '2024-09-13 10:00:00', 'E004', 'M004', 'B004'),
('R005', '2024-09-14 11:15:00', 'E005', 'M005', 'B005'),
('R006', '2024-09-15 15:45:00', 'E006', 'M006', 'B006'),
('R007', '2024-09-16 09:20:00', 'E007', 'M007', 'B007'),
('R008', '2024-09-17 13:30:00', 'E008', 'M008', 'B008'),
('R009', '2024-09-18 10:50:00', 'E009', 'M009', 'B009'),
('R010', '2024-09-20 12:00:00', 'E010', 'M010', 'B010');




