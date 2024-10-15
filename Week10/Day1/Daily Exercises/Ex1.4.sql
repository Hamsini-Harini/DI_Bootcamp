-- Step 1: Create a temporary table with all competitors for analysis
CREATE TEMPORARY TABLE competitor_analysis AS
SELECT DISTINCT p.id, p.full_name
FROM person p;

-- Step 2: Delete competitors who have not won any medals
DELETE FROM competitor_analysis
WHERE id NOT IN (
    SELECT ce.competitor_id
    FROM competitor_event ce
    WHERE ce.medal_id IN (
        SELECT m.id
        FROM medal m
        WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
    )
);
