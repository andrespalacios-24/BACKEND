
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

12. Obtiene la suma total de espectadores de películas producidas por "Warner Bros".

13. Obtener todos los premios de cada película: 
	- Mostrar "nombre premio: título de la película (año estreno)" en la misma columna. 
    - Si el año de estreno es nulo, mostrar "Sin Especificar".
    - Ordenar por película.

14. Obtener las películas que obtuvieron más de un premio.  

15. Obtener las películas que obtuvieron uno o ningun premio. 

16. Obtener los actores que participaron en ninguna o dos películas.

17. Obtener las personas que no tienen películas asociadas.

18. Obtener las reviews de las películas "Gladiator" y "The Matrix".

19. Obtener los nombres de países que no estén asociados a ninguna persona.

20. Obtener el país de nacimiento de todas las personas. Mostrar "No Especificado" si no hay datos. Ordena por nombre.