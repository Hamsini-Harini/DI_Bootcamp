SELECT m.medal_name,
       (SELECT AVG(gc.age)
        FROM competitor_event ce
        JOIN games_competitor gc ON ce.competitor_id = gc.person_id
        WHERE ce.medal_id = m.id
       ) AS avg_age
FROM medal m
WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
GROUP BY m.medal_name;
