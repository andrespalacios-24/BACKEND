-- =============================================================
-- MYSQL - MODIFICADORES 2
-- NULL, MIN, MAX, COUNT, SUM, AVG, IN, BETWEEN,
-- AS (alias), CONCAT, GROUP BY, HAVING, CASE, IFNULL
-- Fuentes: MySQL 8.0 Docs + W3Schools
-- Ejemplos sobre cineDB
-- =============================================================


-- =============================================================
-- 1. NULL - Valores vacíos
-- =============================================================
-- NULL significa "sin valor" — no es 0, no es '', es ausencia de dato.
-- Cuándo aparece: campos opcionales que no se rellenaron al insertar.
-- NUNCA comparar con = NULL — siempre IS NULL o IS NOT NULL.

-- Buscar películas sin director registrado
SELECT title FROM movies WHERE director_id IS NULL;

-- Buscar personas con fecha de nacimiento registrada
SELECT name, birth_date FROM people WHERE birth_date IS NOT NULL;

-- Buscar películas sin espectadores Y sin recaudación
SELECT title FROM movies
WHERE total_viewers IS NULL AND total_revenue IS NULL;


-- =============================================================
-- 2. FUNCIONES DE AGREGACIÓN: MIN, MAX, COUNT, SUM, AVG
-- =============================================================
-- Calculan un valor resumen sobre un conjunto de filas.
-- Se usan en el SELECT, no en el WHERE.
-- Ignoran NULL automáticamente (excepto COUNT(*)).

-- -------------------------------------------------------------
-- MIN() - Valor mínimo
-- -------------------------------------------------------------
-- Cuándo usarlo: el más antiguo, el más barato, el más pequeño.

-- Año de estreno más antiguo registrado
SELECT MIN(release_year) AS año_mas_antiguo FROM movies;

-- Menor recaudación registrada
SELECT MIN(total_revenue) AS menor_recaudacion FROM movies;

-- -------------------------------------------------------------
-- MAX() - Valor máximo
-- -------------------------------------------------------------
-- Cuándo usarlo: el más reciente, el más caro, el más grande.

-- Película con mayor recaudación
SELECT MAX(total_revenue) AS mayor_recaudacion FROM movies;

-- Persona con la fecha de nacimiento más reciente (más joven)
SELECT MAX(birth_date) AS persona_mas_joven FROM people;

-- -------------------------------------------------------------
-- COUNT() - Contar filas
-- -------------------------------------------------------------
-- COUNT(*)         → cuenta TODAS las filas, incluyendo NULL
-- COUNT(columna)   → cuenta solo filas donde esa columna NO es NULL
-- Cuándo usarlo: cuántos registros hay, cuántos cumplen una condición.

-- Total de películas en la tabla
SELECT COUNT(*) AS total_peliculas FROM movies;

-- Total de películas que tienen director registrado (no NULL)
SELECT COUNT(director_id) AS peliculas_con_director FROM movies;

-- Total de actores (no directores)
SELECT COUNT(*) AS total_actores FROM people WHERE category = 'Actor';

-- -------------------------------------------------------------
-- SUM() - Suma total
-- -------------------------------------------------------------
-- Cuándo usarlo: total de ventas, suma de espectadores, acumulados.

-- Suma total de espectadores de todas las películas
SELECT SUM(total_viewers) AS espectadores_totales FROM movies;

-- Suma total de recaudación
SELECT SUM(total_revenue) AS recaudacion_total FROM movies;

-- -------------------------------------------------------------
-- AVG() - Promedio
-- -------------------------------------------------------------
-- Cuándo usarlo: promedio de precios, edad promedio, recaudación media.

-- Recaudación promedio de las películas
SELECT AVG(total_revenue) AS recaudacion_promedio FROM movies;

-- Año de estreno promedio
SELECT AVG(release_year) AS año_promedio FROM movies;


-- =============================================================
-- 3. IN - Filtrar por lista de valores
-- =============================================================
-- Alternativa más limpia a varios OR encadenados.
-- Cuándo usarlo: cuando quieres filtrar por varios valores posibles
--               de una misma columna.

-- Sintaxis:
-- WHERE columna IN (valor1, valor2, valor3)
-- WHERE columna NOT IN (valor1, valor2, valor3)

-- Películas de Warner Bros (1), Columbia Pictures (2) o Universal (4)
SELECT title, studio_id FROM movies WHERE studio_id IN (1, 2, 4);

-- Personas nacidas en Estados Unidos (7), Reino Unido (14) o Canadá (4)
SELECT name, country_of_birth_id
FROM people
WHERE country_of_birth_id IN (7, 14, 4)
ORDER BY country_of_birth_id;

-- NOT IN: personas que NO nacieron en esos países
SELECT name FROM people
WHERE country_of_birth_id NOT IN (7, 14, 4)
AND country_of_birth_id IS NOT NULL;

-- Equivalencia — estas dos queries son idénticas:
-- Con OR:
SELECT title FROM movies WHERE studio_id = 1 OR studio_id = 2 OR studio_id = 4;
-- Con IN (más limpio):
SELECT title FROM movies WHERE studio_id IN (1, 2, 4);


-- =============================================================
-- 4. BETWEEN - Filtrar por rango
-- =============================================================
-- Filtra valores dentro de un rango, incluyendo los extremos.
-- Cuándo usarlo: rangos de fechas, rangos de precios, rangos numéricos.
-- Es equivalente a: columna >= valor1 AND columna <= valor2

-- Sintaxis:
-- WHERE columna BETWEEN valor_minimo AND valor_maximo

-- Películas estrenadas entre 1990 y 2010 (inclusive)
SELECT title, release_year FROM movies
WHERE release_year BETWEEN 1990 AND 2010
ORDER BY release_year;

-- Películas con recaudación entre 100M y 500M
SELECT title, total_revenue FROM movies
WHERE total_revenue BETWEEN 100000000 AND 500000000
ORDER BY total_revenue;

-- Personas nacidas entre 1960 y 1970
SELECT name, birth_date FROM people
WHERE birth_date BETWEEN '1960-01-01' AND '1970-12-31'
ORDER BY birth_date;

-- NOT BETWEEN: fuera del rango
SELECT title, release_year FROM movies
WHERE release_year NOT BETWEEN 1990 AND 2010;


-- =============================================================
-- 5. AS - Alias
-- =============================================================
-- Renombra una columna o tabla en el resultado de la consulta.
-- No cambia nada en la base de datos — solo afecta el resultado.
-- Cuándo usarlo: hacer el resultado más legible, con funciones de
--               agregación, al combinar tablas.

-- Sintaxis:
-- SELECT columna AS nuevo_nombre FROM tabla;
-- SELECT columna AS nuevo_nombre FROM tabla AS alias_tabla;

-- Renombrar columnas con nombres descriptivos
SELECT title AS titulo, release_year AS año_estreno FROM movies;

-- Con funciones de agregación (sin AS el nombre sería COUNT(*))
SELECT COUNT(*) AS total_peliculas FROM movies;
SELECT AVG(total_revenue) AS recaudacion_promedio FROM movies;
SELECT MAX(total_viewers) AS maximo_espectadores FROM movies;

-- Alias de tabla (muy útil al combinar tablas con JOIN más adelante)
SELECT m.title, m.release_year
FROM movies AS m
WHERE m.total_revenue IS NOT NULL;


-- =============================================================
-- 6. CONCAT - Concatenar texto
-- =============================================================
-- Une dos o más valores de texto en uno solo.
-- Cuándo usarlo: combinar nombre y apellido, crear etiquetas,
--               formatear texto en la consulta.
-- Si CUALQUIER valor es NULL, el resultado es NULL.

-- Sintaxis:
-- CONCAT(valor1, valor2, valor3, ...)

-- Combinar nombre con su categoría
SELECT CONCAT(name, ' - ', category) AS persona_y_rol FROM people;

-- Combinar título con año entre paréntesis
SELECT CONCAT(title, ' (', release_year, ')') AS pelicula_con_año
FROM movies
WHERE release_year IS NOT NULL;

-- CONCAT_WS (With Separator) — el primer parámetro es el separador
-- más cómodo cuando tienes muchos valores con el mismo separador
SELECT CONCAT_WS(' | ', title, release_year, total_revenue) AS info
FROM movies;

-- PRECAUCIÓN: si algún campo es NULL, CONCAT devuelve NULL
-- Solución: usar IFNULL dentro de CONCAT (ver sección 9)
SELECT CONCAT(name, ' - ', IFNULL(birth_date, 'Fecha desconocida')) AS info
FROM people;


-- =============================================================
-- 7. GROUP BY - Agrupar filas
-- =============================================================
-- Agrupa filas que tienen el mismo valor en la columna indicada.
-- Cuándo usarlo: siempre que uses funciones de agregación (COUNT,
--               SUM, AVG, etc.) y quieras el resultado por grupos.
-- Regla clave: toda columna en el SELECT que no sea una función
--              de agregación DEBE estar en el GROUP BY.

-- Sintaxis:
-- SELECT columna, FUNCION(otra_columna)
-- FROM tabla
-- GROUP BY columna;

-- Contar cuántas películas tiene cada estudio
SELECT studio_id, COUNT(*) AS cantidad_peliculas
FROM movies
WHERE studio_id IS NOT NULL
GROUP BY studio_id
ORDER BY cantidad_peliculas DESC;

-- Contar cuántas personas hay por categoría (Actor / Director)
SELECT category, COUNT(*) AS cantidad
FROM people
GROUP BY category;

-- Suma de espectadores por año de estreno
SELECT release_year, SUM(total_viewers) AS espectadores_por_año
FROM movies
WHERE release_year IS NOT NULL AND total_viewers IS NOT NULL
GROUP BY release_year
ORDER BY release_year;

-- Recaudación promedio por estudio
SELECT studio_id, AVG(total_revenue) AS recaudacion_promedio
FROM movies
WHERE studio_id IS NOT NULL AND total_revenue IS NOT NULL
GROUP BY studio_id;


-- =============================================================
-- 8. HAVING - Filtrar grupos (GROUP BY + condición)
-- =============================================================
-- Es el WHERE para grupos — filtra después de que GROUP BY agrupa.
-- Cuándo usarlo: cuando quieres filtrar por el resultado de una
--               función de agregación.
-- Diferencia clave:
--   WHERE filtra ANTES de agrupar (filas individuales)
--   HAVING filtra DESPUÉS de agrupar (grupos completos)

-- Sintaxis:
-- SELECT columna, FUNCION(columna2)
-- FROM tabla
-- GROUP BY columna
-- HAVING FUNCION(columna2) condición;

-- Estudios con más de 2 películas
SELECT studio_id, COUNT(*) AS cantidad
FROM movies
WHERE studio_id IS NOT NULL
GROUP BY studio_id
HAVING COUNT(*) > 2;

-- Años con recaudación total mayor a 1 billón
SELECT release_year, SUM(total_revenue) AS total
FROM movies
WHERE release_year IS NOT NULL AND total_revenue IS NOT NULL
GROUP BY release_year
HAVING SUM(total_revenue) > 1000000000
ORDER BY total DESC;

-- Categorías con más de 5 personas
SELECT category, COUNT(*) AS cantidad
FROM people
GROUP BY category
HAVING COUNT(*) > 5;


-- =============================================================
-- 9. CASE - Lógica condicional dentro de una query
-- =============================================================
-- Es el equivalente SQL de un if/elif/else.
-- Cuándo usarlo: crear columnas calculadas según condiciones,
--               categorizar valores, transformar datos en la consulta.
-- Va en el SELECT, no en el WHERE.

-- Sintaxis:
-- CASE
--   WHEN condición1 THEN resultado1
--   WHEN condición2 THEN resultado2
--   ELSE resultado_por_defecto
-- END AS nombre_columna

-- Categorizar películas por recaudación
SELECT title, total_revenue,
    CASE
        WHEN total_revenue >= 1000000000 THEN 'Taquillera'
        WHEN total_revenue >= 200000000  THEN 'Exitosa'
        WHEN total_revenue >= 50000000   THEN 'Rentable'
        WHEN total_revenue IS NULL       THEN 'Sin datos'
        ELSE 'Baja recaudación'
    END AS categoria_recaudacion
FROM movies
ORDER BY total_revenue DESC;

-- Etiquetar personas como recientes o clásicas según nacimiento
SELECT name, birth_date,
    CASE
        WHEN birth_date >= '1980-01-01' THEN 'Generación reciente'
        WHEN birth_date >= '1960-01-01' THEN 'Generación media'
        WHEN birth_date IS NULL         THEN 'Sin fecha registrada'
        ELSE 'Clásico'
    END AS generacion
FROM people
ORDER BY birth_date DESC;


-- =============================================================
-- 10. IFNULL - Reemplazar NULL por un valor
-- =============================================================
-- Si el valor es NULL, lo reemplaza por el valor alternativo.
-- Si no es NULL, devuelve el valor original.
-- Cuándo usarlo: mostrar texto amigable en lugar de NULL,
--               evitar que CONCAT devuelva NULL.

-- Sintaxis:
-- IFNULL(columna, valor_si_es_null)

-- Mostrar "Sin datos" cuando total_viewers es NULL
SELECT title, IFNULL(total_viewers, 0) AS espectadores
FROM movies;

-- Mostrar texto cuando no hay fecha de nacimiento
SELECT name, IFNULL(birth_date, 'Desconocida') AS fecha_nacimiento
FROM people;

-- Combinar IFNULL con CONCAT para evitar NULL en concatenaciones
SELECT CONCAT(name, ' - Nació: ', IFNULL(birth_date, 'Sin fecha')) AS info
FROM people;

-- IFNULL en cálculos — tratar NULL como 0
SELECT title,
    IFNULL(total_viewers, 0) AS espectadores,
    IFNULL(total_revenue, 0) AS recaudacion
FROM movies
ORDER BY recaudacion DESC;


-- =============================================================
-- 11. ORDEN COMPLETO DE CLÁUSULAS
-- =============================================================
-- SELECT   → columnas, funciones, alias, CASE
-- FROM     → tabla (con alias si se necesita)
-- WHERE    → filtro de filas individuales (antes de agrupar)
-- GROUP BY → agrupación
-- HAVING   → filtro de grupos (después de agrupar)
-- ORDER BY → ordenamiento
-- LIMIT    → cantidad máxima de filas

-- Ejemplo con todo junto:
SELECT
    studio_id,
    COUNT(*) AS total_peliculas,
    SUM(IFNULL(total_revenue, 0)) AS recaudacion_total,
    CASE
        WHEN COUNT(*) >= 3 THEN 'Estudio activo'
        ELSE 'Estudio pequeño'
    END AS clasificacion
FROM movies
WHERE release_year IS NOT NULL
GROUP BY studio_id
HAVING COUNT(*) >= 1
ORDER BY recaudacion_total DESC
LIMIT 5;

-- =============================================================
-- 12. SUBQUERY (Subconsulta)
-- =============================================================
-- Una query dentro de otra query.
-- La query interior se ejecuta primero y su resultado
-- lo usa la query exterior como valor o lista de valores.
-- Cuándo usarlo: cuando necesitas datos de otra tabla para
--               filtrar, pero aún no has visto JOIN.

-- Sintaxis con valor único (=):
-- SELECT columnas FROM tabla
-- WHERE columna = (SELECT columna FROM tabla2 WHERE condición);

-- Sintaxis con múltiples valores (IN):
-- SELECT columnas FROM tabla
-- WHERE columna IN (SELECT columna FROM tabla2 WHERE condición);

-- Películas dirigidas por Christopher Nolan
SELECT title
FROM movies
WHERE director_id = (
    SELECT people_id
    FROM people
    WHERE name = 'Christopher Nolan'
);

-- Actores nacidos en Reino Unido (country_id puede ser múltiple → IN)
SELECT name
FROM people
WHERE category = 'Actor'
AND country_of_birth_id IN (
    SELECT country_id
    FROM countries
    WHERE country_name = 'Reino Unido'
)
ORDER BY name;

-- REGLA CLAVE:
-- Si la subquery devuelve UN solo valor  → usar =
-- Si la subquery devuelve VARIOS valores → usar IN

-- =============================================================
-- 13. FUNCIONES DE FECHA
-- =============================================================
-- MySQL tiene funciones para extraer partes de una fecha.
-- Cuándo usarlas: cuando no necesitas la fecha completa sino
--                solo una parte (año, mes, día).

-- YEAR(fecha)  → extrae el año
-- MONTH(fecha) → extrae el mes (número: 1-12)
-- DAY(fecha)   → extrae el día del mes
-- NOW()        → fecha y hora actual del servidor

-- Obtener el año de nacimiento de cada director
SELECT name, YEAR(birth_date) AS año_nacimiento
FROM people
WHERE birth_date IS NOT NULL AND category = 'Director';

-- Obtener el mes de nacimiento de los actores
SELECT name, MONTH(birth_date) AS mes_nacimiento
FROM people
WHERE birth_date IS NOT NULL AND category = 'Actor';

-- Actores nacidos en un mes específico (ej: enero = 1)
SELECT name FROM people
WHERE category = 'Actor' AND MONTH(birth_date) = 1;

-- Películas estrenadas en una década (usando YEAR sobre INT)
-- release_year ya es INT en cineDB, así que no necesita YEAR()
SELECT title, release_year FROM movies
WHERE release_year BETWEEN 1990 AND 1999;