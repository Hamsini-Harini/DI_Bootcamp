-- -- -- -- -- -- CREATE TABLE colors (
-- -- -- -- -- -- color_id SERIAL PRIMARY KEY,
-- -- -- -- -- -- color_name VARCHAR (50)
-- -- -- -- -- -- );

-- -- -- -- -- INSERT into colors (color_name)
-- -- -- -- -- VALUES ('Red'), ('Blue'),('Green'), ('Yellow');

-- -- -- -- CREATE TABLE cars_restrict (
-- -- -- -- car_id SERIAL PRIMARY KEY, 
-- -- -- -- car_name VARCHAR (50),
-- -- -- -- car_color_id INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT
-- -- -- -- )

-- -- -- INSERT INTO cars_restrict (car_name, car_color_id)
-- -- -- VALUES
-- -- -- 	('Toyota', 1),
-- -- -- 	('Ford', 2),
-- -- -- 	('Honda',3),
-- -- -- 	('Mazda',2);


-- -- DELETE FROM colors
-- -- WHERE color_id = 2; -- error we tried to delete referenced foreign key 

-- -- INSERT INTO colors (color_name)
-- -- VALUES 
-- -- 	('Purple') -- ID is 5


-- DELETE FROM colors
-- WHERE color_id = 5; -- we can delete column from parent that is not referenced by child

--OPTION 2 - ON DELETE CASCADE (opposite of restrict - you can delete from parent but that will cascade deletion in child table)
-- creating new child table and deleting previous 
-- the code down is a bit sloppy you can fix if needed but no need

-- CREATE TABLE cars_cascade (
-- VALUES
-- 	car_id SERIAL PRIMARY KEY, 
-- 	car_name VARCHAR (50),
-- 	car_color_id INTEGER REFERENCES colors (color_id) ON DELETE CASCADE
-- );

-- INSERT INTO cars_cascade (car_name, car_color_id)
-- SET
-- 	('Toyota', 1),
-- 	('Ford', 2),
-- 	('Honda',3),
-- 	('Mazda',2);

----------- ON DELETE SET DEFAULT OPTION
-- CREATE TABLE cars_set_default (
--     car_id SERIAL PRIMARY KEY,
--     car_name TEXT,
--     car_color INTEGER DEFAULT 1 REFERENCES colors (color_id) 
--         ON DELETE SET DEFAULT 
--         ON UPDATE SET DEFAULT
-- );

-- INSERT INTO cars_set_default (car_name, car_color) 
-- VALUES 
--     ('Toyota', 1),
--     ('Ford', 2),
--     ('Honda', 3),
--     ('Mazda', 2);

-- DELETE FROM colors WHERE color_id = 2;





