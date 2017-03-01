-- lists all shows contained in  hbtn_0d_tvshows that have at least one genre linked
-- use only one SELECT statement
-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_show.title, tv_show_genres.genre_id ASC;
