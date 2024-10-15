SELECT nr.region_name, COUNT(DISTINCT pr.person_id) AS competitor_count
FROM noc_region nr
JOIN person_region pr ON nr.id = pr.region_id
WHERE pr.person_id IN (
    SELECT ce.competitor_id
    FROM competitor_event ce
    GROUP BY ce.competitor_id
    HAVING COUNT(DISTINCT ce.event_id) > 3
)
GROUP BY nr.region_name
ORDER BY competitor_count DESC
LIMIT 5;
