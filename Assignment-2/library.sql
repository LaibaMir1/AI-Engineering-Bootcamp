-- 1. Create the database and use it
CREATE DATABASE library;
USE library;

-- 2. Create the books table
CREATE TABLE books (
    id     INT PRIMARY KEY,
    title  VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    year   INT,
    price  DECIMAL(10, 2)
);

-- 3. Insert 8 books
INSERT INTO books (id, title, author, year, price) VALUES
(1, 'To Kill a Mockingbird', 'Harper Lee', 1960, 450.00),
(2, '1984', 'George Orwell', 1949, 380.00),
(3, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 300.00),
(4, 'Clean Code', 'Robert C. Martin', 2008, 1200.00),
(5, 'The Alchemist', 'Paulo Coelho', 1988, 520.00),
(6, 'Sapiens', 'Yuval Noah Harari', 2011, 850.00),
(7, 'Atomic Habits', 'James Clear', 2018, 650.00),
(8, 'Pride and Prejudice', 'Jane Austen', 1813, 250.00);

-- 4a. Books with price above 500
SELECT * FROM books
WHERE price > 500;

-- 4b. All books sorted by price, highest first
SELECT * FROM books
ORDER BY price DESC;

-- 4c. How many books there are
SELECT COUNT(*) AS total_books FROM books;

-- 5. Update the price of one book (WHERE makes sure only one row changes)
UPDATE books
SET price = 400.00
WHERE id = 2;

-- Check the update
SELECT * FROM books WHERE id = 2;