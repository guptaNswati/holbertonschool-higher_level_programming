-- lists all the cities of California found in the database hbtn_0d_usa
-- results must be sorted in ascending order by cities.id
-- Results must be sorted in ascending order by cities.id
-- database name will be passed as an argument of the mysql command
SELECT cities.id, name FROM cities WHERE state_id IN
(SELECT states.id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
