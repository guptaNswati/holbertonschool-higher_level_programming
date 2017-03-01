-- lists all shows except comedy
-- results must be sorted in ascending order by tv_shows.title
-- database name will be passed as an argument of the mysql command
SELECT tv_shows.title FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE NOT tv_genres.name='Comedy' ORDER BY tv_shows.title ASC;
