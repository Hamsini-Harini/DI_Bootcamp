UPDATE person
SET height = (
    SELECT AVG(p2.height)
    FROM person p2
    JOIN person_region pr2 ON p2.id = pr2.person_id
    WHERE pr2.region_id = (
        SELECT pr1.region_id
        FROM person_region pr1
        WHERE pr1.person_id = person.id
    )
)
WHERE height IS NULL;
