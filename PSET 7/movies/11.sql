SELECT title from movies
JOIN ratings ON ratings.movie_id = movies.id
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE people.name = "Chadwick Boseman"
ORDER BY ratings.rating DESC LIMIT 5;