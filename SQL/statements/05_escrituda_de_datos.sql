-- =============================================================
-- MYSQL - ESCRITURA DE DATOS
-- INSERT, UPDATE, DELETE
-- Fuentes: MySQL 8.0 Docs + W3Schools
-- Ejemplos sobre cineDB
-- =============================================================
-- Estas tres instrucciones forman el DML (Data Manipulation Language):
-- INSERT → agrega filas nuevas
-- UPDATE → modifica filas existentes
-- DELETE → elimina filas existentes
--
-- REGLA DE ORO: UPDATE y DELETE sin WHERE afectan TODA la tabla.
-- Siempre verifica tu WHERE con un SELECT antes de ejecutar.
-- =============================================================


-- =============================================================
-- 1. INSERT - Insertar datos
-- =============================================================
-- Agrega una o más filas nuevas a una tabla.
-- Cuándo usarlo: registrar un usuario nuevo, agregar un producto,
--               guardar cualquier dato nuevo en el sistema.

-- -------------------------------------------------------------
-- 1.1 Insertar UNA fila (especificando columnas)
-- -------------------------------------------------------------
-- Sintaxis recomendada — siempre especifica las columnas:
-- INSERT INTO tabla (col1, col2, col3) VALUES (val1, val2, val3);
--
-- Ventajas de especificar columnas:
-- → El orden no importa
-- → Puedes omitir columnas opcionales (con DEFAULT o que admiten NULL)
-- → El código no se rompe si la tabla cambia de estructura

INSERT INTO countries (country_name)
VALUES ('Colombia');

INSERT INTO genres (genre_name)
VALUES ('Musical');

INSERT INTO people (name, birth_date, country_of_birth_id, category)
VALUES ('Pedro Almodóvar', '1949-09-25', NULL, 'Director');

-- -------------------------------------------------------------
-- 1.2 Insertar MÚLTIPLES filas en un solo INSERT
-- -------------------------------------------------------------
-- Más eficiente que múltiples INSERT individuales.
-- Cada fila va entre paréntesis, separadas por coma.

INSERT INTO genres (genre_name) VALUES
('Documental'),
('Bélico'),
('Western');

INSERT INTO people (name, birth_date, country_of_birth_id, category) VALUES
('Cate Blanchett', '1969-05-14', 2, 'Actor'),
('Penélope Cruz', '1974-04-28', NULL, 'Actor'),
('Tilda Swinton', '1960-11-05', 14, 'Actor');

-- -------------------------------------------------------------
-- 1.3 Columnas que NO necesitas incluir en el INSERT
-- -------------------------------------------------------------
-- AUTO_INCREMENT (ej: movie_id, people_id) → MySQL lo asigna solo
-- Columnas con DEFAULT definido → toman el valor por defecto
-- Columnas que admiten NULL → quedan como NULL si no las incluyes

-- Esto funciona — movie_id se asigna automáticamente:
INSERT INTO studios (studio_name)
VALUES ('A24');

-- -------------------------------------------------------------
-- 1.4 INSERT con SELECT - Copiar datos de otra tabla
-- -------------------------------------------------------------
-- Inserta el resultado de una consulta como filas nuevas.
-- Cuándo usarlo: migrar datos, hacer copias, poblar tablas derivadas.

-- Copiar solo los directores a una tabla de respaldo (si existiera)
-- INSERT INTO directores_backup (name, birth_date)
-- SELECT name, birth_date FROM people WHERE category = 'Director';

-- PROBAR RESTRICCIÓN UNIQUE con INSERT
-- Si la columna tiene UNIQUE, insertar un valor duplicado da error.
-- Útil para verificar que la restricción está aplicada correctamente.

-- Intento de insertar país duplicado → ERROR:
INSERT INTO cineDB.countries (country_name) VALUES ('Estados Unidos');
-- Error: Duplicate entry 'Estados Unidos' for key 'uq_country'

-- Intento de insertar país nuevo → OK:
INSERT INTO cineDB.countries (country_name) VALUES ('España');

-- =============================================================
-- 2. UPDATE - Modificar datos existentes
-- =============================================================
-- Modifica el valor de una o más columnas en filas existentes.
-- Cuándo usarlo: corregir un dato, actualizar el estado de un
--               registro, cambiar información de un usuario.
--
-- ⚠️ ADVERTENCIA CRÍTICA: si omites el WHERE, se actualizan
--    TODAS las filas de la tabla sin excepción.

-- Sintaxis:
-- UPDATE tabla SET col1 = val1, col2 = val2 WHERE condición;

-- -------------------------------------------------------------
-- 2.1 Actualizar UNA columna en UNA fila (por ID)
-- -------------------------------------------------------------
-- La forma más segura: siempre filtrar por PRIMARY KEY

-- Corregir el año de estreno de una película
UPDATE movies
SET release_year = 1993
WHERE movie_id = 17;

-- Actualizar el nombre de un estudio
UPDATE studios
SET studio_name = '20th Century Studios'
WHERE studio_id = 6;

-- -------------------------------------------------------------
-- 2.2 Actualizar VARIAS columnas a la vez
-- -------------------------------------------------------------
-- Separa los pares col = valor con coma en el SET

UPDATE people
SET birth_date = '1963-06-09',
    country_of_birth_id = 7
WHERE people_id = 30;

-- -------------------------------------------------------------
-- 2.3 Actualizar VARIAS filas con una condición
-- -------------------------------------------------------------
-- Afecta todas las filas que cumplan el WHERE

-- Marcar como NULL el studio_id de películas sin estudio registrado
-- (ejemplo ilustrativo — no cambia nada si ya son NULL)
UPDATE movies
SET studio_id = NULL
WHERE release_year < 1980 AND studio_id IS NOT NULL;

-- -------------------------------------------------------------
-- 2.4 Verificar antes de actualizar
-- -------------------------------------------------------------
-- BUENA PRÁCTICA: antes de ejecutar un UPDATE, corre el SELECT
-- equivalente para confirmar qué filas vas a modificar:

-- Primero verificas:
SELECT * FROM movies WHERE movie_id = 17;
-- Si el resultado es el correcto, entonces actualizas:
UPDATE movies SET release_year = 1993 WHERE movie_id = 17;

-- -------------------------------------------------------------
-- 2.5 Safe Updates en Workbench
-- -------------------------------------------------------------
-- MySQL Workbench tiene activado "Safe Updates" por defecto.
-- Esto bloquea UPDATE y DELETE que no usen la PRIMARY KEY en el WHERE.
-- Si necesitas desactivarlo temporalmente:
SET SQL_SAFE_UPDATES = 0;
-- Tu operación aquí
SET SQL_SAFE_UPDATES = 1;  -- volver a activar siempre
-- Mejor práctica: siempre filtra por PRIMARY KEY y no lo desactives.


-- =============================================================
-- 3. DELETE - Eliminar datos
-- =============================================================
-- Elimina una o más filas de una tabla.
-- Cuándo usarlo: dar de baja un usuario, eliminar un registro
--               obsoleto, limpiar datos de prueba.
--
-- ⚠️ ADVERTENCIA CRÍTICA: DELETE sin WHERE elimina TODAS las filas.
--    A diferencia de TRUNCATE, DELETE puede deshacerse con ROLLBACK
--    si estás dentro de una transacción.

-- Sintaxis:
-- DELETE FROM tabla WHERE condición;

-- -------------------------------------------------------------
-- 3.1 Eliminar UNA fila por ID
-- -------------------------------------------------------------
-- La forma más segura — siempre que sea posible usa la PRIMARY KEY

DELETE FROM genres
WHERE genre_id = 11;  -- el género 'Musical' que insertamos antes

-- -------------------------------------------------------------
-- 3.2 Eliminar VARIAS filas con una condición
-- -------------------------------------------------------------

-- Eliminar todas las personas sin fecha de nacimiento registrada
-- (ejemplo — piénsalo dos veces antes de ejecutar algo así en producción)
DELETE FROM people
WHERE birth_date IS NULL AND category = 'Actor';

-- -------------------------------------------------------------
-- 3.3 Verificar antes de eliminar
-- -------------------------------------------------------------
-- BUENA PRÁCTICA: igual que con UPDATE, primero corre el SELECT

-- Primero verificas qué vas a borrar:
SELECT * FROM genres WHERE genre_id = 11;
-- Si es correcto, entonces eliminas:
DELETE FROM genres WHERE genre_id = 11;

-- -------------------------------------------------------------
-- 3.4 DELETE vs TRUNCATE
-- -------------------------------------------------------------
-- DELETE FROM tabla WHERE condición → elimina filas específicas
-- DELETE FROM tabla                 → elimina TODAS las filas (evitar)
-- TRUNCATE TABLE tabla              → elimina TODAS las filas más rápido,
--                                    resetea el AUTO_INCREMENT, NO se puede
--                                    deshacer con ROLLBACK

-- Cuándo usar cada uno:
-- DELETE  → eliminar filas específicas o cuando necesitas poder deshacer
-- TRUNCATE → vaciar completamente una tabla de datos de prueba


-- =============================================================
-- 4. FOREIGN KEY y restricciones al escribir datos
-- =============================================================
-- Las FOREIGN KEY protegen la integridad de los datos.
-- Esto genera errores comunes al insertar, actualizar o eliminar:

-- ERROR al insertar: si el valor referenciado no existe
-- INSERT INTO movies (..., director_id, ...) VALUES (..., 999, ...)
-- → Error: director_id 999 no existe en people.people_id

-- ERROR al eliminar: si otras tablas referencian ese registro
-- DELETE FROM people WHERE people_id = 59;  -- Christopher Nolan
-- → Error: movies.director_id tiene filas que apuntan a ese people_id

-- Solución: eliminar o actualizar primero las filas dependientes,
-- luego eliminar el registro principal.


-- =============================================================
-- 5. RESUMEN - CUÁNDO USAR CADA UNO
-- =============================================================
--
-- INSERT → dato nuevo que no existía antes
--          registro de usuario, pedido, producto, log de evento
--
-- UPDATE → dato existente que cambió
--          corrección de error, cambio de estado, nueva contraseña
--          SIEMPRE con WHERE — preferiblemente por PRIMARY KEY
--
-- DELETE → dato que ya no debe existir
--          baja de cuenta, limpieza de datos obsoletos
--          SIEMPRE con WHERE — preferiblemente por PRIMARY KEY
--          verificar restricciones de FOREIGN KEY antes de borrar

-- =============================================================
-- 6. FLUJO SEGURO PARA UPDATE Y DELETE
-- =============================================================
-- 1. Escribe el SELECT con el mismo WHERE que usarás
-- 2. Ejecuta el SELECT y verifica que devuelve las filas correctas
-- 3. Cambia SELECT por UPDATE/DELETE
-- 4. Ejecuta

-- Ejemplo:
-- Paso 1 y 2 — verificar:
SELECT * FROM movies WHERE movie_id = 3;
-- Paso 3 y 4 — ejecutar:
UPDATE movies SET total_viewers = 12000000 WHERE movie_id = 3;