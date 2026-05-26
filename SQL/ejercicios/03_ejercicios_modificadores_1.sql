1. Obtener el titulo y año de estreno de todas las películas, ordenadas por año de estreno descendente.

SELECT title, release_year FROM cineDB.movies ORDER BY release_year DESC; 

2. Obtener el nombre y fecha de nacimiento de los actores nacidos desde el 01 de enero de 1975.

SELECT name, birth_date FROM people WHERE birth_date >= '1975-01-01' AND category = 'Actor';

3. Obtener los actores cuyo nombre comience con la letra 'B'.

SELECT name FROM people WHERE name LIKE 'B%'

4. Obtener los actores cuyo nombre termine con la letra 'T', ordenados por fecha de nacimiento descendente.

SELECT name FROM people WHERE name LIKE '%T' ORDER BY birth_date DESC;

5. Obtener los directores cuyo nombre contenga las letras 'V' o 'W'.

SELECT name FROM people WHERE (name LIKE '%V%' OR name LIKE '%W%') AND category = 'Director';

6. Obtener los directores cuyo nombre no contenga las letras 'V' o 'W'.

SELECT name FROM people WHERE (name NOT LIKE '%V%' AND name NOT LIKE '%W%') AND category = 'Director';

7. Obtener el título y año de las películas estrenadas en el año 1980 o antes.

SELECT title, release_year FROM movies WHERE release_year <= '1980'


8. Obtener las 5 películas con más recaudación, ordenadas de manera descendente según su recaudación. Mostrar título, año, cantidad de espectadores y recaudación.

SELECT title, release_year,total_viewers, total_revenue FROM movies WHERE total_revenue IS NOT NULL ORDER BY total_revenue DESC LIMIT 5;

9. Obtener todas las personas que tengan las 5 vocales en su nombre.

ELECT name FROM people WHERE name LIKE '%A%' AND name LIKE '%E%' AND name LIKE'%I%' AND name LIKE '%O%' AND name LIKE '%U%';

10. Obtener la lista de años en que se estrenaron películas. Eliminar duplicados y ordenar de manera ascendente.

SELECT DISTINCT release_year FROM  movies  ORDER BY release_year ASC;

11. Utilizando subqueries (subconsultas), obtener los títulos de las películas dirigidas por Christopher Nolan.

SELECT title FROM  movies WHERE director_id = (SELECT people_id FROM people WHERE name = 'Christopher Nolan');

12. Utilizando subqueries, obtener los nombres de los actores nacidos en Reino Unido. Ordenar por nombre.

SELECT name FROM people WHERE  country_of_birth_id = (SELECT country_id FROM countries WHERE country_name= 'REINO UNIDO' ) AND category = 'Actor' ORDER BY name

13. Utilizando subqueries, obtener todas las películas de "20th Century Fox" (cualquiera sea su año de estreno) y además, sin importar su estudio, aquellas que fueron estrenadas luego de 2010.

SELECT title, release_year FROM movies WHERE studio_id = (SELECT studio_id FROM studios WHERE studio_name = '20th Century Fox') OR release_year > 2010;

14. Utilizando subqueries, obtener todas las películas de "Warner Bros" estrenadas en 2015 o años posteriores.
SELECT title, release_year FROM movies WHERE studio_id = (SELECT studio_id FROM studios WHERE studio_name = 'Warner Bros') AND release_year >= 2015;