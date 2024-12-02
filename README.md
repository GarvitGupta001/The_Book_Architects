## The_Book_Architects

### The Library Database Management System
  
This Library Database Management is a comprehensive system designed to efficiently handle the diverse operations of a library. It streamlines the management of records, including the addition, updation and deletion of essential entities like books, authors, vendors, publishers, and library members. The system offers robust features to track and maintain member borrowing history, fine management, and other critical library operations.

The database simplifies the process of managing the library's book collection and ensures smooth handling of overdue fines. Staff members can easily monitor borrowed items, identify overdue materials, and apply fines as needed, providing a seamless experience for both the staff and members.

Additionally, the system supports the maintainance of records for issue and return of books, ensuring efficient handling of book transactions. This functionality includes recording details such as issue dates, return dates, overdue calculations, and the application of fines when necessary. It enables quick verification of the availability of books and ensures members adhere to borrowing policies.

Further more, we've integrated Architect Assist, an AI-powered chatbot to enhance user experience. It helps you search for books, learn about authors, and get personalized recommendations effortlessly! Whether you're looking for a specific title or exploring new genres, Architect Assist is here to guide you every step of the way.

With its user-friendly interface and comprehensive features, this database serves as a one-stop solution for managing the library's resources effectively while improving operational efficiency. 

## Steps to run the app
    [STEP 1] : install all requirements
                    pip install -r requirements.txt

    [STEP 2] : create virtual environment
                    python -m venv venv

    [STEP 3] : activate virtual environment
                    venv\Scripts\activate

    [STEP 4] : initiallise the database 
                    flask db init

    [STEP 5] : migrate the database 
                    flask db migrate

    [STEP 6] : upgrade the database 
                    flask db upgrade

    [Step 7] : run the app 
                    python app.py

                    
## Routes Documentation


This application provides various routes for managing library operations, user interactions, and book transactions. Most routes are self-explanatory and follow standard RESTful principles.

### Available Routes

### User Authentication and Session Management
- **`/login`**  
  Handles user login, validates credentials, and redirects to the home page on success.

- **`/signup`**  
  Allows new users to create an account and redirects to the login page upon success.

- **`/logout`**  
  Logs the current user out and redirects them to the login page.

### User and Dashboard
- **`/home_page`**  
  Displays the home page of the application with allowing the user to search for a book.

- **`/dashboard`**  
  Displays the user's dashboard, allowing profile updates.

### Book Management
- **`/add_book`**  
  Adds a new book to the library database.

- **`/update_book`**  
  Updates the details of an existing book.

- **`/delete_book`**  
  Deletes a book from the library database.

- **`/book_search`**  
  Searches for books based on the query string provided.

- **`/book/<int:book_id>`**  
  Displays detailed information about a specific book by its ID.

- **`/view_location`**  
  Displays the location of a specific book within the library.

### Author, Vendor, and Publisher Management
- **`/add_author`**  
  Adds a new author to the library database.

- **`/update_author`**  
  Updates the details of an existing author.

- **`/delete_author`**  
  Deletes an author from the library database.

- **`/add_vendor`**  
  Adds a new vendor to the system.

- **`/update_vendor`**  
  Updates the details of an existing vendor.

- **`/delete_vendor`**  
  Deletes a vendor from the system.

- **`/add_publisher`**  
  Adds a new publisher to the library database.

- **`/update_publisher`**  
  Updates the details of an existing publisher.

- **`/delete_publisher`**  
  Deletes a publisher from the library database.

### Transaction Management
- **`/add_transaction`**  
  Logs a new transaction into the system.
  
- **`/view_history`**  
  Displays the transaction history for the current user, categorized by user type.

### User Management
- **`/view_all_members`**  
  Displays a list of all registered members.

This documentation serves as an overview of the available routes and their functionalities.

### Packages and their use

- **alembic==1.13.2**: Database migration tool for SQLAlchemy.
- **blinker==1.8.2**: Signals library for event-driven programming in Python.
- **click==8.1.7**: Python package for creating command-line interfaces.
- **Flask==3.0.3**: Lightweight web framework for Python.
- **Flask-Migrate==4.0.7**: Extension for handling Alembic migrations with Flask-SQLAlchemy.
- **Flask-SQLAlchemy==3.1.1**: SQLAlchemy integration for Flask applications.
- **itsdangerous==2.2.0**: Provides cryptographic utilities for securely signing data.
- **Jinja2==3.1.4**: Template engine for Python, used in Flask.
- **Mako==1.3.5**: A Python templating engine similar to Jinja2.
- **MarkupSafe==2.1.5**: Prevents unsafe HTML or XML rendering in Python templates.
- **PyMySQL==1.1.1**: MySQL database connector for Python.
- **python-dotenv==1.0.1**: Loads environment variables from `.env` files into Python applications.
- **SQLAlchemy==2.0.32**: Python SQL toolkit and Object Relational Mapper (ORM).
- **typing_extensions==4.12.2**: Provides backported features from the `typing` module for older Python versions.
- **Werkzeug==3.0.4**: WSGI utility library for Python, used as Flask's HTTP server.
- **Flask-Login==0.6.3**: User session management for Flask applications.



## Team Information

**Team Name**: The Book Architects  

**Team Members**:  
- Jhanvi Nagori - 23293916025  
- Shubhika Sinha - 23293916087  
- Prayas  - 23293916032  
- Garvit Gupta - 23293916021  


