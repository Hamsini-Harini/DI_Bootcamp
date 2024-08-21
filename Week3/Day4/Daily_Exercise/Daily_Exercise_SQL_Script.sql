-- CREATE TABLE Menu_Items (
-- 	item_id SERIAL PRIMARY KEY,
-- 	item_name VARCHAR(30) NOT NULL,
-- 	item_price SMALLINT DEFAULT 0
-- );

-- INSERT INTO Menu_Items (item_name, item_price) VALUES ('Pizza', 15);
-- INSERT INTO Menu_Items (item_name, item_price) VALUES ('Pasta', 12);
-- INSERT INTO Menu_Items (item_name, item_price) VALUES ('Salad', 8);
-- INSERT INTO Menu_Items (item_name, item_price) VALUES ('Sushi', 20);
-- INSERT INTO Menu_Items (item_name, item_price) VALUES ('Tacos', 10);
-- INSERT INTO Menu_Items (item_name, item_price) VALUES ('Steak', 25);

DELETE FROM Menu_Items
WHERE item_name = 'Burger'
AND item_id NOT IN (
    SELECT MIN(item_id)
    FROM Menu_Items
    WHERE item_name = 'Burger'
);
