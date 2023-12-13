Project objectives
1. What's a database?
   - A database is a structured collection of data that is organized and stored in a way that allows for efficient retrieval and manipulation of information. Databases can store various types of data and are used in applications ranging from simple record-keeping systems to complex enterprise systems.

2. What's a relational database?
   - A relational database is a type of database that organizes data into tables with rows and columns. The relationships between tables are established based on common fields, allowing for the retrieval of related information through queries. Examples of relational database management systems (RDBMS) include MySQL, PostgreSQL, and Microsoft SQL Server.

3. What does SQL stand for?
   - SQL stands for Structured Query Language. It is a domain-specific language used for managing and manipulating relational databases. SQL allows users to perform tasks such as querying data, updating data, inserting data, and defining the structure of a database.

4. What's MySQL?
   - MySQL is an open-source relational database management system (RDBMS) that uses SQL. It is widely used for web applications and is known for its reliability, ease of use, and strong community support.

5. How to create a database in MySQL:
   - To create a database in MySQL, you can use the following SQL command:
     ```sql
     CREATE DATABASE database_name;
     ```

6. What does DDL and DML stand for?
   - DDL stands for Data Definition Language, and it includes SQL commands that define and manage the structure of a database, such as creating, altering, and dropping tables.
   - DML stands for Data Manipulation Language, and it includes SQL commands that manipulate the data stored in the database, such as inserting, updating, and deleting records.

7. How to CREATE or ALTER a table:
   - To create a table in MySQL, you can use the following SQL command:
     ```sql
     CREATE TABLE table_name (
       column1 datatype1,
       column2 datatype2,
       ...
     );
     ```
   - To alter a table, you can use the ALTER TABLE statement with various options to add, modify, or drop columns.

8. How to SELECT data from a table:
   - To select data from a table in MySQL, you can use the SELECT statement:
     ```sql
     SELECT column1, column2, ...
     FROM table_name
     WHERE condition;
     ```

9. How to INSERT, UPDATE, or DELETE data:
   - To insert data into a table:
     ```sql
     INSERT INTO table_name (column1, column2, ...)
     VALUES (value1, value2, ...);
     ```
   - To update data:
     ```sql
     UPDATE table_name
     SET column1 = value1, column2 = value2, ...
     WHERE condition;
     ```
   - To delete data:
     ```sql
     DELETE FROM table_name
     WHERE condition;
     ```

10. What are subqueries:
    - Subqueries, or nested queries, are queries embedded within another SQL statement. They can be used to retrieve data to be used by the main query or to perform operations based on the results of another query.

11. How to use MySQL functions:
    - MySQL provides various built-in functions that perform operations on data. Examples include:
      - Mathematical functions (e.g., `SUM`, `AVG`, `MAX`, `MIN`).
      - String functions (e.g., `CONCAT`, `SUBSTRING`, `UPPER`, `LOWER`).
      - Date and time functions (e.g., `NOW`, `DATE_FORMAT`, `TIMESTAMPDIFF`).
      - Aggregate functions (e.g., `COUNT`, `GROUP_CONCAT`).

