-- lists all shows, and all genres linked to that show
-- use only one SELECT statement
-- results must be sorted in ascending order by tv_shows.title
-- database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_genres.name FROM tv_genres
RIGHT OUTER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
RIGHT OUTER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC;
