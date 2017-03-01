-- lists all genres and displays the number of shows linked to each
-- Don't display a genre that doesn't have any shows linked
-- Don't display a genre that doesn't have any shows linked
-- results must be sorted in descending order by number of shows
-- database name will be passed as an argument of the mysql command
SELECT tv.genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows FROM tv_show_genres 
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY number_shows DESC;
