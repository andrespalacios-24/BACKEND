
1. Asociar los generos "Comedia", "Acción" y "Ciencia Ficción" a la película "Avatar".
-- realizado por mi menos seguro ya que si te falta una coma y demas falla la busqueda
-- tambien son muchas lineas
USE cineDB;
INSERT INTO movie_genre (movie_id, genre_id)
VALUES 
((SELECT movie_id FROM cineDB.movies WHERE title= 'Avatar'),
(SELECT genre_id FROM cineDB.genres WHERE genre_name= 'Comedia')),
((SELECT movie_id FROM cineDB.movies WHERE title= 'Avatar'),
(SELECT genre_id FROM cineDB.genres WHERE genre_name= 'Accion')),
((SELECT movie_id FROM cineDB.movies WHERE title= 'Avatar'),
(SELECT genre_id FROM cineDB.genres WHERE genre_name= 'Ciencia Ficcion'))
-- realizado por mouredev, mas practico y seguro buscar primeros los id,
-- asi se asegura que existen y no se preocupa por tildes y demas
SELECT movie_id FROM movies WHERE title = 'Avatar'; 
SELECT genre_id, genre_name FROM genres WHERE genre_name IN ('Comedia', 'Acción', 'Ciencia Ficción'); 
-- se hace la consulta y despues con las id, se insertan 
INSERT INTO movie_genre (movie_id, genre_id) VALUES (19, 8), (19, 2), (19, 1);

2. Relaciona a los actores Sam Worthington y Al Pacino con la película "Avatar".

SELECT movie_id FROM cineDB.movies WHERE title = 'Avatar'; 
SELECT people_id, name FROM cineDB.people WHERE name IN ('Sam Worthington', 'Al Pacino')
USE cineDB;
INSERT INTO movie_actor (movie_id, actor_id)
VALUES (19,74), (19,2);

3. Utilizando Subqueries, cambia el genero "Comedia" por "Aventura" en la película "Avatar".

USE cineDB;
UPDATE movie_genre 
SET genre_id= (SELECT genre_id FROM genres WHERE genre_name ='Aventura')
WHERE movie_id = (SELECT movie_id FROM movies WHERE title= 'Avatar')
AND genre_id = (SELECT genre_id FROM genres WHERE genre_name = 'Comedia');


4. Utilizando Subqueries, elimina al actor Al Pacino de la película "Avatar".

USE cineDB;
DELETE FROM movie_actor 
WHERE movie_id =(SELECT movie_id FROM movies WHERE title = 'Avatar')
AND actor_id =(SELECT people_id FROM people WHERE name= 'Al pacino');

5. Trata de eliminar "Avatar" de la tabla peliculas. Revisa que sucede. 
-- asi da un error distinto: el error es por utilizar subquery en la misma tabla
 USE cineDB;
DELETE FROM movies WHERE movie_id= (SELECT movie_id FROM movies WHERE title= 'Avatar');
-- el error esperado: no deja eliminar porque aun hay relaciones conectadas a esta pelicula
DELETE FROM movies WHERE title = 'Avatar';

6. Elimina todas las relaciones de la película "Avatar" (actores y generos).

USE cineDB;
DELETE FROM movie_actor WHERE movie_id = (SELECT movie_id FROM movies WHERE title = 'Avatar');
DELETE FROM movie_genre WHERE movie_id = (SELECT movie_id FROM movies WHERE title = 'Avatar');

7. Trata de eliminar nuevamente "Avatar" de la tabla peliculas.

DELETE FROM movies WHERE title = 'Avatar';
-- ahora si lo elimino ya que se eliminaron primero las relaciones que tenia

8. Utilizando Subqueries, elimina la relación de los géneros "Infantil" y "Animación" de todas las películas.

DELETE FROM movie_genre 
WHERE genre_id IN (
SELECT genre_id FROM genres WHERE genre_name IN ('Infantil', 'Animación')
);

9. Elimina todas las películas que no tengan actores y géneros asociados.

USE cineDB;
SET SQL_SAFE_UPDATES = 0; --se hace para desactivar el modo seguro. se debe activar inmediatamente
DELETE FROM movies
WHERE movie_id NOT IN (SELECT DISTINCT movie_id FROM movie_genre)
AND  movie_id NOT IN (SELECT DISTINCT movie_id FROM movie_actor);
SET SQL_SAFE_UPDATES = 1; -- activar de nuevo el modo seguro

10. Inserta 2 reviews para la película "Gladiator" y 1 review para la película "Titanic".
-- consultando el id
USE cineDB;
INSERT INTO movie_review (movie_id,review_text, review_timestamp)
VALUES (16,'perrona la pelicula, la verdad','2026-06-06 17:54:30'),
	   (16,'malita la pelicula, pero bueno','2026-06-06 17:57:00'),
       (6, 'muy pero muy malita','2026-06-06 17:59:50' );

-- sin consultar el id sino solo con el nombre
INSERT INTO movie_review (movie_id,review_text, review_timestamp)
VALUES (
(SELECT movie_id FROM movies WHERE title = 'Gladiator'),
'perrona la pelicula, la verdad','2026-06-06 17:54:30'
);

11. Inserta 3 reviews para la película "The Matrix" sin ingresar la fecha y hora de la review.

USE cineDB;
INSERT INTO movie_review (movie_id,review_text)
VALUES (18, 'mala, todo culpa de serpe'),
	   (18, 'la mejor, gracias a serpe'),
       (18, 'ni buena ni mala, firmes con serpe');

12. Inserta los siguientes premios:
    - Oscar Mejor Película
	- Oscar Mejor Director
    - Oscar Mejor Actor
    - Globo de Oro Mejor Película
    - Globo de Oro Mejor Director
    - Globo de Oro Mejor Actor

USE cineDB;
INSERT INTO awards (award_name)
VALUES 
('Oscar Mejor Película'),
('Oscar Mejor Director'),
('Oscar Mejor Actor'),
('Globo de Oro Mejor Película'),
('Globo de Oro Mejor Director'),
('Globo de Oro Mejor Actor');

13. Asocia los siguientes premios a las películas:
	- Oscar Mejor Película:
		- Gladiator
		- Schindler’s List
		- Titanic
        - The Godfather
		- Alien
	- Oscar Mejor Director:
		- Titanic
        - The Matrix
    - Oscar Mejor Actor:
		- Barbie
        - Jurassic Park
	- Globo de Oro Mejor Película:
		- Fight Club
		- Gladiator
    - Globo de Oro Mejor Director:
		- The Dark Knight
		- Gladiator
		- Edward Scissorhands
    - Globo de Oro Mejor Actor:
		- The Irishman
		- Alien

		USE cineDB;
INSERT INTO movie_award (movie_id, award_id)
VALUES (17,1),
(7,1),(16,1),(13,1),(6,1),
(6,2),(18,2),
(10,3),(5,3),
(15,4),(16,4),
(8,5),(16,5),(11,5),
(7,6),(3,6);
