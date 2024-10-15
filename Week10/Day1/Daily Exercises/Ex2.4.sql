-- Step 1: Create a temporary table to track competitors' participation in both Summer and Winter games
CREATE TEMPORARY TABLE competitor_season_participation AS
SELECT gc.person_id AS competitor_id, COUNT(DISTINCT g.season) AS season_count
FROM games_competitor gc
JOIN games g ON gc.games_id = g.id
WHERE g.season IN ('Summer', 'Winter')
GROUP BY gc.person_id
HAVING season_count > 1;

-- Step 2: Query the temporary table to show the competitors who participated in both Summer and Winter games
SELECT * FROM competitor_season_participation;
