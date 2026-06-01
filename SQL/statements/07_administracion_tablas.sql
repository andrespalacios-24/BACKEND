-- =============================================================
-- MYSQL - ADMINISTRACIÓN DE TABLAS
-- CREATE TABLE, TIPOS DE DATO, CONSTRAINTS, ALTER TABLE, DROP TABLE
-- Fuentes: MySQL 8.0 Docs + W3Schools
-- Ejemplos sobre cineDB
-- =============================================================
-- DDL (Data Definition Language) — define la ESTRUCTURA de la base
-- de datos, no los datos en sí.
--   DDL: CREATE, ALTER, DROP
--   DML (visto en otros archivos): INSERT, UPDATE, DELETE
-- =============================================================


-- =============================================================
-- 1. TIPOS DE DATO
-- =============================================================
-- Cada columna debe tener un tipo de dato definido.
-- Elegir el tipo correcto afecta espacio en disco, rendimiento
-- y qué valores acepta la columna.


-- -------------------------------------------------------------
-- 1.1 INT
-- -------------------------------------------------------------
-- Número entero. El más común para IDs y contadores.
-- Rango: -2,147,483,648 a 2,147,483,647
-- Ocupa: 4 bytes
-- Cuándo: IDs, cantidades, años, contadores

-- Sintaxis:
-- columna INT
-- columna INT NOT NULL
-- columna INT NOT NULL AUTO_INCREMENT

movie_id   INT,
cantidad   INT NOT NULL DEFAULT 0,
release_year INT,


-- -------------------------------------------------------------
-- 1.2 VARCHAR(n)
-- -------------------------------------------------------------
-- Texto de longitud VARIABLE — ocupa solo el espacio necesario.
-- n = número máximo de caracteres permitidos (tú lo defines).
-- Máximo teórico: 65,535 — en práctica usar valores razonables.
-- Cuándo: nombres, emails, títulos, cualquier texto corto variable.

-- Sintaxis:
-- columna VARCHAR(n)
-- columna VARCHAR(n) NOT NULL

-- Valores comunes en backends:
nombre    VARCHAR(100),   -- nombres de persona
email     VARCHAR(150),   -- emails
titulo    VARCHAR(200),   -- títulos de productos/películas
hash      VARCHAR(255),   -- hashes de contraseña


-- -------------------------------------------------------------
-- 1.3 CHAR(n)
-- -------------------------------------------------------------
-- Texto de longitud FIJA — siempre ocupa exactamente n caracteres.
-- Rellena con espacios si el valor es más corto.
-- Cuándo: datos de longitud siempre igual — códigos, siglas.

codigo_pais   CHAR(2),    -- 'CO', 'US'
codigo_postal CHAR(6),


-- -------------------------------------------------------------
-- 1.4 TEXT
-- -------------------------------------------------------------
-- Texto largo sin límite práctico definido por ti (hasta ~65,535 bytes).
-- NO admite DEFAULT.
-- NO se puede usar como UNIQUE ni INDEX directamente.
-- Cuándo: descripciones, comentarios, contenido largo,
--         logs de auditoría (old_values, new_values).

-- Sintaxis:
-- columna TEXT
-- columna TEXT NULL   (acepta NULL — comportamiento por defecto)

old_values  TEXT,
descripcion TEXT,

-- Variantes para textos más grandes:
-- TINYTEXT   → hasta 255 bytes
-- TEXT       → hasta 65,535 bytes  (el más usado)
-- MEDIUMTEXT → hasta 16 MB
-- LONGTEXT   → hasta 4 GB

-- DIFERENCIA VARCHAR vs TEXT:
-- VARCHAR(n):
--   → Tú defines el límite máximo
--   → Admite DEFAULT, UNIQUE e INDEX
--   → Más rápido en búsquedas
--   → Cuándo: textos cortos y predecibles (nombres, emails, títulos)
-- TEXT:
--   → Sin límite definido por ti
--   → NO admite DEFAULT ni UNIQUE
--   → Más lento en búsquedas
--   → Cuándo: textos largos e impredecibles
-- REGLA: si sabes el largo máximo y es menor a 255 → VARCHAR(n)
--        si el texto puede ser muy largo o no sabes cuánto → TEXT


-- -------------------------------------------------------------
-- 1.5 DECIMAL(M, D)
-- -------------------------------------------------------------
-- Número con decimales EXACTO — sin error de redondeo.
-- M = dígitos TOTALES (incluyendo decimales)
-- D = dígitos DESPUÉS del punto decimal
-- Dígitos antes del punto = M - D
-- Cuándo: dinero, precios, salarios, ratings — donde el redondeo
--         no es aceptable.

-- Sintaxis:
-- columna DECIMAL(M, D)

-- Cómo leer DECIMAL(M, D):
-- DECIMAL(10, 2) → 8 antes del punto + 2 decimales → hasta 99,999,999.99
-- DECIMAL(15, 2) → 13 antes + 2 decimales → hasta 9,999,999,999,999.99
-- DECIMAL(4, 1)  → 3 antes + 1 decimal → hasta 999.9  (para ratings 0-10)
-- DECIMAL(5, 2)  → 3 antes + 2 decimales → hasta 999.99

-- Ejemplos reales en cineDB:
total_revenue DECIMAL(15, 2),  -- recaudación en millones
rating        DECIMAL(4, 1),   -- rating 0.0 a 10.0
precio        DECIMAL(10, 2),  -- hasta 99,999,999.99
salario       DECIMAL(8, 2),   -- hasta 999,999.99

-- Cuándo NO usar DECIMAL:
--   → Coordenadas GPS → usar DOUBLE
--   → Mediciones científicas → usar FLOAT o DOUBLE
--   → Son aproximados pero más rápidos para cálculos científicos
-- REGLA: si el valor involucra dinero → siempre DECIMAL


-- -------------------------------------------------------------
-- 1.6 BOOLEAN
-- -------------------------------------------------------------
-- MySQL no tiene tipo BOOLEAN nativo.
-- BOOLEAN y BOOL son sinónimos de TINYINT(1).
-- 0 = FALSE, 1 = TRUE.
-- Cuándo: campos de verdadero/falso — activo, verificado, publicado.

activo         BOOLEAN NOT NULL DEFAULT TRUE,
email_verificado BOOLEAN NOT NULL DEFAULT FALSE,


-- -------------------------------------------------------------
-- 1.7 DATE, DATETIME, TIMESTAMP
-- -------------------------------------------------------------

-- DATE → solo fecha 'YYYY-MM-DD'
-- Cuándo: cumpleaños, fecha de contrato, fecha de entrega
birth_date    DATE,
fecha_contrato DATE,

-- DATETIME → fecha y hora 'YYYY-MM-DD HH:MM:SS'
-- No cambia con zona horaria. Cuándo: registrar un evento exacto.
creado_en     DATETIME,

-- TIMESTAMP → igual en formato, pero:
--   → Se convierte a UTC al guardar, a hora local al leer
--   → Rango: 1970-01-01 a 2038-01-19
--   → Ideal para logs y auditoría
-- Cuándo: registrar cuándo se creó o modificó un registro
creado_en      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

-- DIFERENCIA DATETIME vs TIMESTAMP:
-- DATETIME  → guarda el valor exacto sin conversión de zona horaria
-- TIMESTAMP → maneja zonas horarias automáticamente (mejor para apps globales)


-- -------------------------------------------------------------
-- 1.8 ENUM('valor1', 'valor2', ...)
-- -------------------------------------------------------------
-- Solo acepta uno de los valores listados.
-- MySQL rechaza cualquier otro valor que no esté en la lista.
-- Internamente guarda un índice numérico — más eficiente que VARCHAR
-- para opciones fijas.
-- Cuándo: campos con opciones conocidas y fijas (estados, roles, tipos).
-- Precaución: agregar un valor nuevo requiere ALTER TABLE.

-- Sintaxis:
-- columna ENUM('val1', 'val2', 'val3') NOT NULL DEFAULT 'val1'

operation_type ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL,
estado         ENUM('activo', 'inactivo', 'pendiente') NOT NULL DEFAULT 'activo',
rol            ENUM('admin', 'editor', 'viewer') NOT NULL DEFAULT 'viewer',


-- =============================================================
-- 2. CONSTRAINTS (RESTRICCIONES)
-- =============================================================
-- Reglas que MySQL aplica automáticamente para proteger la
-- integridad de los datos.
-- Se definen al crear la tabla o se agregan después con ALTER TABLE.
-- Pueden tener nombre (con CONSTRAINT) o ser anónimas.


-- -------------------------------------------------------------
-- 2.1 NOT NULL
-- -------------------------------------------------------------
-- El campo no puede quedar vacío — es obligatorio al insertar.
-- Sin NOT NULL, el campo acepta NULL por defecto.
-- Cuándo: campos que siempre deben tener valor (nombre, email, tipo).

-- Sintaxis:
-- columna TIPO NOT NULL

-- En CREATE TABLE:
nombre VARCHAR(100) NOT NULL,
email  VARCHAR(150) NOT NULL,

-- Con ALTER TABLE (agregar a columna existente):
-- ALTER TABLE tabla MODIFY COLUMN columna TIPO NOT NULL;
ALTER TABLE people MODIFY COLUMN name VARCHAR(100) NOT NULL;

-- Intento de insertar sin el campo NOT NULL → ERROR:
-- INSERT INTO tabla (otro_campo) VALUES ('algo');
-- Error: Field 'nombre' doesn't have a default value


-- -------------------------------------------------------------
-- 2.2 UNIQUE
-- -------------------------------------------------------------
-- Todos los valores de esa columna deben ser diferentes entre sí.
-- Permite NULL (a diferencia de PRIMARY KEY).
-- Puede haber varias columnas UNIQUE en una tabla.
-- Cuándo: emails, usernames, códigos — cualquier campo sin duplicados.

-- Sintaxis inline (sin nombre):
-- columna TIPO UNIQUE

-- Sintaxis con nombre (recomendada — más fácil de eliminar después):
-- CONSTRAINT nombre_unique UNIQUE (columna)
-- o con ALTER TABLE: ADD CONSTRAINT nombre UNIQUE (columna)

-- En CREATE TABLE inline:
email VARCHAR(150) NOT NULL UNIQUE,

-- En CREATE TABLE con nombre:
email VARCHAR(150) NOT NULL,
CONSTRAINT uq_email UNIQUE (email),

-- Con ALTER TABLE:
ALTER TABLE countries ADD CONSTRAINT uq_country UNIQUE (country_name);

-- Eliminar un UNIQUE por nombre:
ALTER TABLE countries DROP INDEX uq_country;

-- Intento de insertar valor repetido → ERROR:
-- Error: Duplicate entry 'test@test.com' for key 'email'


-- -------------------------------------------------------------
-- 2.3 PRIMARY KEY
-- -------------------------------------------------------------
-- Identifica de forma única cada fila de la tabla.
-- Implica automáticamente: NOT NULL + UNIQUE.
-- Solo puede haber UNA PRIMARY KEY por tabla.
-- Cuándo: siempre en la columna ID principal de la tabla.

-- Sintaxis inline:
-- columna INT PRIMARY KEY AUTO_INCREMENT

-- Sintaxis al final (necesaria para PRIMARY KEY compuesta):
-- PRIMARY KEY (columna)
-- PRIMARY KEY (col1, col2)  ← compuesta

-- PRIMARY KEY simple:
movie_id INT PRIMARY KEY AUTO_INCREMENT,

-- PRIMARY KEY compuesta (tablas de relación muchos a muchos):
-- La combinación de columnas debe ser única — ni movie_id ni actor_id
-- solos necesitan ser únicos, pero el par sí.
movie_id INT,
actor_id INT,
PRIMARY KEY (movie_id, actor_id),


-- -------------------------------------------------------------
-- 2.4 FOREIGN KEY
-- -------------------------------------------------------------
-- Relaciona una columna con la PRIMARY KEY de otra tabla.
-- Garantiza integridad referencial: no puedes insertar un valor
-- que no exista en la tabla referenciada.
-- Cuándo: siempre que una tabla dependa de datos de otra.

-- Sintaxis en CREATE TABLE:
-- CONSTRAINT nombre_fk FOREIGN KEY (columna_local) REFERENCES tabla(columna)

-- Sintaxis con ALTER TABLE:
-- ALTER TABLE tabla ADD CONSTRAINT nombre_fk
-- FOREIGN KEY (columna_local) REFERENCES otra_tabla(columna);

-- En CREATE TABLE:
director_id INT,
CONSTRAINT fk_director FOREIGN KEY (director_id) REFERENCES people(people_id),

-- Con ALTER TABLE:
ALTER TABLE movies
ADD CONSTRAINT fk_studio
FOREIGN KEY (studio_id) REFERENCES studios(studio_id);

-- Eliminar una FOREIGN KEY:
ALTER TABLE movies DROP FOREIGN KEY fk_studio;

-- ERROR al insertar valor inexistente:
-- INSERT INTO movies (director_id) VALUES (999);
-- Error: Cannot add or update a child row: foreign key constraint fails

-- ERROR al eliminar registro referenciado por otra tabla:
-- DELETE FROM people WHERE people_id = 59;
-- Error: Cannot delete a parent row: foreign key constraint fails
-- Solución: eliminar primero las filas dependientes, luego el registro.


-- -------------------------------------------------------------
-- 2.5 CHECK
-- -------------------------------------------------------------
-- Rechaza cualquier valor que no cumpla la condición definida.
-- Disponible desde MySQL 8.0.16 (antes se parseaba pero se ignoraba).
-- Cuándo: rangos numéricos, validaciones de negocio.

-- Sintaxis inline (sin nombre):
-- columna TIPO CHECK (condición)

-- Sintaxis con nombre (recomendada):
-- CONSTRAINT nombre_check CHECK (condición)

-- En CREATE TABLE inline:
rating DECIMAL(4,1) CHECK (rating >= 0 AND rating <= 10),
age    INT CHECK (age >= 0),

-- En CREATE TABLE con nombre:
rating DECIMAL(4,1),
CONSTRAINT chk_rating CHECK (rating >= 0 AND rating <= 10),

-- Con ALTER TABLE:
ALTER TABLE movies ADD CONSTRAINT chk_rating CHECK (rating >= 0 AND rating <= 10);

-- Eliminar un CHECK por nombre:
ALTER TABLE movies DROP CHECK chk_rating;

-- ERROR al insertar valor inválido:
-- INSERT INTO movies (rating) VALUES (11);
-- Error: Check constraint 'chk_rating' is violated.


-- -------------------------------------------------------------
-- 2.6 DEFAULT
-- -------------------------------------------------------------
-- Si no se especifica un valor al insertar, MySQL usa el DEFAULT.
-- Cuándo: estados iniciales, timestamps automáticos, valores comunes.

-- Sintaxis:
-- columna TIPO DEFAULT valor
-- columna TIPO NOT NULL DEFAULT valor

-- Valores DEFAULT más comunes:

-- Números:
stock    INT NOT NULL DEFAULT 0,
intentos INT NOT NULL DEFAULT 0,
precio   DECIMAL(10,2) NOT NULL DEFAULT 0.00,

-- Booleanos:
activo     BOOLEAN NOT NULL DEFAULT TRUE,
verificado BOOLEAN NOT NULL DEFAULT FALSE,

-- Texto:
rol    VARCHAR(20) NOT NULL DEFAULT 'viewer',
estado ENUM('activo','inactivo') NOT NULL DEFAULT 'activo',

-- Fechas y tiempo:
creado_en      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- → se llena automáticamente al hacer INSERT

actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
-- → se llena al INSERT y se actualiza automáticamente en cada UPDATE

fecha_inicio   DATE DEFAULT (CURRENT_DATE),
-- → solo la fecha sin hora (requiere MySQL 8.0.13+)

-- NULL explícito (comportamiento por defecto si no se escribe nada):
notas       TEXT DEFAULT NULL,
descripcion VARCHAR(255) DEFAULT NULL,

-- Con ALTER TABLE (cambiar o agregar DEFAULT a columna existente):
ALTER TABLE movies MODIFY COLUMN duration_minutes INT NOT NULL DEFAULT 0;


-- -------------------------------------------------------------
-- 2.7 AUTO_INCREMENT
-- -------------------------------------------------------------
-- MySQL asigna automáticamente el siguiente número al insertar.
-- Solo funciona con columnas numéricas enteras.
-- Siempre va junto a PRIMARY KEY.
-- El contador nunca retrocede — si borras el último registro,
-- el siguiente INSERT continúa desde donde quedó.

-- Sintaxis:
-- columna INT PRIMARY KEY AUTO_INCREMENT

id INT PRIMARY KEY AUTO_INCREMENT,

-- Al insertar no especificas el ID — MySQL lo asigna solo:
INSERT INTO studios (studio_name) VALUES ('A24');        -- id = 11
INSERT INTO studios (studio_name) VALUES ('Blumhouse');  -- id = 12


-- -------------------------------------------------------------
-- 2.8 ADD CONSTRAINT - Agregar restricción con nombre
-- -------------------------------------------------------------
-- Permite agregar cualquier restricción (UNIQUE, CHECK, FOREIGN KEY)
-- con un nombre propio a una tabla existente.
-- Cuándo usarlo: cuando la tabla ya existe y necesitas agregar
--               una restricción sin recrear la tabla.
-- Ventaja del nombre: puedes eliminarla fácilmente referenciándola
--                     por ese nombre con DROP.

-- Convención de nombres:
-- uq_  → UNIQUE       (ej: uq_country, uq_email)
-- fk_  → FOREIGN KEY  (ej: fk_studio, fk_director)
-- chk_ → CHECK        (ej: chk_rating, chk_precio)
-- pk_  → PRIMARY KEY  (ej: pk_movie_actor)

-- Sintaxis:
-- ALTER TABLE tabla ADD CONSTRAINT nombre UNIQUE (columna);
-- ALTER TABLE tabla ADD CONSTRAINT nombre CHECK (condición);
-- ALTER TABLE tabla ADD CONSTRAINT nombre FOREIGN KEY (col) REFERENCES tabla(col);

-- Ejemplos:
ALTER TABLE countries ADD CONSTRAINT uq_country UNIQUE (country_name);
ALTER TABLE movies ADD CONSTRAINT chk_rating CHECK (rating >= 0 AND rating <= 10);
ALTER TABLE movies ADD CONSTRAINT fk_studio FOREIGN KEY (studio_id) REFERENCES studios(studio_id);

-- Eliminar según el tipo:
ALTER TABLE countries DROP INDEX uq_country;       -- UNIQUE
ALTER TABLE movies DROP CHECK chk_rating;          -- CHECK
ALTER TABLE movies DROP FOREIGN KEY fk_studio;     -- FOREIGN KEY


-- =============================================================
-- 3. CREATE TABLE - Crear una tabla nueva
-- =============================================================
-- Define la estructura completa: columnas, tipos y restricciones.
-- Cuándo usarlo: al iniciar un proyecto, al agregar una entidad nueva.

-- Sintaxis:
-- CREATE TABLE nombre_tabla (
--     columna1 TIPO restricciones,
--     columna2 TIPO restricciones,
--     CONSTRAINT nombre TIPO (columna)   ← restricciones al final
-- );

-- Tabla simple:
CREATE TABLE awards (
    award_id   INT PRIMARY KEY AUTO_INCREMENT,
    award_name VARCHAR(100) NOT NULL UNIQUE
);

-- Tabla con todas las restricciones — ejemplo real (audit_log):
CREATE TABLE audit_log (
    audit_id         INT PRIMARY KEY AUTO_INCREMENT,
    table_name       VARCHAR(100) NOT NULL,
    operation_type   ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL,
    record_id        INT NOT NULL,
    changed_by       VARCHAR(100) NOT NULL,
    change_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    old_values       TEXT,
    new_values       TEXT
);

-- CREATE TABLE IF NOT EXISTS — no da error si la tabla ya existe:
CREATE TABLE IF NOT EXISTS awards (
    award_id   INT PRIMARY KEY AUTO_INCREMENT,
    award_name VARCHAR(100) NOT NULL UNIQUE
);

-- Tabla con FOREIGN KEY y CHECK — ejemplo completo:
CREATE TABLE movies_ejemplo (
    movie_id      INT PRIMARY KEY AUTO_INCREMENT,
    title         VARCHAR(100) NOT NULL,
    release_year  INT,
    director_id   INT,
    studio_id     INT,
    rating        DECIMAL(4,1),
    activo        BOOLEAN NOT NULL DEFAULT TRUE,
    creado_en     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_rating   CHECK (rating >= 0 AND rating <= 10),
    CONSTRAINT fk_director  FOREIGN KEY (director_id) REFERENCES people(people_id),
    CONSTRAINT fk_studio    FOREIGN KEY (studio_id) REFERENCES studios(studio_id)
);

-- Tabla de relación con PRIMARY KEY compuesta:
CREATE TABLE movie_actor (
    movie_id INT,
    actor_id INT,
    PRIMARY KEY (movie_id, actor_id),
    CONSTRAINT fk_ma_movie FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    CONSTRAINT fk_ma_actor FOREIGN KEY (actor_id) REFERENCES people(people_id)
);


-- =============================================================
-- 4. ALTER TABLE - Modificar una tabla existente
-- =============================================================
-- Cambia la estructura de una tabla sin perder los datos existentes.
-- Cuándo usarlo: cuando los requisitos cambian después de crear la tabla.
-- En MySQL 8.0 puedes combinar varias operaciones separadas por coma.

-- Sintaxis general:
-- ALTER TABLE tabla OPERACIÓN;


-- -------------------------------------------------------------
-- 4.1 ADD - Agregar columna nueva
-- -------------------------------------------------------------
-- Sintaxis:
-- ALTER TABLE tabla ADD columna TIPO restricciones;
-- ALTER TABLE tabla ADD columna TIPO restricciones AFTER otra_columna;

-- Al final de la tabla:
ALTER TABLE movies ADD duration_minutes INT;

-- Después de una columna específica:
ALTER TABLE movies ADD duration_minutes INT AFTER title;

-- Con restricciones:
ALTER TABLE movies ADD rating DECIMAL(4,1) CHECK (rating >= 0 AND rating <= 10);

-- NOT NULL con DEFAULT (obligatorio si la tabla ya tiene datos):
ALTER TABLE movies ADD duration_minutes INT NOT NULL DEFAULT 0;

-- PRECAUCIÓN al agregar NOT NULL sin DEFAULT en tabla con datos:
-- MySQL no sabe qué valor poner en las filas existentes → ERROR.
-- Solución: siempre agregar DEFAULT cuando la tabla ya tiene filas.


-- -------------------------------------------------------------
-- 4.2 RENAME COLUMN - Renombrar columna
-- -------------------------------------------------------------
-- Cambia el nombre manteniendo el tipo, datos y restricciones.
-- Sintaxis:
-- ALTER TABLE tabla RENAME COLUMN nombre_viejo TO nombre_nuevo;

ALTER TABLE movies RENAME COLUMN duration TO duration_minutes;


-- -------------------------------------------------------------
-- 4.3 MODIFY COLUMN - Cambiar tipo o restricciones
-- -------------------------------------------------------------
-- Cambia el tipo de dato, restricciones o DEFAULT de una columna.
-- IMPORTANTE: debes escribir el tipo completo con TODAS las
--             restricciones que quieres conservar — las que omitas
--             se pierden.
-- PRECAUCIÓN: cambiar a tipo incompatible puede causar pérdida de datos.

-- Sintaxis:
-- ALTER TABLE tabla MODIFY COLUMN columna NUEVO_TIPO restricciones;

-- Ampliar VARCHAR:
ALTER TABLE studios MODIFY COLUMN studio_name VARCHAR(80) NOT NULL;

-- Agregar DEFAULT:
ALTER TABLE movies MODIFY COLUMN duration_minutes INT NOT NULL DEFAULT 0;

-- Agregar NOT NULL (requiere que no haya NULLs en la columna):
-- Flujo seguro cuando ya hay datos:
SET SQL_SAFE_UPDATES = 0;
UPDATE movies SET duration_minutes = 0 WHERE duration_minutes IS NULL;
SET SQL_SAFE_UPDATES = 1;
ALTER TABLE movies MODIFY COLUMN duration_minutes INT NOT NULL DEFAULT 0;

-- Agregar UNIQUE a columna existente:
ALTER TABLE awards MODIFY COLUMN award_name VARCHAR(100) NOT NULL UNIQUE;

-- Agregar CHECK a columna existente:
ALTER TABLE movies MODIFY COLUMN rating DECIMAL(4,1) CHECK (rating >= 0 AND rating <= 10);

-- Cambiar ENUM agregando un nuevo valor:
ALTER TABLE audit_log MODIFY COLUMN operation_type 
ENUM('INSERT', 'UPDATE', 'DELETE', 'SELECT') NOT NULL;

-- Cambiar VARCHAR a TEXT (cuando el contenido creció más de lo esperado):
ALTER TABLE movies MODIFY COLUMN title TEXT NOT NULL;

-- RECORDATORIO: siempre reescribir TODAS las restricciones.
-- Si la columna tenía NOT NULL y solo pones el tipo → pierde NOT NULL.
-- Incorrecto — pierde NOT NULL:
-- ALTER TABLE studios MODIFY COLUMN studio_name VARCHAR(80);
-- Correcto — conserva NOT NULL:
-- ALTER TABLE studios MODIFY COLUMN studio_name VARCHAR(80) NOT NULL;

-- -------------------------------------------------------------
-- FLUJO PARA LIMPIAR NULL ANTES DE APLICAR NOT NULL O UNIQUE
-- -------------------------------------------------------------
-- Cuando una columna ya tiene NULLs guardados y necesitas aplicar
-- NOT NULL o UNIQUE, MySQL rechaza la operación.
-- Debes limpiar los NULLs primero según el tipo de dato.

-- PASO 1: verificar qué filas tienen NULL
SELECT * FROM tabla WHERE columna IS NULL;

-- PASO 2: desactivar Safe Updates si no filtras por PRIMARY KEY
SET SQL_SAFE_UPDATES = 0;

-- PASO 3: limpiar según el tipo de dato

-- INT → reemplazar con 0 o el valor que tenga sentido
UPDATE movies SET duration_minutes = 0 WHERE duration_minutes IS NULL;

-- VARCHAR / CHAR → reemplazar con texto vacío o valor por defecto
UPDATE awards SET award_name = 'Sin nombre' WHERE award_name IS NULL;
UPDATE studios SET studio_name = 'Desconocido' WHERE studio_name IS NULL;

-- DECIMAL → reemplazar con 0.00
UPDATE movies SET rating = 0.0 WHERE rating IS NULL;
UPDATE movies SET total_revenue = 0.00 WHERE total_revenue IS NULL;

-- BOOLEAN → reemplazar con TRUE o FALSE según el caso
UPDATE tabla SET activo = FALSE WHERE activo IS NULL;

-- DATE / DATETIME / TIMESTAMP → reemplazar con fecha conocida
UPDATE people SET birth_date = '1900-01-01' WHERE birth_date IS NULL;

-- ENUM → reemplazar con uno de los valores válidos del ENUM
UPDATE audit_log SET operation_type = 'INSERT' WHERE operation_type IS NULL;

-- TEXT → reemplazar con texto vacío (TEXT no admite DEFAULT)
UPDATE movies SET descripcion = '' WHERE descripcion IS NULL;

-- PASO 4: volver a activar Safe Updates
SET SQL_SAFE_UPDATES = 1;

-- PASO 5: aplicar la restricción
ALTER TABLE tabla MODIFY COLUMN columna TIPO NOT NULL;
ALTER TABLE tabla MODIFY COLUMN columna TIPO NOT NULL UNIQUE;

-- ALTERNATIVA: si las filas con NULL no sirven, eliminarlas
-- en lugar del UPDATE del paso 3:
DELETE FROM awards WHERE award_name IS NULL;

-- NOTA: para UNIQUE además de limpiar NULL debes verificar
-- que no haya valores repetidos en la columna:
SELECT columna, COUNT(*) FROM tabla GROUP BY columna HAVING COUNT(*) > 1;
-- Si hay duplicados, corrígelos antes de aplicar UNIQUE.

-- -------------------------------------------------------------
-- 4.4 DROP COLUMN - Eliminar columna
-- -------------------------------------------------------------
-- Elimina la columna y todos sus datos permanentemente.
-- ⚠️ Irreversible — los datos de esa columna se pierden.

-- Sintaxis:
-- ALTER TABLE tabla DROP COLUMN nombre_columna;

-- Una columna:
ALTER TABLE movies DROP COLUMN duration_minutes;

-- Varias columnas en un solo ALTER TABLE:
ALTER TABLE movies DROP COLUMN duration_minutes, DROP COLUMN rating;


-- =============================================================
-- 5. DROP TABLE - Eliminar tabla completa
-- =============================================================
-- Elimina la tabla: estructura y todos sus datos.
-- ⚠️ Irreversible.
-- ⚠️ Si otras tablas tienen FOREIGN KEY apuntando a esta,
--    primero debes eliminar esas dependencias.

-- Sintaxis:
-- DROP TABLE tabla;
-- DROP TABLE IF EXISTS tabla;

DROP TABLE movie_review;

-- IF EXISTS — no da error si la tabla no existe:
-- Sin IF EXISTS → error si la tabla no existe
-- Con IF EXISTS → no hace nada si no existe, sin error
-- PREFERIR siempre IF EXISTS
DROP TABLE IF EXISTS movie_review;

-- Varias tablas a la vez:
DROP TABLE IF EXISTS tabla1, tabla2, tabla3;


-- =============================================================
-- 6. DIAGRAMA ENTIDAD-RELACIÓN (ER)
-- =============================================================
-- Representación visual de la estructura de la base de datos.
-- Muestra tablas, columnas y relaciones entre ellas.
-- En Workbench: Database → Reverse Engineer
-- Útil antes de escribir queries con JOIN — te muestra qué tablas
-- necesitas unir y por qué columnas.

-- Símbolos en las líneas de relación:
-- |    → "uno"
-- <    → "muchos"
-- |<   → uno a muchos (un estudio tiene muchas películas)
-- >|   → muchos a uno
-- Línea continua  → FOREIGN KEY definida formalmente
-- Línea punteada  → relación inferida sin FOREIGN KEY explícita


-- =============================================================
-- 7. RESUMEN - CUÁNDO USAR CADA INSTRUCCIÓN
-- =============================================================
--
-- CREATE TABLE          → tabla nueva desde cero
-- CREATE TABLE IF NOT EXISTS → igual, sin error si ya existe
-- ALTER TABLE ADD       → agregar columna o restricción a tabla existente
-- ALTER TABLE RENAME    → renombrar columna sin cambiar datos ni tipo
-- ALTER TABLE MODIFY    → cambiar tipo, restricciones o DEFAULT
--                         ojo: reescribir TODAS las restricciones
-- ALTER TABLE DROP      → eliminar columna o restricción (irreversible)
-- DROP TABLE            → eliminar tabla completa (irreversible)
-- DROP TABLE IF EXISTS  → igual pero sin error si no existe
--
-- UPDATE vs ALTER TABLE MODIFY:
--   UPDATE        → modifica los DATOS dentro de las filas
--   ALTER MODIFY  → modifica la ESTRUCTURA de la columna
--
-- CONSTRAINT con nombre vs sin nombre:
--   Sin nombre  → MySQL asigna nombre automático difícil de recordar
--   Con nombre  → tú controlas el nombre, fácil de eliminar después
--   CONVENCIÓN: uq_ / fk_ / chk_ según el tipo