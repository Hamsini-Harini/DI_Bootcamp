
-- guessing the outputs

-- 1 - will return IDs 5 ,6 and 7 

-- 2 -  the query will count 3 rows (ids 6, 7, and NULL) and return 3

-- 3 - no rows will satisfy the NOT IN condition - you cant comapre anything to NULL, and the output will be 0.

-- 4 - I expect IDs 6 and 7 to be returned and probably NULL as well 