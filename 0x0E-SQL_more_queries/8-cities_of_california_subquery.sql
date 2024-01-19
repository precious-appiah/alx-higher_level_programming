--looking for an item when we only know the name 
SELECT * FROM cities WHERE id =(
    SELECT id FROM states where name = 'California';
);
