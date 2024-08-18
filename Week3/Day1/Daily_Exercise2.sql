-- -- -- -- -- -- CREATE TABLE students (
-- -- -- -- -- -- 	id serial primary key, 
-- -- -- -- -- -- 	first_name varchar(50),
-- -- -- -- -- -- 	last_name varchar(50),
-- -- -- -- -- -- 	birth_date date
-- -- -- -- -- -- );

-- -- -- -- -- -- -- SELECT * from students

-- -- -- -- -- INSERT INTO students (first_name, last_name, birth_date) VALUES
-- -- -- -- -- ('Marc', 'Benichou', '1998-02-11'),
-- -- -- -- -- ('Yoan', 'Cohen', '2010-03-12'),
-- -- -- -- -- ('Lea', 'Benichou', '1987-07-27'),
-- -- -- -- -- ('Amelia', 'Dux', '1996-04-07'),
-- -- -- -- -- ('David', 'Grez', '2003-06-14'),
-- -- -- -- -- ('Omer', 'Simpson', '1980-10-03');

-- -- -- -- -- -- INSERT INTO students (first_name, last_name, birth_date) VALUES
-- -- -- -- -- -- ('Alexander', 'DP', '1930-01-01');

-- -- -- -- -- SELECT * from students WHERE last_name = 'Benichou' and first_name = 'Marc' ;

-- -- -- -- -- SELECT * from students WHERE last_name = 'Benichou' OR first_name = 'Marc' ;

-- -- -- -- SELECT * FROM students
-- -- -- -- WHERE first_name ILIKE '%a%' ;

-- -- -- -- SELECT * FROM students
-- -- -- -- WHERE first_name ILIKE 'a%'

-- -- -- SELECT * FROM students
-- -- -- WHERE first_name ILIKE '%a'

-- -- SELECT * FROM students WHERE first_name LIKE '%_a_';

-- SELECT * FROM students 
-- WHERE id = 1 OR id = 3;

SELECT * FROM students
WHERE birth_date >= '2000-01-01';
