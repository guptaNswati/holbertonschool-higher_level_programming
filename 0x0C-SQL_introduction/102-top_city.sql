SOURCE ./temperatures.sql;
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = '7' AND '8' GROUP BY city ORDER BY avg_temp DESC limit 3;
