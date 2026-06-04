-- =============================================================
-- MYSQL - ESCRITURA DE DATOS RELACIONADOS
-- INSERT, UPDATE, DELETE en tablas con relaciones 1:1, 1:N, N:M
-- Fuentes: MySQL 8.0 Docs + W3Schools
-- Ejemplos sobre cineDB
-- =============================================================
-- Cuando las tablas tienen FOREIGN KEY, el orden en que insertas,
-- actualizas o eliminas importa. MySQL valida las relaciones en
-- cada operación y rechaza las que violen la integridad referencial.
-- =============================================================


-- =============================================================
-- 1. REGLA FUNDAMENTAL — ORDEN DE OPERACIONES
-- =============================================================
-- La FOREIGN KEY garantiza que no puedas referenciar un registro
-- que no existe. Esto define el orden obligatorio:
--
-- INSERT: primero la tabla padre (el referenciado), luego el hijo
-- DELETE: primero la tabla hijo (el que tiene la FK), luego el padre
-- UPDATE: si cambias una FK, el nuevo valor debe existir en el padre
--
-- Violar este orden genera estos errores:
-- ERROR 1452: Cannot add or update a child row: foreign key constraint fails
--             → intentaste insertar/actualizar un hijo con un padre inexistente
-- ERROR 1451: Cannot delete or update a parent row: foreign key constraint fails
--             → intentaste eliminar un padre que todavía tiene hijos


-- =============================================================
-- 2. RELACIÓN 1:1 — Un registro de A con exactamente uno de B
-- =============================================================
-- La FK está en la tabla secundaria CON UNIQUE.
-- Tablas de referencia:
--   users (user_id PK, username, email)
--   dni   (dni_id PK, dni_number, user_id FK UNIQUE → users)


-- -------------------------------------------------------------
-- 2.1 INSERT en 1:1
-- -------------------------------------------------------------
-- Para qué: agregar el registro secundario vinculado al principal.
-- Cuándo: al crear datos que dependen de otro registro (DNI de usuario,
--         perfil de empleado, contrato de trabajador).
-- Cómo: primero insertar el padre, luego el hijo con la FK del padre.

-- Sintaxis:
-- INSERT INTO tabla_secundaria (columnas, fk_columna)
-- VALUES (valores, id_del_padre);

-- Paso 1 — insertar el padre:
INSERT INTO users (username, email)
VALUES ('jperez', 'juan@example.com');

-- Paso 2 — insertar el hijo con ID conocido:
INSERT INTO dni (dni_number, user_id)
VALUES (12345678, 1);

-- Paso 2 — insertar el hijo con subquery (más robusto):
INSERT INTO dni (dni_number, user_id)
VALUES (12345678,
    (SELECT user_id FROM users WHERE username = 'jperez')
);

-- ERROR — insertar dos registros secundarios para el mismo padre:
-- INSERT INTO dni (dni_number, user_id) VALUES (99999999, 1);
-- Error: Duplicate entry '1' for key 'user_id' (viola el UNIQUE)

-- ERROR — insertar hijo con padre inexistente:
-- INSERT INTO dni (dni_number, user_id) VALUES (12345678, 999);
-- Error: Cannot add or update a child row: foreign key constraint fails


-- -------------------------------------------------------------
-- 2.2 UPDATE en 1:1
-- -------------------------------------------------------------
-- Para qué: modificar el dato del registro secundario.
-- Cuándo: corrección de datos, actualización de información personal.
-- Cómo: UPDATE en la tabla secundaria filtrando por la FK del padre.

-- Sintaxis:
-- UPDATE tabla_secundaria
-- SET columna = nuevo_valor
-- WHERE fk_columna = (SELECT pk FROM tabla_padre WHERE condición);

UPDATE dni
SET dni_number = 87654321
WHERE user_id = (SELECT user_id FROM users WHERE username = 'jperez');


-- -------------------------------------------------------------
-- 2.3 DELETE en 1:1
-- -------------------------------------------------------------
-- Para qué: eliminar el registro y su dependiente.
-- Cuándo: dar de baja un usuario y todos sus datos asociados.
-- Cómo: primero eliminar el hijo, luego el padre.

-- Sintaxis:
-- DELETE FROM tabla_secundaria WHERE fk_columna = id_del_padre;
-- DELETE FROM tabla_principal WHERE pk_columna = id;

-- Paso 1 — eliminar el hijo:
DELETE FROM dni
WHERE user_id = (SELECT user_id FROM users WHERE username = 'jperez');

-- Paso 2 — eliminar el padre:
DELETE FROM users WHERE username = 'jperez';

-- ERROR — intentar eliminar el padre sin eliminar el hijo primero:
-- DELETE FROM users WHERE username = 'jperez';
-- Error: Cannot delete or update a parent row: foreign key constraint fails


-- =============================================================
-- 3. RELACIÓN 1:N — Un padre con muchos hijos
-- =============================================================
-- La FK está en la tabla hijo SIN UNIQUE.
-- ES LA RELACIÓN MÁS COMÚN en bases de datos relacionales.
-- Tablas de referencia:
--   movies      (movie_id PK, title, director_id FK → people)
--   people      (people_id PK, name, category)
--   movie_review (review_id PK, movie_id FK → movies, review_text)


-- -------------------------------------------------------------
-- 3.1 INSERT en 1:N
-- -------------------------------------------------------------
-- Para qué: agregar múltiples registros hijo a un mismo padre.
-- Cuándo: agregar reseñas a una película, pedidos a un cliente,
--         empleados a una empresa.
-- Cómo: el padre ya existe, insertar los hijos con su FK.

-- Sintaxis:
-- INSERT INTO tabla_hijo (fk_columna, otras_columnas)
-- VALUES (id_padre, valores),
--        (id_padre, valores);

-- Con ID conocido — múltiples hijos en un INSERT:
INSERT INTO movie_review (movie_id, review_text, review_timestamp)
VALUES (16, 'Excelente película', '2024-01-15 10:30:00'),
       (16, 'Una obra maestra',   '2024-02-20 14:45:00');

-- Con subquery — sin conocer el ID:
INSERT INTO movie_review (movie_id, review_text)
VALUES (
    (SELECT movie_id FROM movies WHERE title = 'Gladiator'),
    'La mejor película de gladiadores'
);

-- Sin fecha — usa DEFAULT (CURRENT_TIMESTAMP):
INSERT INTO movie_review (movie_id, review_text)
VALUES (18, 'Review sin fecha explícita');
-- review_timestamp se llena automáticamente con la fecha actual


-- -------------------------------------------------------------
-- 3.2 UPDATE en 1:N
-- -------------------------------------------------------------
-- Para qué: cambiar la FK de un hijo (reasignarlo a otro padre),
--           o actualizar datos de varios hijos a la vez.
-- Cuándo: cambiar el director de una película, reasignar empleados
--         a otra empresa, cambiar el estudio de varias películas.
-- Cómo: UPDATE en la tabla hijo con WHERE que filtre los hijos correctos.

-- Sintaxis:
-- UPDATE tabla_hijo
-- SET fk_columna = nuevo_id_padre
-- WHERE condición;

-- Cambiar el director de una película:
UPDATE movies
SET director_id = (SELECT people_id FROM people WHERE name = 'Ridley Scott')
WHERE title = 'Alien';

-- Actualizar todas las películas de un director (varios hijos a la vez):
UPDATE movies
SET studio_id = (SELECT studio_id FROM studios WHERE studio_name = 'Warner Bros')
WHERE director_id = (SELECT people_id FROM people WHERE name = 'Christopher Nolan');


-- -------------------------------------------------------------
-- 3.3 DELETE en 1:N
-- -------------------------------------------------------------
-- Para qué: eliminar un padre y todos sus hijos.
-- Cuándo: eliminar una película y sus reseñas, dar de baja
--         un cliente y sus pedidos.
-- Cómo: primero eliminar todos los hijos, luego el padre.

-- Sintaxis:
-- DELETE FROM tabla_hijo WHERE fk_columna = id_padre;
-- DELETE FROM tabla_padre WHERE pk_columna = id;

-- Paso 1 — eliminar los hijos:
DELETE FROM movie_review
WHERE movie_id = (SELECT movie_id FROM movies WHERE title = 'Gladiator');

-- Paso 2 — eliminar el padre:
DELETE FROM movies WHERE title = 'Gladiator';

-- Eliminar hijos de varios padres con IN:
DELETE FROM movie_review
WHERE movie_id IN (
    SELECT movie_id FROM movies WHERE release_year < 1990
);

-- ERROR — intentar eliminar el padre sin eliminar hijos primero:
-- DELETE FROM movies WHERE title = 'Gladiator';
-- Error: Cannot delete or update a parent row: foreign key constraint fails


-- =============================================================
-- 4. RELACIÓN N:M — Muchos de A con muchos de B
-- =============================================================
-- Requiere tabla intermedia con FK a ambas tablas y PK compuesta.
-- Tablas de referencia:
--   movies      (movie_id PK)
--   genres      (genre_id PK)
--   people      (people_id PK)
--   movie_genre (movie_id FK + genre_id FK → tabla intermedia)
--   movie_actor (movie_id FK + actor_id FK → tabla intermedia)


-- -------------------------------------------------------------
-- 4.1 INSERT en N:M
-- -------------------------------------------------------------
-- Para qué: crear una relación entre dos registros existentes.
-- Cuándo: asociar géneros a una película, actores a una película,
--         idiomas a un usuario, productos a un pedido.
-- Cómo: insertar en la tabla intermedia un par de IDs.
--       Ambos registros deben existir antes de insertar la relación.

-- Sintaxis:
-- INSERT INTO tabla_intermedia (fk_a, fk_b)
-- VALUES (id_a, id_b),
--        (id_a, id_b);

-- Con IDs conocidos — múltiples relaciones en un INSERT:
INSERT INTO movie_genre (movie_id, genre_id)
VALUES (19, 8),   -- Avatar - Comedia
       (19, 2),   -- Avatar - Acción
       (19, 1);   -- Avatar - Ciencia Ficción

-- Con subqueries — una relación por INSERT:
INSERT INTO movie_genre (movie_id, genre_id)
VALUES (
    (SELECT movie_id FROM movies WHERE title = 'Avatar'),
    (SELECT genre_id FROM genres WHERE genre_name = 'Acción')
);

-- Con subqueries — múltiples relaciones en un INSERT:
INSERT INTO movie_genre (movie_id, genre_id)
VALUES
    ((SELECT movie_id FROM movies WHERE title = 'Avatar'),
     (SELECT genre_id FROM genres WHERE genre_name = 'Comedia')),
    ((SELECT movie_id FROM movies WHERE title = 'Avatar'),
     (SELECT genre_id FROM genres WHERE genre_name = 'Acción')),
    ((SELECT movie_id FROM movies WHERE title = 'Avatar'),
     (SELECT genre_id FROM genres WHERE genre_name = 'Ciencia Ficción'));

-- ERROR — el par ya existe (viola la PK compuesta):
-- INSERT INTO movie_genre (movie_id, genre_id) VALUES (19, 2);
-- Error: Duplicate entry '19-2' for key 'PRIMARY'

-- ERROR — alguno de los IDs no existe:
-- INSERT INTO movie_genre (movie_id, genre_id) VALUES (999, 2);
-- Error: Cannot add or update a child row: foreign key constraint fails


-- -------------------------------------------------------------
-- 4.2 UPDATE en N:M
-- -------------------------------------------------------------
-- Para qué: cambiar uno de los valores de la relación.
-- Cuándo: cambiar un género por otro en una película específica.
-- Cómo: UPDATE en la tabla intermedia filtrando por ambas FK.
-- NOTA: en N:M suele ser más limpio DELETE + INSERT porque la
--       PK compuesta incluye el valor que quieres cambiar.

-- Sintaxis:
-- UPDATE tabla_intermedia
-- SET fk_b = nuevo_id
-- WHERE fk_a = id_a AND fk_b = id_b_viejo;

-- Cambiar el género "Comedia" por "Aventura" en "Avatar":
UPDATE movie_genre
SET genre_id = (SELECT genre_id FROM genres WHERE genre_name = 'Aventura')
WHERE movie_id = (SELECT movie_id FROM movies WHERE title = 'Avatar')
  AND genre_id = (SELECT genre_id FROM genres WHERE genre_name = 'Comedia');


-- -------------------------------------------------------------
-- 4.3 DELETE en N:M
-- -------------------------------------------------------------
-- Para qué: eliminar una o todas las relaciones de un registro.
-- Cuándo: quitar un actor de una película, quitar todos los géneros
--         de una película antes de eliminarla.
-- Cómo: DELETE en la tabla intermedia filtrando por las FK necesarias.

-- Sintaxis — eliminar UNA relación específica:
-- DELETE FROM tabla_intermedia WHERE fk_a = id_a AND fk_b = id_b;

-- Sintaxis — eliminar TODAS las relaciones de un registro:
-- DELETE FROM tabla_intermedia WHERE fk_a = id_a;

-- Eliminar una relación específica (un actor de una película):
DELETE FROM movie_actor
WHERE movie_id = (SELECT movie_id FROM movies WHERE title = 'Avatar')
  AND actor_id = (SELECT people_id FROM people WHERE name = 'Al Pacino');

-- Eliminar todas las relaciones de una película (todos sus actores):
DELETE FROM movie_actor
WHERE movie_id = (SELECT movie_id FROM movies WHERE title = 'Avatar');

-- Eliminar relaciones de múltiples géneros en todas las películas:
DELETE FROM movie_genre
WHERE genre_id IN (
    SELECT genre_id FROM genres WHERE genre_name IN ('Infantil', 'Animación')
);

-- Eliminar una película con todas sus relaciones:
-- Orden: limpiar todas las tablas intermedias, luego la principal
DELETE FROM movie_actor WHERE movie_id = (SELECT movie_id FROM movies WHERE title = 'Avatar');
DELETE FROM movie_genre WHERE movie_id = (SELECT movie_id FROM movies WHERE title = 'Avatar');
DELETE FROM movie_review WHERE movie_id = (SELECT movie_id FROM movies WHERE title = 'Avatar');
DELETE FROM movies WHERE title = 'Avatar';

-- Eliminar películas sin actores NI géneros asociados:
DELETE FROM movies
WHERE movie_id NOT IN (SELECT DISTINCT movie_id FROM movie_actor)
  AND movie_id NOT IN (SELECT DISTINCT movie_id FROM movie_genre);


-- =============================================================
-- 5. TABLA INTERMEDIA CON DATOS PROPIOS
-- =============================================================
-- Para qué: cuando la relación en sí tiene atributos propios.
-- Cuándo: fecha en que se ganó un premio, cantidad de un producto
--         en un pedido, rol de un actor en una película.
-- Cómo: agregar columnas adicionales a la tabla intermedia.

-- Sintaxis:
-- CREATE TABLE tabla_intermedia (
--     fk_a      INT,
--     fk_b      INT,
--     dato_propio TIPO,
--     PRIMARY KEY (fk_a, fk_b),
--     FOREIGN KEY (fk_a) REFERENCES tabla_a(pk),
--     FOREIGN KEY (fk_b) REFERENCES tabla_b(pk)
-- );

-- Tabla intermedia sin datos propios — solo relaciona:
CREATE TABLE movie_award (
    movie_id INT,
    award_id INT,
    PRIMARY KEY (movie_id, award_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (award_id) REFERENCES awards(award_id)
);

-- Tabla intermedia con dato propio — año en que ganó el premio:
CREATE TABLE movie_award_detail (
    movie_id  INT,
    award_id  INT,
    year_won  INT NOT NULL,
    PRIMARY KEY (movie_id, award_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (award_id) REFERENCES awards(award_id)
);

-- INSERT en tabla intermedia con dato propio:
INSERT INTO movie_award (movie_id, award_id)
VALUES (16, 1),   -- Gladiator - Oscar Mejor Película
       (6,  1),   -- Titanic   - Oscar Mejor Película
       (6,  2);   -- Titanic   - Oscar Mejor Director

-- Con subqueries:
INSERT INTO movie_award (movie_id, award_id)
VALUES (
    (SELECT movie_id FROM movies WHERE title = 'Gladiator'),
    (SELECT award_id FROM awards WHERE award_name = 'Oscar Mejor Película')
);


-- =============================================================
-- 6. FLUJO SEGURO PARA OPERACIONES EN TABLAS RELACIONADAS
-- =============================================================

-- ANTES DE INSERT:
-- 1. Verificar que el padre existe
SELECT movie_id FROM movies WHERE title = 'Avatar';
-- 2. Verificar que la relación no existe ya (en N:M)
SELECT * FROM movie_genre WHERE movie_id = 19 AND genre_id = 2;
-- 3. Insertar

-- ANTES DE DELETE en tabla padre:
-- 1. Verificar qué hijos dependen del padre
SELECT * FROM movie_actor  WHERE movie_id = 19;
SELECT * FROM movie_genre  WHERE movie_id = 19;
SELECT * FROM movie_review WHERE movie_id = 19;
-- 2. Eliminar todos los hijos
-- 3. Eliminar el padre

-- ANTES DE UPDATE con FK:
-- 1. Verificar que el nuevo valor referenciado existe
SELECT people_id FROM people WHERE name = 'Ridley Scott';
-- 2. Ejecutar el UPDATE

--------------------------------------------------------------
-- VERIFICAR TODAS LAS RELACIONES DE UN REGISTRO ANTES DE ELIMINAR
-- -------------------------------------------------------------
-- Con ID conocido:
SELECT * FROM tabla_intermedia WHERE fk_columna = id;

-- Con subquery (sin conocer el ID):
SELECT * FROM tabla_intermedia
WHERE fk_columna = (SELECT pk FROM tabla_padre WHERE condición);

-- Ejemplos con cineDB — verificar relaciones de Avatar:
SELECT * FROM movie_actor  WHERE movie_id = (SELECT movie_id FROM movies WHERE title = 'Avatar');
SELECT * FROM movie_genre  WHERE movie_id = (SELECT movie_id FROM movies WHERE title = 'Avatar');
SELECT * FROM movie_review WHERE movie_id = (SELECT movie_id FROM movies WHERE title = 'Avatar');

-- Verificar relaciones de una persona (actor o director):
SELECT * FROM movie_actor WHERE actor_id = (SELECT people_id FROM people WHERE name = 'Al Pacino');
SELECT * FROM movies      WHERE director_id = (SELECT people_id FROM people WHERE name = 'Christopher Nolan');

-- Verificar relaciones de un género:
SELECT * FROM movie_genre WHERE genre_id = (SELECT genre_id FROM genres WHERE genre_name = 'Acción');

-- REGLA: si alguna de estas consultas devuelve filas →
--        debes eliminar esas relaciones antes de eliminar el registro padre.
--        Si todas devuelven 0 filas → puedes eliminar directamente.