# User Management System

This project is a **User Management System** developed using Flask (Python), focusing on CRUD (Create, Read, Update, Delete) operations. It allows users to add, delete, modify, and retrieve user credentials like Name, Age, and City.

## Project Details

- **Project Name**: User Management System
- **Developer**: SRIVIKAS M
- **Internship**: First Internship as a Python Developer
- **Database**: MySQL (MySQL Workbench)

## Features

- **Add User**: Add new user credentials.
- **Delete User**: Remove existing user credentials.
- **Update User**: Modify existing user credentials.
- **Retrieve User**: View user credentials.

## Technologies Used

- **Flask**: Python web framework.
- **MySQL Workbench**: Database management.

## Installation and Setup

### Prerequisites

- Python 3.x (I used 3.9.6)
- Flask
- MySQL

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Srivi24/User-Management-System.git
    cd user-management-system
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    - Open MySQL Workbench and execute the following commands:

    ```sql
    SHOW DATABASES;
    CREATE DATABASE crud;
    USE crud;
    CREATE TABLE users (
        ID INTEGER AUTO_INCREMENT PRIMARY KEY,
        NAME VARCHAR(25),
        AGE INTEGER CHECK (AGE > 12),
        CITY VARCHAR(50)
    );
    SHOW TABLES;
    DESC users;
    SELECT * FROM users;
    ```

5. **Run the application**:
    ```bash
    flask run
    ```

## MySQL Commands

Below are the MySQL commands used to create and manage the database:

```sql
SHOW DATABASES;
CREATE DATABASE crud;
USE crud;
CREATE TABLE users (
    ID INTEGER AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(25),
    AGE INTEGER CHECK (AGE > 12),
    CITY VARCHAR(50)
);
SHOW TABLES;
DESC users;
SELECT * FROM users;
