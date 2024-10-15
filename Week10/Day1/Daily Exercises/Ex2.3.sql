-- Step 1: Create a temporary table to store the results
CREATE TEMPORARY TABLE competitor_multi_event AS
SELECT ce.competitor_id, COUNT(ce.event_id) AS total_events, gc.games_id
FROM competitor_event ce
JOIN games_competitor gc ON ce.competitor_id = gc.person_id
WHERE ce.competitor_id IN (
    -- Step 2: Subquery to filter competitors who participated in more than one event in the same games
    SELECT ce2.competitor_id
    FROM competitor_event ce2
    JOIN games_competitor gc2 ON ce2.competitor_id = gc2.person_id
    GROUP BY ce2.competitor_id, gc2.games_id
    HAVING COUNT(DISTINCT ce2.event_id) > 1
)
GROUP BY ce.competitor_id, gc.games_id;

-- Step 3: Query the temporary table to show results
SELECT * FROM competitor_multi_event;
