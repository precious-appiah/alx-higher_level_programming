-- list alll record in a table , exceplt values undder name column that is NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
