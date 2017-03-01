-- lists all the cities
-- use only one SELECT statement
-- results must be sorted in ascending order by cities.id
-- database name will be passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name FROM cities
LEFT JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
