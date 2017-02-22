-- Lists the number of records with the same score in the table second_table
-- Result displays score and number of records for this score as number
-- List should be sorted by the number of records (descending)
-- Database name will be passed as an argument to the mysql command
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
