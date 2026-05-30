-- =============================================================
-- MYSQL - SUBQUERIES CON INSERT, UPDATE, DELETE
-- Fuentes: MySQL 8.0 Docs + W3Schools
-- Ejemplos sobre cineDB
-- =============================================================
-- Una subquery dentro de INSERT, UPDATE o DELETE permite usar
-- valores de otras tablas sin necesidad de conocer los IDs
-- de antemano. Hace el código más robusto y reutilizable.
-- =============================================================


-- =============================================================
-- 1. UPDATE + SUBQUERY
-- =============================================================
-- Cuándo usarlo: cuando necesitas actualizar una columna con un
-- valor que viene de otra tabla, sin hardcodear el ID.

-- -------------------------------------------------------------
-- 1.1 Actualizar una columna usando el resultado de una subquery
-- -------------------------------------------------------------

-- Asociar el estudio "Warner Bros" a "Interstellar" y "The Dark Knight"
-- Sin subquery (frágil — depende de conocer el ID):
UPDATE cineDB.movies
SET studio_id = 1
WHERE title IN ('Interstellar', 'The Dark Knight');

-- Con subquery (robusto — funciona aunque el ID cambie):
UPDATE cineDB.movies
SET studio_id = (SELECT studio_id FROM studios WHERE studio_name = 'Warner Bros')
WHERE title IN ('Interstellar', 'The Dark Knight');

-- Asignar director a una película por nombre (sin saber el ID)
UPDATE cineDB.movies
SET director_id = (SELECT people_id FROM people WHERE name = 'Ridley Scott')
WHERE title = 'Alien';

-- Actualizar el país de nacimiento de una persona por nombre de país
UPDATE cineDB.people
SET country_of_birth_id = (SELECT country_id FROM countries WHERE country_name = 'España')
WHERE name = 'Pedro Almodóvar';

-- -------------------------------------------------------------
-- 1.2 UPDATE con subquery en el WHERE
-- -------------------------------------------------------------
-- Cuándo usarlo: cuando la condición del WHERE depende de datos
-- de otra tabla.

-- Poner en NULL el studio_id de todas las películas de "Fox Searchlight"
UPDATE cineDB.movies
SET studio_id = NULL
WHERE studio_id = (SELECT studio_id FROM studios WHERE studio_name = 'Fox Searchlight');

-- Actualizar espectadores de todas las películas dirigidas por Nolan
UPDATE cineDB.movies
SET total_viewers = total_viewers + 1000000
WHERE director_id = (SELECT people_id FROM people WHERE name = 'Christopher Nolan');


-- =============================================================
-- 2. INSERT + SUBQUERY
-- =============================================================
-- Cuándo usarlo: cuando los valores a insertar dependen de IDs
-- que están en otras tablas, sin necesidad de consultarlos antes.

-- -------------------------------------------------------------
-- 2.1 INSERT usando subqueries como valores
-- -------------------------------------------------------------

-- Insertar una película usando subqueries para director y estudio
INSERT INTO cineDB.movies (title, release_year, director_id, studio_id, total_viewers, total_revenue)
VALUES (
    'Avatar',
    2009,
    (SELECT people_id FROM people WHERE name = 'James Cameron'),
    (SELECT studio_id FROM studios WHERE studio_name = '20th Century Fox'),
    331000000,
    2923706026
);

-- Insertar una persona y asignarle el país por nombre
INSERT INTO cineDB.people (name, birth_date, country_of_birth_id, category)
VALUES (
    'Alejandro González Iñárritu',
    '1963-08-15',
    (SELECT country_id FROM countries WHERE country_name = 'México'),
    'Director'
);

-- -------------------------------------------------------------
-- 2.2 INSERT ... SELECT - Insertar el resultado de una consulta
-- -------------------------------------------------------------
-- Cuándo usarlo: copiar datos entre tablas, poblar tablas derivadas.

-- Copiar todos los directores a una tabla de respaldo (si existiera)
-- INSERT INTO directores_backup (name, birth_date, category)
-- SELECT name, birth_date, category
-- FROM people
-- WHERE category = 'Director';


-- =============================================================
-- 3. DELETE + SUBQUERY
-- =============================================================
-- Cuándo usarlo: cuando la condición de eliminación depende de
-- datos en otra tabla.

-- Eliminar todas las películas de un estudio por nombre
DELETE FROM cineDB.movies
WHERE studio_id = (SELECT studio_id FROM studios WHERE studio_name = 'Fox Searchlight');

-- Eliminar de movie_actor todos los registros de un actor por nombre
DELETE FROM cineDB.movie_actor
WHERE actor_id = (SELECT people_id FROM people WHERE name = 'Hugo Weaving');

-- Eliminar relaciones de género de películas anteriores a 1980
DELETE FROM cineDB.movie_genre
WHERE movie_id IN (
    SELECT movie_id FROM movies WHERE release_year < 1980
);


-- =============================================================
-- 4. REGLA CLAVE - cuándo usar = vs IN con subqueries
-- =============================================================
-- = → cuando la subquery devuelve UN solo valor
-- IN → cuando la subquery puede devolver VARIOS valores

-- Devuelve UN valor → usar =
UPDATE movies
SET studio_id = (SELECT studio_id FROM studios WHERE studio_name = 'Warner Bros')
WHERE title = 'Inception';

-- Devuelve VARIOS valores → usar IN
UPDATE movies
SET total_viewers = 0
WHERE director_id IN (
    SELECT people_id FROM people WHERE country_of_birth_id = (
        SELECT country_id FROM countries WHERE country_name = 'Reino Unido'
    )
);


-- =============================================================
-- 5. FLUJO SEGURO AL COMBINAR SUBQUERIES CON UPDATE/DELETE
-- =============================================================
-- 1. Primero prueba la subquery sola para verificar su resultado
-- 2. Luego prueba el SELECT equivalente con esa subquery en el WHERE
-- 3. Si el resultado es correcto, cambia a UPDATE o DELETE

-- Paso 1 — verificar la subquery:
SELECT studio_id FROM studios WHERE studio_name = 'Warner Bros';

-- Paso 2 — verificar qué filas se van a afectar:
SELECT title, studio_id FROM movies
WHERE title IN ('Interstellar', 'The Dark Knight');

-- Paso 3 — ejecutar el UPDATE:
UPDATE movies
SET studio_id = (SELECT studio_id FROM studios WHERE studio_name = 'Warner Bros')
WHERE title IN ('Interstellar', 'The Dark Knight');