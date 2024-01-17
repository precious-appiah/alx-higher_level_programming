-- return 
SELECT score, COUNT(*) as count_of_occurrences
FROM second_table
GROUP BY number
HAVING COUNT(*) > 1;
