-- SELECT name as list_of languages FROM language; 

-- SELECT 
--     film.title, 
--     film.description, 
--     language.name AS language_name
-- FROM 
--     film
-- INNER JOIN 
--     language ON film.language_id = language.language_id;

-- SELECT
-- 	film.title, 
-- 	film.description,
-- 	language.name as language_name
-- FROM
-- 	language
-- LEFT JOIN film 
-- ON film.language_id = language.language_id;

-- CREATE TABLE new_film (
-- id SERIAL PRIMARY KEY, 
-- name VARCHAR (54) NOT NULL 
-- );

-- INSERT INTO new_film (name)
-- VALUES
--     ('Inception'),
--     ('Interstellar'),
--     ('The Dark Knight'),
--     ('The Matrix'),
--     ('Pulp Fiction');

-- CREATE TABLE customer_review (
-- 	review_id SERIAL PRIMARY KEY NOT NULL,
-- 	film_id INT, 
-- 	language_id INT, 
-- 	title VARCHAR (244) NOT NULL,
-- 	score INTEGER,
-- 	review_text TEXT, 
-- 	last_update DATE,
-- 	FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE, 
-- 	FOREIGN KEY (language_id) REFERENCES language(language_id)
-- );

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
-- VALUES
--     (1, 1, 'Amazing Visuals', 9, 'Inception has stunning visual effects and a mind-bending plot.', CURRENT_TIMESTAMP),
--     (2, 2, 'Masterpiece', 10, 'Interstellar is a visually striking and emotionally powerful movie.', CURRENT_TIMESTAMP);

-- DELETE FROM new_film WHERE id = 1




-- EXERCISE 2 -----------------------------------------------------------------------------------------------

-- UPDATE language
-- SET name = 'Dutch'
-- WHERE name = 'Spanish';

-- question: 
-- ANSWER The customer table has foreign key references to the store and address tables via store_id and address_id.
-- When inserting data into the customer table, the values for store_id and address_id must exist in the store and address tables.
-- If you try to insert a store_id or address_id that doesn’t exist, PostgreSQL will return a foreign key violation error.

-- before dropping we should check for foreign key refferences, if we are dropping a parent table there might be a  problem, dropping a child table is usually easier and reuires less checks
-- we can use CASCADE here as well 

-- DROP TABLE customer_review CASCADE;

-- SELECT COUNT(*) AS outstanding_rentals
-- FROM rental
-- WHERE return_date IS NULL;

-- SELECT 
--     film.title, 
--     film.rental_rate, 
--     rental.rental_date
-- FROM 
--     rental
-- INNER JOIN 
--     inventory ON rental.inventory_id = inventory.inventory_id
-- INNER JOIN 
--     film ON inventory.film_id = film.film_id
-- WHERE 
--     rental.return_date IS NULL 
-- ORDER BY 
--     film.rental_rate DESC       
-- LIMIT 30;                       

-- SELECT film.title
-- FROM film
-- INNER JOIN film_actor ON film.film_id = film_actor.film_id
-- INNER JOIN actor ON film_actor.actor_id = actor.actor_id
-- WHERE 
--     actor.first_name = 'Penelope' 
--     AND actor.last_name = 'Monroe'
--     AND film.description ILIKE '%sumo%';


-- SELECT 
--     title as R_rated_under_60
-- FROM 
--     film
-- WHERE 
--     rental_duration < 60 
--     AND rating = 'R';

-- SELECT 
--     film.title
-- FROM 
--     rental
-- INNER JOIN 
--     payment ON rental.rental_id = payment.rental_id
-- INNER JOIN 
--     customer ON rental.customer_id = customer.customer_id
-- INNER JOIN 
--     inventory ON rental.inventory_id = inventory.inventory_id
-- INNER JOIN 
--     film ON inventory.film_id = film.film_id
-- WHERE 
--     customer.first_name ILIKE 'Matthew'
--     AND customer.last_name ILIKE 'Mahan'
--     AND payment.amount > 4.00
--     AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01';

SELECT 
    film.title
FROM 
    rental
INNER JOIN 
    customer ON rental.customer_id = customer.customer_id
INNER JOIN 
    inventory ON rental.inventory_id = inventory.inventory_id
INNER JOIN 
    film ON inventory.film_id = film.film_id
WHERE 
    customer.first_name ILIKE 'Matthew'
    AND customer.last_name ILIKE 'Mahan'
    AND (film.title ILIKE '%boat%' OR film.description ILIKE '%boat%')
    AND film.replacement_cost = (
        SELECT MAX(replacement_cost) 
        FROM film
    );

-- NOTE TO CHECKER - NOT SURE WHY NO OUTPUT HERE in my last querry 















































