-- =============================================================
-- MYSQL - MODIFICADORES 1
-- DISTINCT, WHERE, ORDER BY, LIKE, AND/OR/NOT, LIMIT
-- Fuentes: MySQL 8.0 Docs + W3Schools
-- Ejemplos sobre cineDB
-- =============================================================


-- =============================================================
-- 1. DISTINCT - Eliminar duplicados
-- =============================================================
-- Devuelve solo valores únicos en la columna indicada.
-- Cuándo usarlo: cuando una columna puede tener valores repetidos
--               y solo quieres ver qué valores distintos existen.

-- Sintaxis:
-- SELECT DISTINCT columna FROM tabla;

-- Ver qué categorías existen en people (sin repetir)
SELECT DISTINCT category FROM people;

-- Ver en qué años se estrenaron películas (sin repetir)
SELECT DISTINCT release_year FROM movies ORDER BY release_year;


-- =============================================================
-- 2. WHERE - Filtrar filas
-- =============================================================
-- Filtra y devuelve solo las filas que cumplen la condición.
-- Cuándo usarlo: siempre que no quieras traer toda la tabla.
-- Va después de FROM, antes de ORDER BY y LIMIT.

-- Sintaxis:
-- SELECT columnas FROM tabla WHERE condición;

-- Operadores de comparación:
--   =       igual
--   != o <> distinto
--   >       mayor que
--   <       menor que
--   >=      mayor o igual
--   <=      menor o igual

-- Películas estrenadas después del año 2000
SELECT title, release_year FROM movies WHERE release_year > 2000;

-- Personas que son directores
SELECT name, birth_date FROM people WHERE category = 'Director';

-- Películas con más de 50 millones de espectadores
SELECT title, total_viewers FROM movies WHERE total_viewers > 50000000;

-- Películas con recaudación exactamente nula (no registrada)
-- IMPORTANTE: para NULL siempre usar IS NULL, nunca = NULL
SELECT title FROM movies WHERE total_revenue IS NULL;

-- Películas que SÍ tienen recaudación registrada
SELECT title, total_revenue FROM movies WHERE total_revenue IS NOT NULL;


-- =============================================================
-- 3. ORDER BY - Ordenar resultados
-- =============================================================
-- Ordena las filas del resultado por una o más columnas.
-- ASC  = ascendente (A→Z, 0→9) — valor por defecto si no se escribe
-- DESC = descendente (Z→A, 9→0)
-- Cuándo usarlo: cuando el orden de los resultados importa.

-- Sintaxis:
-- SELECT columnas FROM tabla ORDER BY columna ASC|DESC;

-- Películas ordenadas por año de estreno (más antiguas primero)
SELECT title, release_year FROM movies ORDER BY release_year ASC;

-- Películas ordenadas por recaudación (mayor primero)
SELECT title, total_revenue FROM movies ORDER BY total_revenue DESC;

-- Personas ordenadas por nombre alfabéticamente
SELECT name FROM people ORDER BY name ASC;

-- Ordenar por dos columnas:
-- primero por categoría (A→Z), luego por nombre (A→Z) dentro de cada categoría
SELECT name, category FROM people ORDER BY category ASC, name ASC;


-- =============================================================
-- 4. LIKE - Buscar por patrón de texto
-- =============================================================
-- Busca filas donde una columna de texto coincide con un patrón.
-- Cuándo usarlo: cuando no sabes el valor exacto pero sí una parte.
-- SIEMPRE va dentro de WHERE.

-- Sintaxis:
-- SELECT columnas FROM tabla WHERE columna LIKE 'patrón';

-- WILDCARDS (caracteres especiales que representan texto):
--
-- %  → cualquier cantidad de caracteres (incluyendo ninguno)
-- _  → exactamente UN carácter

-- Patrones más comunes:
-- 'A%'    → empieza con A
-- '%a'    → termina con a
-- '%on%'  → contiene "on" en cualquier posición
-- '_ohn'  → cualquier carácter + "ohn" (4 letras en total)
-- 'J___'  → J + exactamente 3 caracteres (4 letras en total)

-- Películas que empiezan con "The"
SELECT title FROM movies WHERE title LIKE 'The%';

-- Personas cuyo nombre termina en "on"
SELECT name FROM people WHERE name LIKE '%on';

-- Personas cuyo nombre contiene "ar" en cualquier posición
SELECT name FROM people WHERE name LIKE '%ar%';

-- Personas cuyo nombre empieza con "J" y tiene exactamente 4 letras
SELECT name FROM people WHERE name LIKE 'J___';

-- NOT LIKE: lo contrario — filas que NO coinciden con el patrón
-- Películas cuyo título NO empieza con "The"
SELECT title FROM movies WHERE title NOT LIKE 'The%';

-- NOTA: LIKE no distingue mayúsculas de minúsculas por defecto en MySQL
-- 'the%' y 'The%' devuelven los mismos resultados


-- =============================================================
-- 5. AND, OR, NOT - Combinar condiciones
-- =============================================================
-- Permiten combinar múltiples condiciones en el WHERE.

-- AND → ambas condiciones deben cumplirse
-- OR  → al menos una condición debe cumplirse
-- NOT → niega la condición (invierte el resultado)

-- Sintaxis:
-- WHERE condición1 AND condición2
-- WHERE condición1 OR condición2
-- WHERE NOT condición

-- AND: películas después de 2000 Y con más de 50M espectadores
SELECT title, release_year, total_viewers
FROM movies
WHERE release_year > 2000 AND total_viewers > 50000000;

-- OR: directores nacidos en Reino Unido O en Canadá
-- (country_id 14 = Reino Unido, 4 = Canadá)
SELECT name, country_of_birth_id
FROM people
WHERE category = 'Director'
AND (country_of_birth_id = 14 OR country_of_birth_id = 4);

-- NOT: personas que NO son actores
SELECT name, category FROM people WHERE NOT category = 'Actor';
-- equivalente a:
SELECT name, category FROM people WHERE category != 'Actor';

-- Combinación de los tres: películas entre 1990 y 2010,
-- que NO tengan recaudación nula, ordenadas por recaudación
SELECT title, release_year, total_revenue
FROM movies
WHERE release_year >= 1990
AND release_year <= 2010
AND NOT total_revenue IS NULL
ORDER BY total_revenue DESC;

-- PRECEDENCIA (orden en que MySQL evalúa):
-- 1. NOT   (se evalúa primero)
-- 2. AND
-- 3. OR    (se evalúa último)
-- Usa paréntesis para controlar el orden cuando combines AND y OR:
-- WHERE (condA OR condB) AND condC   ← paréntesis cambia el resultado


-- =============================================================
-- 6. LIMIT - Limitar cantidad de resultados
-- =============================================================
-- Devuelve solo los primeros N registros.
-- Cuándo usarlo: paginación, previews, top N resultados.
-- Es la última cláusula que va en la query.

-- Sintaxis:
-- SELECT columnas FROM tabla LIMIT n;
-- SELECT columnas FROM tabla LIMIT n OFFSET m;

-- Las 5 películas con mayor recaudación
SELECT title, total_revenue
FROM movies
WHERE total_revenue IS NOT NULL
ORDER BY total_revenue DESC
LIMIT 5;

-- Las 3 personas más jóvenes (por fecha de nacimiento más reciente)
SELECT name, birth_date
FROM people
WHERE birth_date IS NOT NULL
ORDER BY birth_date DESC
LIMIT 3;

-- LIMIT con OFFSET — paginación:
-- OFFSET indica cuántos registros saltar antes de empezar a devolver
-- Página 1 (registros 1-5):
SELECT title FROM movies ORDER BY movie_id LIMIT 5 OFFSET 0;
-- Página 2 (registros 6-10):
SELECT title FROM movies ORDER BY movie_id LIMIT 5 OFFSET 5;
-- Página 3 (registros 11-15):
SELECT title FROM movies ORDER BY movie_id LIMIT 5 OFFSET 10;

-- Fórmula para paginación en backend:
-- OFFSET = (número_de_página - 1) * registros_por_página


-- =============================================================
-- 7. ORDEN OBLIGATORIO DE CLÁUSULAS (recordatorio)
-- =============================================================
-- SELECT   → qué columnas
-- FROM     → de qué tabla
-- WHERE    → filtro de filas
-- ORDER BY → ordenamiento
-- LIMIT    → cantidad máxima de filas

-- Ejemplo completo con todo:
SELECT DISTINCT title, release_year, total_revenue
FROM movies
WHERE release_year >= 1990
AND total_revenue IS NOT NULL
ORDER BY total_revenue DESC
LIMIT 10 OFFSET 0;