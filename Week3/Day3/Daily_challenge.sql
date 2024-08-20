
-- CREATE TABLE customer2 (
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE customer_profile (
--     id SERIAL PRIMARY KEY,
--     isLoggedIn BOOLEAN DEFAULT FALSE,
--     customer_id INT UNIQUE REFERENCES customer2(id) ON DELETE CASCADE
-- );

-- -- Insert customers
-- INSERT INTO customer2 (first_name, last_name)
-- VALUES 
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');


-- Insert profiles with subqueries for customer_id
-- INSERT INTO customer_profile (isLoggedIn, customer_id)
-- VALUES 
-- (TRUE, (SELECT id FROM customer2 WHERE first_name = 'John')),
-- (FALSE, (SELECT id FROM customer2 WHERE first_name = 'Jerome'));

-- SELECT customer2.first_name 
-- FROM customer2
-- INNER JOIN customer_profile 
--     ON customer2.id = customer_profile.customer_id
-- WHERE customer_profile.isLoggedIn = TRUE;

-- SELECT 
--     customer2.first_name, 
--     customer_profile.isLoggedIn 
	
-- FROM 
--     customer2
-- LEFT JOIN 
--     customer_profile 
-- ON 
--     customer2.id = customer_profile.customer_id;


-- SELECT COUNT (*)
-- FROM customer2
-- LEFT JOIN customer_profile
-- ON customer2.id = customer_profile.customer_id
-- WHERE customer_profile.isloggedin = FALSE;


-- CREATE TABLE Book (
--     book_id SERIAL PRIMARY KEY,
--     title VARCHAR(255) NOT NULL,
--     author VARCHAR(255) NOT NULL
-- );

-- INSERT INTO Book (title, author)
-- VALUES
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To Kill a Mockingbird', 'Harper Lee');

-- CREATE TABLE Student (
--     student_id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL UNIQUE,
--     age INT CHECK (age <= 15)
-- );

-- INSERT INTO Student (name, age) 
-- VALUES 
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);


-- CREATE TABLE Library (
--     book_fk_id INT,
--     student_fk_id INT,
--     borrowed_date DATE,
--     PRIMARY KEY (book_fk_id, student_fk_id),
--     FOREIGN KEY (book_fk_id) REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     FOREIGN KEY (student_fk_id) REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
-- );

-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES 
--     ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--      (SELECT student_id FROM Student WHERE name = 'John'),
--      '2022-02-15'),
     
--     ((SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'),
--      (SELECT student_id FROM Student WHERE name = 'Bob'),
--      '2021-03-03'),
     
--     ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--      (SELECT student_id FROM Student WHERE name = 'Lera'),
--      '2021-05-23'),
     
--     ((SELECT book_id FROM Book WHERE title = 'Harry Potter'),
--      (SELECT student_id FROM Student WHERE name = 'Bob'),
--      '2021-08-12');

-- SELECT * FROM Library;

-- SELECT Student.name, Book.title, Library.borrowed_date

-- FROM Library  
-- INNER JOIN Student ON Library.student_fk_id = Student.student_id
-- INNER JOIN Book on Library.book_fk_id = Book.book_id;

-- SELECT AVG(Student.age) AS average_age
-- FROM Library
-- INNER JOIN Student ON Library.student_fk_id = Student.student_id
-- INNER JOIN Book ON Library.book_fk_id = Book.book_id
-- WHERE Book.title = 'Alice In Wonderland';


-- DELETE FROM Student
-- WHERE student_id = 1;
-- CASCADE DELETE HAPPENED FROM LIBRARY









































