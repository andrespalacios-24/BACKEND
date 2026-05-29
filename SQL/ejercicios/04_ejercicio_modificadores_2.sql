

1. Obtener el título y año de estreno de las películas que no fueron lanzadas en 1993, 1999, 2000 y 2017.

SELECT title, release_year FROM cineDB.movies WHERE release_year NOT IN ('1993', '1999', '2000', '2017');

2. Obtener las películas que no tienen año de estreno.

SELECT title, release_year FROM cineDB.movies WHERE release_year IS NULL; 

3. Obtener las películas con estudio cinematográfico asociado.

SELECT title FROM cineDB.movies WHERE studio_id IS NOT NULL; 

4. Obtener los actores sin fecha de nacimiento o identificador de país de nacimiento.

SELECT name FROM cineDB.people WHERE birth_date AND country_of_birth_id IS  NULL; 

5. Obtener los actores sin fecha de nacimiento e identificador de país de nacimiento.

SELECT name, birth_date, country_of_birth_id FROM cineDB.people WHERE (birth_date IS NULL OR country_of_birth_id IS NULL) AND category = 'Actor';

6. Obtener la cantidad total de películas almacenadas en la base de datos. Mostrar el resultado como "Total Peliculas".

SELECT COUNT(*) AS Total_Peliculas FROM cineDB.movies;

7. Calcular el promedio de recaudación de todas las películas.

SELECT AVG(total_revenue) AS 'promedio de ganancias totales' FROM cineDB.movies;

8. Contar cuántas películas se estrenaron por año. Ordenar por año descendente.

SELECT release_year, COUNT(*) as cantidad FROM cineDB.movies GROUP BY release_year ORDER BY release_year DESC; 


9. Obtener las películas cuyo año de estreno está entre 1990 y 1999.

SELECT title, release_year FROM cineDB.movies WHERE release_year BETWEEN 1990 AND 1999;

10. Clasificar las películas según su recaudación, mostrando título, recaudación y clasificación, siguiendo estos criterios:
    - Menor a 500000000, mostrar 'Bajo rendimiento'
    - Entre 100000000 y 500000000, mostrar 'Moderado'
    - Entre 500000000 y 1000000000, mostrar "Éxito"
    - Mayor a 1000000000, mostrar "Éxito masivo"
    - Recaudación nula, mostrar "Sin datos de recaudación"
    - Ordena el resultado alfabéticamente por nombre de película.

SELECT title AS 'Titilo', total_revenue AS 'Recaudacion',
CASE
WHEN total_revenue < 500000000 THEN 'Bajo Rendimiento'
WHEN total_revenue BETWEEN 100000000 AND 500000000 THEN 'Moderado'
WHEN total_revenue BETWEEN 500000000 AND 1000000000 THEN 'Exito'
WHEN total_revenue > 1000000000 THEN 'Exito Masivo'
WHEN total_revenue IS NULL THEN 'Sin datos'
END AS Clasificacion 
FROM cineDB.movies
ORDER BY title;

11. Obtiene el nombre y fecha de nacimiento de cada actor. Muestra el resultado en una única columna llamada "Actores", con formato "Nombre actor (fecha nacimiento)". Descarta los actores sin fecha de nacimiento.

SELECT CONCAT('Nombre de Actor: ',name,'','(Fecha Nacimieto): ', birth_date) AS 'Actores' FROM cineDB.people WHERE birth_date IS NOT NULL;

12. Obtiene el valor mínimo de recaudación (no usar los modificadores ORDER BY y LIMIT).

SELECT MIN(total_revenue) AS 'menor recaudacion' FROM cineDB.movies;

13. Obtiene la cantidad máxima de espectadores (no usar el modificador ORDER BY y LIMIT). 

SELECT MAX(total_viewers) AS 'Cantidad Total Espectadores' FROM cineDB.movies;

14. Obtiene la recaudación total y cantidad total de espectadores de todas las películas. 

SELECT SUM(total_revenue) AS 'Total ganancias', 
SUM(total_viewers) AS 'Total espectadores' FROM cineDB.movies;

15. Obtiene título y año de estreno de las películas. Si no está el año, mostrar "No especificado". Usa los alias "Película" y "Año Estreno". Ordenar por película.

SELECT title AS 'Pelicula',  IFNULL(release_year,'No especificado') AS 'Año de estreno' FROM cineDB.movies ORDER BY title;

16. Mostrar los años en que se estrenaron más de 1 película. Ordena por año de estreno ascendente. 

SELECT  release_year, COUNT(*) AS 'Cantidad peliculas'
FROM cineDB.movies WHERE release_year IS NOT NULL
GROUP BY release_year HAVING COUNT(*) >1
ORDER BY release_year;

17. Obtiene los estudios de cine que han producido películas cuya taquilla supera el promedio de recaudación.

-- de esta manera se muestras los id y los valores superiores al promedio
USE cineDB; SELECT studio_id, SUM(total_revenue) AS 'Ganancia mayor al promedio'
FROM movies WHERE studio_id IS NOT NULL AND total_revenue IS NOT NULL
GROUP BY studio_id
HAVING SUM(total_revenue) > (SELECT AVG(total_revenue) 
FROM movies WHERE total_revenue IS NOT NULL)
-- de esta manera de muestran las peliculas con valores superiores al promedio
SELECT studio_name FROM studios WHERE studio_id IN 
(SELECT studio_id FROM movies WHERE total_revenue > 
(SELECT AVG(total_revenue) FROM movies));

18. Obtiene el año de nacimiento de cada director.

SELECT name, YEAR (birth_date) FROM cineDB.people WHERE birth_date IS NOT NULL AND category='Director'

19. Obtiene los títulos de las películas en mayúsculas y la cantidad de letras de su nombre.

SELECT UPPER(title) AS 'titulo mayuscula',
LENGTH(title)  AS 'cantidad de letras'
FROM cineDB.movies; 

20. Calcula la edad aproximada de cada persona utilizando funciones de fecha.
    - Tener en cuenta solo el año de nacimiento al hacer el cálculo.
    - Excluye las personas sin fecha de nacimiento.
    - Ordena por edad ascendente.

    SELECT name, 
    YEAR(CURDATE()) - YEAR(birth_date) AS 'Edad Aproximada'
    FROM cineDB.people WHERE birth_date IS NOT NULL  ORDER BY birth_date; 