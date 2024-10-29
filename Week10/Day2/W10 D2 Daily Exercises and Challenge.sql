-- How to display all the tables with their columns and data types: 

-- SELECT table_name, column_name, data_type
-- FROM information_schema.columns
-- WHERE table_schema = 'movies'
-- ORDER BY table_name, ordinal_position;

-- Task 1: Rank Movies by Popularity within Each Genre
-- Use the RANK() function to rank movies by their popularity within each genre.
-- Display the genre name, movie title, and their rank based on popularity.

SELECT 
    g.genre_name, 
    m.title AS movie_title, 
    RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS popularity_rank
FROM 
    movies.movie m
JOIN 
    movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN 
    movies.genre g ON mg.genre_id = g.genre_id
ORDER BY 
    g.genre_name, popularity_rank;


-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company

-- Use the NTILE() function to divide the movies produced by each production company into quartiles based on revenue.
-- Display the company name, movie title, revenue, and quartile.
-- ME: Let's solve this using CTE instead of joins (probably subq is not best practice but joins)

WITH movie_revenue_cte AS (
    SELECT 
        pc.company_name, 
        m.title AS movie_title, 
        m.revenue
    FROM 
        movies.movie m
    JOIN 
        movies.movie_company mc ON m.movie_id = mc.movie_id
    JOIN 
        movies.production_company pc ON mc.company_id = pc.company_id
    WHERE 
        m.revenue IS NOT NULL  -- to exclude movies without revenue data
)
SELECT 
    company_name, 
    movie_title, 
    revenue, 
    NTILE(4) OVER (PARTITION BY company_name ORDER BY revenue DESC) AS revenue_quartile
FROM 
    movie_revenue_cte
ORDER BY 
    company_name, revenue_quartile;


-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre

-- Use the SUM() function to calculate the running total of movie budgets within each genre.
-- Display the genre name, movie title, budget, and running total budget.

SELECT 
    g.genre_name, 
    m.title AS movie_title, 
    m.budget, 
    SUM(m.budget) OVER (PARTITION BY g.genre_name ORDER BY m.title ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total_budget
FROM 
    movies.movie m
JOIN 
    movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN 
    movies.genre g ON mg.genre_id = g.genre_id
WHERE 
    m.budget IS NOT NULL


-- Task 4: Identify the Most Recent Movie for Each Genre

-- Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date.
-- Display the genre name, movie title, and release date.

SELECT 
    g.genre_name, 
    FIRST_VALUE(m.title) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS most_recent_movie_title,
    FIRST_VALUE(m.release_date) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS most_recent_release_date
FROM 
    movies.movie m
JOIN 
    movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN 
    movies.genre g ON mg.genre_id = g.genre_id
WHERE 
    m.release_date IS NOT NULL
ORDER BY 
    g.genre_name;

-- Exercise 2: Cast and Crew Performance Analysis
-- Task 1: Rank Actors by Their Appearance in Movies

-- Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in.
-- Display the actor’s name and their rank.


SELECT 
    actor_name,
    movie_count,
    DENSE_RANK() OVER (ORDER BY movie_count DESC) AS rank
FROM (
    SELECT 
        p.person_name AS actor_name,
        COUNT(mc.movie_id) AS movie_count
    FROM 
        movies.person p
    JOIN 
        movies.movie_cast mc ON p.person_id = mc.person_id
    GROUP BY 
        p.person_name
) AS actor_movie_counts
ORDER BY 
    rank;


-- Task 2: Identify the Top Director by Average Movie Rating

-- Use a CTE and the RANK() function to find the director with the highest average movie rating.
-- Display the director’s name and their average rating.


WITH DirectorRatings AS (
	SELECT
		p.person_name AS director_name, 
		AVG(m.vote_average) AS average_rating
	    FROM 
        movies.person p
    JOIN 
        movies.movie_crew mc ON p.person_id = mc.person_id
    JOIN 
        movies.movie m ON mc.movie_id = m.movie_id
    WHERE 
        mc.job = 'Director'  -- Ensure we are only considering directors
        AND m.vote_average IS NOT NULL  -- Ignore movies without ratings
    GROUP BY 
        p.person_name
)
SELECT 
    director_name,
    average_rating,
    RANK() OVER (ORDER BY average_rating DESC) AS rank
FROM 
    DirectorRatings
ORDER BY 
    rank

-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor

-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor.
-- Display the actor’s name and the cumulative revenue.

WITH ActorRevenue AS (
    SELECT 
        p.person_name AS actor_name,
        SUM(m.revenue) AS total_revenue
    FROM 
        movies.person p
    JOIN 
        movies.movie_cast mc ON p.person_id = mc.person_id
    JOIN 
        movies.movie m ON mc.movie_id = m.movie_id
    WHERE 
        m.revenue IS NOT NULL  -- Exclude movies with no revenue data
    GROUP BY 
        p.person_name
)
SELECT 
    actor_name,
    total_revenue
FROM 
    ActorRevenue
ORDER BY 
    total_revenue DESC;

-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget

-- Use a CTE and a window function to find the director whose movies have the highest total budget.
-- Display the director’s name and the total budget.


WITH DirectorBudgets AS (
	SELECT
		p.person_name as director_name,
		SUM(m.budget) AS total_budget
	FROM
		movies.person p
	JOIN
		movies.movie_crew mc ON p.person_id = mc.person_id
	JOIN
		movies.movie m ON mc.movie_id = m.movie_id
	WHERE 
		mc.job = 'Director'
		AND m.budget IS NOT NULL -- exclude movies with no budget - null values
	GROUP BY
		p.person_name
)

SELECT
	director_name,
	total_budget
FROM (
	SELECT 
		director_name,
		total_budget,
		RANK() OVER (ORDER BY total_budget DESC) as RANK
	FROM
		DirectorBudgets
		
) ranked_directors
WHERE
	rank = 1;













	

-- DAILY CHALLENGE--------------------------------------------------------------------------------------------------
-- Task 1: Calculate the Average Budget Growth Rate for Each Production Company
-- Calculate the average budget growth rate for each production company across all movies they have produced. 
-- Use window functions to determine the budget growth rate and then calculate the average growth rate.





WITH BudgetGrowthRates AS (
    SELECT 
        pc.company_name,
        m.title AS movie_title,
        m.budget AS current_budget,
        LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date) AS previous_budget,
        CASE 
            WHEN LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date) IS NOT NULL 
                 AND LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date) != 0
            THEN (m.budget - LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date)) / 
                 LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date) * 100
            ELSE NULL
        END AS budget_growth_rate
    FROM 
        movies.movie m
    JOIN 
        movies.movie_company mc ON m.movie_id = mc.movie_id
    JOIN 
        movies.production_company pc ON mc.company_id = pc.company_id
    WHERE 
        m.budget IS NOT NULL
)
SELECT 
    company_name,
    ROUND(AVG(budget_growth_rate), 2) AS average_growth_rate  -- Rounding the result to 2 decimal places
FROM 
    BudgetGrowthRates
WHERE 
    budget_growth_rate IS NOT NULL
GROUP BY 
    company_name
ORDER BY 
    average_growth_rate DESC;


-- 🌟 Task 2: Determine the Most Consistently High-Rated Actor
-- Identify the actor who has appeared in the most movies that are rated above the average rating of all movies.
-- Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.

-- Step 1: Calculate the average rating of all movies
WITH AvgMovieRating AS (
    SELECT AVG(m.vote_average) AS avg_rating
    FROM movies.movie m
),

-- Step 2: Identify movies that have ratings above the average rating
HighRatedMovies AS (
    SELECT m.movie_id, m.title, m.vote_average
    FROM movies.movie m, AvgMovieRating
    WHERE m.vote_average > AvgMovieRating.avg_rating
),

-- Step 3: Count how many high-rated movies each actor has appeared in
ActorHighRatedMovies AS (
    SELECT 
        p.person_name AS actor_name,
        COUNT(hrm.movie_id) AS high_rated_movie_count
    FROM 
        movies.person p
    JOIN 
        movies.movie_cast mc ON p.person_id = mc.person_id
    JOIN 
        HighRatedMovies hrm ON mc.movie_id = hrm.movie_id
    GROUP BY 
        p.person_name
)

-- Step 4: Rank actors by their number of high-rated movies and return the top one
SELECT 
    actor_name,
    high_rated_movie_count
FROM 
    ActorHighRatedMovies
ORDER BY 
    high_rated_movie_count DESC
LIMIT 1;


-- 🌟 Task 3: Calculate the Rolling Average Revenue for Each Genre
-- Calculate the rolling average revenue for movies within each genre, considering only the last three movies released in the genre.
-- Use window functions with the ROWS frame specification to achieve this.

SELECT
	g.genre_name, 
	m.title AS movie_title,
	m.release_date,
	m.revenue,
    ROUND(
        AVG(m.revenue) OVER (
            PARTITION BY g.genre_name
            ORDER BY m.release_date
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ), 2 -- Rounding to 2 decimal places
    ) AS rolling_avg_revenue
	
FROM
	movies.movie m
JOIN
	movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN
	movies.genre g ON mg.genre_id = g.genre_id

WHERE 
    m.revenue IS NOT NULL  -- This excludes NULL values
	AND m.revenue > 0  -- Exclude zero values
ORDER BY 
    g.genre_name, m.release_date;

-- 🌟 Task 4: Identify the Highest-Grossing Movie Series
-- Identify the movie series (based on shared keywords) with the highest total revenue.
-- Use window functions and CTEs to group movies by their series and calculate the total revenue.

-- 1. Using CTE to calculate total revenue for each series (grouped by keyword)
WITH SeriesRevenue AS (
    SELECT 
        k.keyword_name AS series_name,
        SUM(m.revenue) AS total_revenue
    FROM 
        movies.movie m
    JOIN 
        movies.movie_keywords mk ON m.movie_id = mk.movie_id
    JOIN 
        movies.keyword k ON mk.keyword_id = k.keyword_id
    WHERE 
        m.revenue IS NOT NULL
    GROUP BY 
        k.keyword_name
),

-- Step 2: Rank the series by total revenue - another CTE refferencing the first CTE

RankedSeries AS (
	SELECT
		series_name,
		total_revenue,
		RANK() OVER (ORDER BY total_revenue DESC) AS revenue_rank
	FROM
		SeriesRevenue
)

-- Step 3: Select the series with the highest total revenue, stepping outside CTEs

SELECT
	series_name,
	total_revenue,
	revenue_rank
FROM 
	RankedSeries





























