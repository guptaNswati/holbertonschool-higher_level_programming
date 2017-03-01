-- lists all genres not linkde to show Dexter
-- results must be sorted in ascending order by genre name
-- database name will be passed as an argument of the mysql command
SELECT tv_genres.name FROM tv_show_genres
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE NOT tv_shows.title='Dexter' ORDER BY name ASC;
