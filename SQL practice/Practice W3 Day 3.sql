-- INSERT INTO actors (actor_id, first_name, last_name, age, number_oscars)
-- VALUES
-- (1, 'Leonardo', 'DiCaprio', '1974-11-11', 1),
-- (2, 'Meryl', 'Streep', '1949-06-22', 3),
-- (3, 'Brad', 'Pitt', '1963-12-18', 2),
-- (4, 'Denzel', 'Washington', '1954-12-28', 2),
-- (5, 'Cate', 'Blanchett', '1969-05-14', 2),
-- (6, 'Tom', 'Hanks', '1956-07-09', 2),
-- (7, 'Jennifer', 'Lawrence', '1990-08-15', 1),
-- (8, 'Morgan', 'Freeman', '1937-06-01', 1);

-- CREATE TABLE scenarios (
--     pk_movie_id INTEGER NOT NULL,
--     scenario_story TEXT NOT NULL,
--     PRIMARY KEY (pk_movie_id),
--     CONSTRAINT fk_movie_id FOREIGN KEY (pk_movie_id) REFERENCES movies (movie_id)
-- );

-- ONE TO MANY

-- CREATE TABLE directors (
--   director_id SERIAL,
--   first_name VARCHAR(30) NOT NULL,
--   last_name VARCHAR(30) NOT NULL,
--   PRIMARY KEY (director_id)
-- );

/*
 one to many: A director directs many movies
*/

-- CREATE TABLE movies (
--   movie_id SERIAL,
--   movie_title VARCHAR(45) NOT NULL,
--   released_date date NOT NULL,
--   fk_director_id INTEGER NOT NULL,
--   PRIMARY KEY (movie_id),
--   FOREIGN KEY (fk_director_id) REFERENCES directors(director_id) ON DELETE CASCADE
-- );

-- CREATE TABLE actors_movies (
--   actor_id INTEGER NOT NULL,
--   movie_id INTEGER NOT NULL,
--   actor_role VARCHAR(30) NOT NULL,
--   is_lead_role BOOLEAN NOT NULL,
--   PRIMARY KEY (actor_id, movie_id),
--   FOREIGN KEY (actor_id) REFERENCES actors(actor_id) ON UPDATE CASCADE,
--   FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON UPDATE CASCADE
-- );

















