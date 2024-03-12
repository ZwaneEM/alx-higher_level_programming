-- lists all genres from the database and
-- display the number of shows linked to each
SELECT genre AS genre,
       COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY genre
ORDER BY number_of_shows DESC;
