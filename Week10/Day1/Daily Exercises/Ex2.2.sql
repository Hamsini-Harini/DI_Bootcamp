-- Step 1: Create a temporary table to store the results
CREATE TEMPORARY TABLE competitor_multi_event AS
SELECT ce.competitor_id, COUNT(ce.event_id) AS total_events, ce.games_id
FROM competitor_event ce
WHERE ce.competitor_id IN (
    -- Step 2: Subquery to filter competitors who participated in more than one event in the same games
    SELECT competitor_id
    FROM competitor_event
    GROUP BY competitor_id, games_id
    HAVING COUNT(DISTINCT event_id) > 1
)
GROUP BY ce.competitor_id, ce.games_id;

-- Step 3: Query the temporary table to show results
SELECT * FROM competitor_multi_event;
