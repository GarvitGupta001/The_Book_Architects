CREATE DATABASE Library;
USE LIBRARY;
CREATE TABLE BOOK(
    Book_id VARCHAR(10) PRIMARY KEY,
    Author_id VARCHAR(10) NOT NULL,
    Book_Title VARCHAR(80) NOT NULL,
    Publisher_id VARCHAR(10) NOT NULL,
    Vendor_id VARCHAR(10) NOT NULL,
    Shelf_id varchar(10) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    Price float NOT NULL, 
    Language_name VARCHAR(50) NOT NULL,  
    Subject_name VARCHAR(50) NOT NULL,
    Genre VARCHAR(50) NOT NULL,
    Date_of_publishing date NOT NULL,
    Date_of_addition date NOT NULL,
    Availability int NOT NULL,
    Shelf_date date NOT NULL,
    Bought_on date NOT NULL,
    foreign key (Author_id) references Author(Author_id),
    foreign key (Publisher_id) references Publisher(Publisher_id),
    foreign key (Vendor_Id) references Vendor(Vendor_id),
    foreign key (Shelf_id) references Shelf(Shelf_id)
);

Create Table Author(
    Author_id Varchar(10) Primary Key,
    Author_name varchar(50) NOT NULL
);

CREATE TABLE Publisher(
    Publisher_id Varchar(10) Primary Key,
    Publisher_name varchar(50) NOT NULL
);

CREATE TABLE Vendor(
    Vendor_id VARCHAR(10),
    Vendor_name VARCHAR(50)
);

CREATE TABLE Shelf(
    Shelf_id VARCHAR(10) PRIMARY KEY,
    Quantity INT PRIMARY KEY,
    Shelf_floor INT NOT NULL,
    Shelf_rows INT NOT NULL,
    Shelf_cols INT NOT NULL
);

CREATE TABLE EMPLOYEE(
    Employee_id VARCHAR(10) PRIMARY KEY,
    Employee_name VARCHAR(50) NOT NULL,
    Employee_email VARCHAR(50) NOT NULL,
    Employee_phone INT NOT NULL,
    Gender Varchar(10) NOT NULL,
    Date_of_Birth date NOT NULL,
    Date_of_joining date NOT NULL
);

CREATE TABLE Member(
    Member_id Varchar(10) NOT NULL,
    Member_name VARCHAR(50) NOT NULL,
    Member_Type Varchar(50) NOT NULL,
    Date_of_birth date NOT NULL,
    Date_of_joining date NOT NULL,
    Member_course VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL, 
    State VARCHAR(50) NOT NULL, 
    City VARCHAR(50) NOT NULL,
    Street INT  
	);
    
CREATE TABLE Fine(
    Fine_id VARCHAR(10) primary key,
    Amount float NOT NULL,
    Days_Delay date NOT NULL,
    Member_id VARCHAR(10) NOT NULL,
    foreign key (Member_id) References Member(Member_id)
);

CREATE TABLE Book_Issue(
    Issue_id VARCHAR(10) Primary Key,
    Issue_date datetime NOT NULL,
    Employee_id Varchar(10) NOT NULL,
    Member_id VARCHAR(10) NOT NULL,
    Book_id VARCHAR(10) NOT NULL,
    foreign key (Employee_id) references Employee(employee_id),
    foreign key (Member_id) references Member(Member_id),
    foreign key (Book_id) references Book(Book_id)
);
CREATE TABLE Book_Return(
    Return_id VARCHAR(10) Primary Key,
    Return_date datetime NOT NULL,
    Employee_id Varchar(10) NOT NULL,
    Member_id VARCHAR(10) NOT NULL,
    Book_id VARCHAR(10) NOT NULL,
    foreign key (Employee_id) references Employee(employee_id),
    foreign key (Member_id) references Member(Member_id),
    foreign key (Book_id) references Book(Book_id)
);

