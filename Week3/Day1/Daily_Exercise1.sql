-- -- -- -- -- -- CREATE Table items (
-- -- -- -- -- -- 	id serial primary key,
-- -- -- -- -- -- 	Furniture varchar(20),
-- -- -- -- -- -- 	Price integer
-- -- -- -- -- -- );

-- -- -- -- -- -- CREATE Table customers (
-- -- -- -- -- -- 	id serial primary key,
-- -- -- -- -- -- 	First_name varchar(20),
-- -- -- -- -- -- 	Last_name varchar(20)
-- -- -- -- -- -- )

-- -- -- -- -- INSERT into customers (first_name, last_name)
-- -- -- -- -- VALUES
-- -- -- -- -- ('Greg', 'Jones'),
-- -- -- -- -- ('Sandra', 'Jones'),
-- -- -- -- -- ('Scott', 'Scott'),
-- -- -- -- -- ('Trevor', 'Green'),
-- -- -- -- -- ('Melanie', 'Johnson');

-- -- -- -- INSERT into items (furniture, price) 
-- -- -- -- VALUES
-- -- -- -- ('Small Desk', 100),
-- -- -- -- ('Large Desk', 300),
-- -- -- -- ('Fan', 80
-- -- -- -- );

-- -- -- SELECT * from items

-- -- -- SELECT * from items price WHERE price > 80;

-- -- -- SELECT * from items price WHERE price <= 300;

-- -- SELECT * from customers WHERE last_name = 'Smith';

-- SELECT * from customers WHERE last_name = 'Jones'

SELECT * from customers WHERE first_name !=  'Scott'






