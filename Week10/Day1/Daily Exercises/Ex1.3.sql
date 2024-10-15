-- Step 1: Create the temporary table
CREATE TEMPORARY TABLE medal_count AS
SELECT ce.competitor_id, COUNT(ce.medal_id) AS total_medals
FROM competitor_event ce
WHERE ce.medal_id IN (
    SELECT m.id FROM medal m
    WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
)
GROUP BY ce.competitor_id;

-- Step 2: Query the temporary table to filter competitors with more than 2 medals
SELECT competitor_id, total_medals
FROM medal_count
WHERE total_medals > 2;
