1. Crear una vista llamada "vw_movie" con la siguiente información de todas las películas:
   	- ID de película
    - Nombre de película
    - Año Estreno
    - ID y nombre del director
    - ID y nombre del Estudio 
    - Total de espectadores 
    - Total de recaudación

USE cineDB;
CREATE VIEW vw_movie AS
SELECT m.movie_id AS Pelicula_id, m.title AS nombre, m.release_year AS año_estreno,
 m.director_id AS director_id, p.name AS nombre_director, 
s.studio_id AS estudio_id, s.studio_name AS nombre_estudio,
 m.total_viewers AS total_vistas, m.total_revenue AS ganancia_total
FROM movies m
LEFT JOIN people p ON m.director_id = p.people_id
LEFT JOIN studios s ON m.studio_id = s.studio_id


2. Crear una vista llamada "vw_movie_90" con la siguiente información de todas las películas estrenadas en la década del '90:
   	- ID de película
    - Nombre de película
    - Año Estreno
    - Total de espectadores 
    - Total de recaudación

    USE cineDB;
CREATE VIEW vw_movie_90 AS
SELECT m.movie_id AS Pelicula_id, m.title AS nombre, m.release_year AS año_estreno,
 m.total_viewers AS total_vistas, m.total_revenue AS ganancia_total
FROM movies m
WHERE m.release_year BETWEEN 1990 AND 1999; 

3. Crear una vista llamada "vw_movie_actor" con las películas y sus actores correspondientes.

USE cineDB;
CREATE VIEW vw_movie_actor AS
SELECT title AS titulo, name AS nombre
FROM movies m
INNER JOIN movie_actor ma ON m.movie_id = ma.movie_id
INNER JOIN people p ON ma.actor_id = p.people_id


4. Crear una vista llamada "vw_movie_director" con las películas y su correspondiente director.

USE cineDB;
CREATE VIEW vw_movie_director AS
SELECT title AS titulo, name AS nombre
FROM movies m
INNER JOIN people p ON m.director_id = p.people_id
WHERE p.category= 'Director';


5. Utilizando las vistas creadas en los ejercicios 3 y 4, y la sentencia "UNION", recupera los actores y director de la película "The Matrix":
	- Muestra los encabezados de columna como "Nombre" y "Rol"
    - En la columna "Rol", indica si es Actor o Director. 
    - Ordena los resultados por Nombre.

SELECT nombre AS persona, 'Actor' AS 'Rol'
FROM vw_movie_actor
WHERE titulo= 'The Matrix'
UNION
SELECT nombre AS persona, 'Director' AS 'Rol'
FROM vw_movie_director
WHERE titulo= 'The Matrix'
ORDER BY persona;

--la de mouredev:
SELECT Actor AS Nombre, 'Actor' AS Rol FROM vw_movie_actor WHERE Película = 'The Matrix'
   UNION
   SELECT Director  AS Nombre, 'Director' AS Rol FROM vw_movie_director WHERE Película = 'The Matrix'
   ORDER BY Nombre;


6. Crear cinco procedimientos: 
	- "sp_insert_movie" para insertar una nueva película.
	- "sp_delete_movie" para eliminar una película.
	- "sp_update_release_year" para actualizar el año de estreno de una película.
    - "sp_update_viewers" para actualizar la cantidad de espectadores de una película.
    - "sp_update_revenue" para actualizar la recaudación de una película.

USE cineDB;
DELIMITER //
CREATE PROCEDURE sp_insert_movie(
IN new_title VARCHAR(100),
IN new_release_year INT, 
IN new_director_id INT,
IN new_studio_id INT,
IN new_total_viewers BIGINT,
IN new_total_revenue DECIMAL(15,2)
)
BEGIN
INSERT INTO movies(title, release_year,director_id, studio_id, total_viewers, total_revenue)
VALUES (new_title, new_release_year, new_director_id, new_studio_id, new_total_viewers, new_total_revenue );
END //

CREATE PROCEDURE sp_delete_movie(IN movie_title VARCHAR(100))
BEGIN 
DELETE FROM movies WHERE title = movie_title;
END //

CREATE PROCEDURE sp_update_release_year(IN p_title VARCHAR(150), IN new_release_year INT)
BEGIN 
UPDATE movies
SET release_year= new_release_year
WHERE title = p_title;
END//

CREATE PROCEDURE sp_update_viewers (IN p_title VARCHAR(150), IN new_total_viewers BIGINT)
BEGIN 
UPDATE movies
SET total_viewers= new_total_viewers
WHERE title = p_title;
END//

CREATE PROCEDURE sp_update_revenue (IN p_title VARCHAR(150), IN new_total_revenue DECIMAL(15,2))
BEGIN 
UPDATE movies
SET total_revenue= new_total_revenue
WHERE title = p_title;
END//
DELIMITER ;

7. Crear triggers para registrar inserciones, actualizaciones y eliminaciones en la tabla "movies".
   La información de la operación realizada se registrará en la tabla "audit_log":
	- nombre de la tabla impactada
    - el tipo de operación que se realizó (INSERT, UPDATE, DELETE)
    - el ID del registro impactado
    - el usuario y fecha y hora que se realizó
    - los datos impactados (usando la función JSON_OBJECT() para almacenar los datos previos y nuevos de manera estructurada).	

8. Insertar la película "Avatar" utilizando el procedimiento creado en el ejercicio 6.
    - Nombre: Avatar
    - Año Estreno: 2009
    - ID Director: 6
    - ID Estudio: 6
    - Total Espectadores: 331000000
    - Total Recaudación: 2923706026

9. Utiliza la vista creada en el ejercicio 1 para recuperar la información de las películas "Titanic", "Gladiator" y "Avatar".

10. Utilizando los procedimientos creados en el ejercicio 6:
	- Actualiza a 26000300 la cantidad de espectadores de "The Godfather".
    - Actualiza a 1993 el año de estreno de "Schindler’s List".
    - Actualiza a 95000000.00 la recaudación de "Edward Scissorhands".
    - Elimina la película "Avatar".
    
11. Revisa la tabla de auditoría y chequea que los triggers creados en el ejercicio 7 se ejecutaron correctamente.

12. Crear dos índices, llamados "idx_release_year" e "idx_revenue", en las columnas "release_year" y "total_revenue" de la tabla "movies". 

13. Crear un índice, llamado "idx_movie_actor", compuesto por las columnas "movie_id" y "actor_id" de la tabla "movie_actor".

14. Elimina el índice "idx_revenue" creado en el ejercicio 12.

15. Elimina la vista creada en el ejercicio 2.

16. Elimina el procedimiento "sp_update_release_year" creado en el ejercicio 6.

17. Usando "Transacciones", inserta una película con el procedimiento creado en el ejercicio 6 y luego confirma dicha operación. Verifica si la película fue insertada.

18. Usando "Transacciones", inserta una película con el procedimiento creado en el ejercicio 6 y luego vuelve atrás dicha operación. Verifica si la película fue insertada.

NOTA: para los ejercicios 17 y 18 asegúrate de tener la opción "Auto-Commit Transactions" (del menú "Query") desactivada.
