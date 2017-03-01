-- lists all shows contained in hbtn_0d_tvshows
-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- show doesn't have a genre, display NULL
-- show doesn't have a genre, display NULL
-- database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_show.title, tv_show_genres.genre_id ASC;
