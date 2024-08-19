-- SELECT * FROM items
-- ORDER BY price ASC;

-- SELECT * FROM items
-- WHERE price >= 80
-- ORDER BY price DESC;

-- SELECT item, price
-- FROM items
-- ORDER BY item ASC
-- LIMIT 3;

-- SELECT last_name from customers
-- ORDER BY last_name DESC;


------------------------------------- EXERCISE 2 -------------------------------------  

-- -- SELECT * FROM customer;

-- -- SELECT CONCAT(first_name, ' ', last_name) AS full_name
-- -- -- FROM customer;

-- -- -- SELECT DISTINCT create_date from customer;

-- -- -- SELECT * FROM customer 
-- -- -- ORDER BY first_name DESC;

-- -- SELECT film_id, title, description, release_year, rental_rate
-- -- FROM film
-- -- ORDER BY rental_rate ASC;

-- SELECT address, phone FROM address
-- WHERE district = 'Texas';

-- SELECT *
-- FROM film
-- -- WHERE film_id IN (15, 150);

-- SELECT film_id, title, description, length, rental_rate from film
-- WHERE title ILIKE 'African Egg';

-- SELECT film_id, title, description, length, rental_rate from film
-- WHERE title ILIKE 'Af%';

-- SELECT *
-- FROM payment
-- ORDER BY amount ASC
-- LIMIT 10;

-- SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date
-- FROM customer
-- INNER JOIN payment
-- ON customer.customer_id = payment.customer_id
-- ORDER BY customer.customer_id ASC;

-- SELECT film.film_id, film.title, film.description
-- FROM film
-- LEFT JOIN inventory
-- ON film.film_id = inventory.film_id;

-- SELECT city.city, country.country
-- FROM city
-- INNER JOIN country
-- ON city.country_id = country.country_id;



















