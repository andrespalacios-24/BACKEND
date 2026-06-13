
1. Obtener las películas que tengan un director asociado. Mostrar el título de la pelicula, el año de estreno y el nombre del director. Ordena por película.

USE cineDB;
SELECT m.title AS pelicula, m.release_year AS estreno, p.name AS director 
FROM movies m
JOIN people p ON m.director_id = p.people_id
ORDER BY m.title

2. Obtener las películas que tengan un estudio asociado. Mostrar el título de la película y el estudio. Ordena por nombre de estudio.

USE cineDB;
SELECT m.title AS pelicula,  s.studio_name AS estudio 
FROM movies m
JOIN studios s ON m.studio_id = s.studio_id
ORDER BY s.studio_name

3. Obtener las películas junto con el estudio que las produjo (tengan o no un estudio asociado), ordenadas por nombre de película.

USE cineDB;
SELECT m.title AS pelicula,  s.studio_name AS estudio 
FROM movies m
LEFT JOIN studios s ON m.studio_id = s.studio_id
ORDER BY m.title

4. Obtener los nombres de los actores y las películas en las que han participado. Ordena por actor y película.

USE cineDB;
SELECT p.name AS nombre, m.title AS titulo
FROM people p
INNER JOIN movie_actor ma ON p.people_id = ma.actor_id
INNER JOIN movies m ON ma.movie_id = m.movie_id
ORDER BY p.name, m.title; 

5. Obtener la lista de las películas con sus géneros asociados. Ordena por película.

USE cineDB;
SELECT m.title AS pelicula, g.genre_name AS genero
FROM movies m
INNER JOIN movie_genre mg ON m.movie_id = mg.movie_id
INNER JOIN genres g ON mg.genre_id = g.genre_id
ORDER BY title

6. Obtener todas las películas de un director específico (por ejemplo, "Christopher Nolan").

USE cineDB;
SELECT m.title AS pelicula, p.name AS nombre
FROM movies m
INNER JOIN people p ON m.director_id = p.people_id
WHERE p.name= 'Christopher Nolan'


7. Obtener los actores que han participado en películas de "Aventura" o "Terror".

USE cineDB;
SELECT DISTINCT p.name AS nombre, m.title AS pelicula
FROM people p
INNER JOIN movie_actor ma ON p.people_id = ma.actor_id
INNER JOIN movies m ON ma.movie_id = m.movie_id
INNER JOIN movie_genre mg ON m.movie_id = mg.movie_id
INNER JOIN genres g ON mg.genre_id = g.genre_id
WHERE g.genre_name IN ('Aventura','Terror')

8. Obtener los estudios de cine y la cantidad de películas producidas por cada uno. Ordenado por cantidad descendente.

USE cineDB;
SELECT s.studio_name AS estudio,
COUNT(m.movie_id) AS total_peliculas
FROM studios s
LEFT JOIN movies m ON s.studio_id = m.studio_id
GROUP BY s.studio_name
ORDER BY total_peliculas DESC;

9. Obtener el total de películas por cada género (incluir los géneros que no tengan películas asociadas).

USE cineDB;
SELECT g.genre_name AS genero,
COUNT(mg.movie_id) AS total_genero
FROM genres g
LEFT JOIN movie_genre mg ON g.genre_id = mg.genre_id
GROUP BY g.genre_name


10. Obtener las películas que ganaron el premio "Oscar" o "Globo de Oro" a "Mejor Película". 
	- Mostrar el nombre de la película, el director, el estudio y año de estreno. 
    - Ten en cuenta que las películas sin director o estudio asociado deben también mostrarse en el resultado.

USE cineDB;
SELECT m.title AS pelicula, p.name AS nombre, s.studio_name AS estudio, m.release_year AS año_estreno,
a.award_name
FROM movies m
INNER JOIN movie_award ma ON m.movie_id = ma.movie_id
INNER JOIN awards a ON ma.award_id = a.award_id
LEFT JOIN people p ON m.director_id = p.people_id
LEFT JOIN studios s ON m.studio_id = s.studio_id
WHERE a.award_name IN ('Globo de Oro Mejor Película','Oscar Mejor Película');

11. Obtiene las películas que tienen reviews, mostrando nombre de la película y cantidad de reviews que tiene.

USE cineDB;
SELECT m.title AS pelicula,
COUNT(mr.movie_id) AS total_criticas
FROM movies m
INNER JOIN movie_review mr ON m.movie_id = mr.movie_id
WHERE mr.review_id IS NOT NULL
GROUP BY m.title


12. Obtiene la suma total de espectadores de películas producidas por "Warner Bros".

USE cineDB;
SELECT s.studio_name AS ESTUDIO,
SUM(m.total_viewers) AS total_espectadores
FROM studios s 
INNER JOIN movies m ON s.studio_id = m.studio_id
WHERE s.studio_name = 'Warner Bros'
GROUP BY s.studio_name

13. Obtener todos los premios de cada película: 
	- Mostrar "nombre premio: título de la película (año estreno)" en la misma columna. 
    - Si el año de estreno es nulo, mostrar "Sin Especificar".
    - Ordenar por película.

USE cineDB;
SELECT 
CONCAT(
a.award_name, '-', 
m.title, '-', 
'(', IFNULL(m.release_year, 'sin especificar'),')' 
) AS 'PREMIOS GANADOS'
FROM awards a 
INNER JOIN movie_award ma ON a.award_id = ma.award_id
INNER JOIN movies m ON ma.movie_id = m.movie_id
ORDER BY title

14. Obtener las películas que obtuvieron más de un premio.  


USE cineDB;
SELECT m.title, COUNT(ma.award_id) AS 'cantidad de premios'
FROM movies m 
INNER JOIN movie_award ma ON m.movie_id = ma.movie_id
GROUP BY m.title
HAVING COUNT(ma.award_id) > 1;

15. Obtener las películas que obtuvieron uno o ningun premio. 

USE cineDB;
SELECT m.title, COUNT(ma.award_id) AS 'cantidad de premios'
FROM movies m 
LEFT JOIN movie_award ma ON m.movie_id = ma.movie_id
GROUP BY m.title
HAVING COUNT(ma.award_id) <= 1;

16. Obtener los actores que participaron en ninguna o dos películas.

USE cineDB;
SELECT p.name, COUNT(ma.movie_id) AS peliculas
FROM people p
LEFT JOIN movie_actor ma ON p.people_id = ma.actor_id
WHERE p.category = 'Actor'
GROUP BY p.people_id
HAVING COUNT(ma.movie_id) = 0 OR COUNT(ma.movie_id) = 2;

17. Obtener las personas que no tienen películas asociadas.

USE cineDB;
SELECT p.name, COUNT(ma.movie_id) AS peliculas
FROM people p
LEFT JOIN movie_actor ma ON p.people_id = ma.actor_id
WHERE p.category = 'Actor'
GROUP BY p.people_id
HAVING COUNT(ma.movie_id) = 0;
-- mejor estructurado y como debe de ser 
SELECT p.name AS 'Actor / Director'
FROM people p
LEFT JOIN movies m ON m.director_id = p.people_id
WHERE p.category = 'Director' AND m.director_id IS NULL
UNION
SELECT p.name AS 'Actor / Director'
FROM people p
LEFT JOIN movie_actor ma ON ma.actor_id = p.people_id
WHERE p.category = 'Actor' AND ma.movie_id IS NULL    
ORDER BY 1;

18. Obtener las reviews de las películas "Gladiator" y "The Matrix".

USE cineDB;
SELECT  mr.review_text AS reseña, m.title AS pelicula
FROM movies m
INNER JOIN movie_review mr ON m.movie_id = mr.movie_id
WHERE m.title IN ('Gladiator','The Matrix');


19. Obtener los nombres de países que no estén asociados a ninguna persona.

USE cineDB;
SELECT  c.country_name AS 'pais sin asociados'
FROM countries c
LEFT JOIN people p ON c.country_id = country_of_birth_id
WHERE country_of_birth_id IS NULL;

20. Obtener el país de nacimiento de todas las personas. Mostrar "No Especificado" si no hay datos. Ordena por nombre.

USE cineDB;
SELECT IFNULL(p.name,'No Especificado' ) AS Nombre, IFNULL(c.country_name, 'No Especificado') AS 'Pais'
FROM  people p
LEFT JOIN countries c ON  country_of_birth_id = c.country_id
ORDER BY p.name