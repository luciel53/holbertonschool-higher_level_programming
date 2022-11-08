-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows

JOIN tv_genres
ON tv_genres.id = tv_shows.id
WHERE tv_genres.name = 'Comedy'

ORDER BY tv_shows.title ASC;
