-- Lists all records of the table second_table
-- Results displays the score and the name sorted by descending score
-- Database name will be passed as an argument to the mysql command
-- Not allowed to use any JOIN or UNION
SELECT score, name FROM second_table WHERE (name IS NOT NULL AND name != '') ORDER BY score DESC;
