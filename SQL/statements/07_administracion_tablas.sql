-- =============================================================
-- MYSQL - ADMINISTRACIÓN DE TABLAS
-- CREATE TABLE, NOT NULL, UNIQUE, PRIMARY KEY, CHECK, DEFAULT,
-- AUTO_INCREMENT, DROP TABLE, ALTER TABLE (ADD, RENAME COLUMN,
-- MODIFY COLUMN, DROP COLUMN)
-- Fuentes: MySQL 8.0 Docs + W3Schools
-- Ejemplos sobre cineDB
-- =============================================================
-- Las instrucciones de esta sección forman el DDL
-- (Data Definition Language) — definen la ESTRUCTURA de la base
-- de datos, no los datos en sí.
-- DDL: CREATE, ALTER, DROP
-- DML (visto antes): INSERT, UPDATE, DELETE
-- =============================================================


-- =============================================================
-- 1. CREATE TABLE - Crear una tabla nueva
-- =============================================================
-- Define la estructura de una tabla: nombre, columnas, tipos de
-- datos y restricciones.
-- Cuándo usarlo: al iniciar un proyecto, al agregar una nueva
-- entidad al sistema.

-- Sintaxis:
-- CREATE TABLE nombre_tabla (
--     columna1 TIPO restricciones,
--     columna2 TIPO restricciones,
--     ...
-- );

-- Tabla simple:
CREATE TABLE awards (
    award_id   INT PRIMARY KEY AUTO_INCREMENT,
    award_name VARCHAR(100)
);

-- Tabla completa con todas las restricciones:
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

-- CREATE TABLE IF NOT EXISTS — no da error si ya existe la tabla
CREATE TABLE IF NOT EXISTS awards (
    award_id   INT PRIMARY KEY AUTO_INCREMENT,
    award_name VARCHAR(100)
);

-- -------------------------------------------------------------
-- DIAGRAMA ENTIDAD-RELACIÓN (ER)
-- -------------------------------------------------------------
-- Es una representación visual de la estructura de la base de datos.
-- Muestra las tablas, sus columnas y cómo se relacionan entre sí.
-- En Workbench se genera con: Database → Reverse Engineer
-- Útil para entender la base de datos antes de escribir queries,
-- especialmente cuando necesitas JOIN entre varias tablas.

-- Símbolos en las líneas de relación:
-- |    → "uno"
-- <    → "muchos"
-- |<   → uno a muchos (una tabla tiene muchas filas en la otra)
-- >|   → muchos a uno
-- Línea continua  → FOREIGN KEY definida formalmente
-- Línea punteada  → relación inferida sin FOREIGN KEY explícita

-- -------------------------------------------------------------
-- COMPONENTES DE UNA TABLA EN CREATE TABLE
-- -------------------------------------------------------------

CREATE TABLE ejemplo_componentes (

    -- INT
    -- Tipo numérico entero. El más común para IDs y contadores.
    -- Rango: -2,147,483,648 a 2,147,483,647
    -- Cuándo: IDs, cantidades, años, contadores
    movie_id INT,

    -- PRIMARY KEY
    -- Identifica de forma única cada fila.
    -- Implica NOT NULL + UNIQUE automáticamente.
    -- Solo puede haber una por tabla.
    -- Cuándo: siempre en la columna ID principal de la tabla
    -- Se puede declarar inline o al final:
    --   inline:  movie_id INT PRIMARY KEY
    --   al final: PRIMARY KEY (movie_id)
    movie_id INT PRIMARY KEY,

    -- AUTO_INCREMENT
    -- MySQL asigna el siguiente número automáticamente al insertar.
    -- Solo funciona con enteros y debe ser PRIMARY KEY o UNIQUE.
    -- El contador nunca retrocede aunque se borren registros.
    -- Cuándo: siempre junto a PRIMARY KEY para IDs
    movie_id INT PRIMARY KEY AUTO_INCREMENT,

    -- VARCHAR(n)
    -- Texto de longitud variable — ocupa solo el espacio necesario.
    -- n = máximo de caracteres permitidos.
    -- Cuándo: nombres, emails, títulos, cualquier texto corto variable
    -- Valores comunes: nombres→100, emails→150, títulos→200, hashes→255
    title VARCHAR(100),

    -- NOT NULL
    -- El campo no puede quedar vacío — es obligatorio al insertar.
    -- Sin NOT NULL, el campo acepta NULL por defecto.
    -- Cuándo: campos que siempre deben tener valor (nombre, email, tipo)
    title VARCHAR(100) NOT NULL,

    -- UNIQUE
    -- Todos los valores de esta columna deben ser diferentes.
    -- Permite NULL (a diferencia de PRIMARY KEY).
    -- Puede haber varias columnas UNIQUE en una tabla.
    -- Cuándo: emails, usernames, códigos — cualquier campo sin duplicados
    email VARCHAR(150) NOT NULL UNIQUE,

    -- DEFAULT valor
    -- Si no se especifica valor al insertar, usa este por defecto.
    -- Cuándo: estados iniciales, timestamps, valores más comunes
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- CHECK (condición)
    -- Rechaza cualquier valor que no cumpla la condición.
    -- Disponible desde MySQL 8.0.16.
    -- Cuándo: rangos numéricos, validaciones de negocio
    rating DECIMAL(3,1) CHECK (rating >= 0 AND rating <= 10),

    -- FOREIGN KEY
    -- Relaciona esta columna con la PRIMARY KEY de otra tabla.
    -- Garantiza integridad referencial: no puedes insertar un valor
    -- que no exista en la tabla referenciada.
    -- Cuándo: siempre que una tabla dependa de datos de otra tabla
    director_id INT,
    FOREIGN KEY (director_id) REFERENCES people(people_id),

    -- PRIMARY KEY compuesta — para tablas de relación (muchos a muchos)
    -- La combinación de las dos columnas debe ser única.
    -- Cuándo: tablas intermedias como movie_actor, movie_genre
    movie_id INT,
    actor_id INT,
    PRIMARY KEY (movie_id, actor_id)
);

-- =============================================================
-- 2. RESTRICCIONES (CONSTRAINTS)
-- =============================================================
-- Las restricciones son reglas que MySQL aplica automáticamente
-- para proteger la integridad de los datos.
-- Se definen al crear la tabla o se agregan después con ALTER TABLE.


-- -------------------------------------------------------------
-- 2.1 NOT NULL - Campo obligatorio
-- -------------------------------------------------------------
-- El campo no puede quedar vacío — siempre debe tener un valor.
-- Cuándo usarlo: campos que son indispensables para el registro
-- (nombre, email, fecha, tipo).
-- Sin NOT NULL, el campo acepta NULL por defecto.

CREATE TABLE ejemplo_not_null (
    id    INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,   -- obligatorio
    notas  TEXT                     -- opcional (puede ser NULL)
);

-- Intento de insertar sin el campo NOT NULL → ERROR:
-- INSERT INTO ejemplo_not_null (notas) VALUES ('algo');
-- Error: Field 'nombre' doesn't have a default value


-- -------------------------------------------------------------
-- 2.2 UNIQUE - Valores únicos
-- -------------------------------------------------------------
-- Todos los valores de esa columna deben ser diferentes entre sí.
-- Cuándo usarlo: emails, usernames, códigos, cualquier campo que
-- no puede repetirse.
-- Diferencia con PRIMARY KEY: puede haber varias columnas UNIQUE
-- en una tabla; PRIMARY KEY solo una.
-- UNIQUE sí permite NULL (a diferencia de PRIMARY KEY).

CREATE TABLE ejemplo_unique (
    id    INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(150) NOT NULL UNIQUE,
    username VARCHAR(50) UNIQUE
);

-- Intento de insertar email repetido → ERROR:
-- INSERT INTO ejemplo_unique (email) VALUES ('test@test.com');
-- INSERT INTO ejemplo_unique (email) VALUES ('test@test.com');
-- Error: Duplicate entry 'test@test.com' for key 'email'


-- -------------------------------------------------------------
-- 2.3 PRIMARY KEY - Llave primaria
-- -------------------------------------------------------------
-- Identifica de forma única cada fila de la tabla.
-- Implica automáticamente: NOT NULL + UNIQUE.
-- Una tabla solo puede tener UNA PRIMARY KEY.
-- Puede ser una sola columna o una combinación (PRIMARY KEY compuesta).

-- PRIMARY KEY en una columna:
CREATE TABLE ejemplo_pk (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title    VARCHAR(100) NOT NULL
);

-- PRIMARY KEY compuesta (combinación de dos columnas — usada en tablas de relación):
CREATE TABLE movie_actor_ejemplo (
    movie_id INT,
    actor_id INT,
    PRIMARY KEY (movie_id, actor_id)  -- la combinación debe ser única
);


-- -------------------------------------------------------------
-- 2.4 CHECK - Validar valores con una condición
-- -------------------------------------------------------------
-- Rechaza cualquier valor que no cumpla la condición definida.
-- Disponible desde MySQL 8.0.16.
-- Cuándo usarlo: rangos numéricos, validaciones de formato simple,
-- restricciones de negocio (edad mínima, rating máximo).

-- Sintaxis:
-- columna TIPO CHECK (condición)
-- o con nombre: CONSTRAINT nombre_constraint CHECK (condición)

CREATE TABLE ejemplo_check (
    id     INT PRIMARY KEY AUTO_INCREMENT,
    rating DECIMAL(3,1) CHECK (rating >= 0 AND rating <= 10),
    age    INT CHECK (age >= 0)
);

-- Con nombre (recomendado — más fácil de identificar en errores):
CREATE TABLE movies_con_rating (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title    VARCHAR(100) NOT NULL,
    rating   DECIMAL(3,1),
    CONSTRAINT chk_rating CHECK (rating >= 0 AND rating <= 10)
);

-- Intento de insertar valor inválido → ERROR:
-- INSERT INTO movies_con_rating (title, rating) VALUES ('Test', 11);
-- Error: Check constraint 'chk_rating' is violated.

-- NOTA: CHECK fue ignorado en versiones anteriores a MySQL 8.0.16.
-- Si usas una versión antigua, MySQL lo parsea pero no lo aplica.


-- -------------------------------------------------------------
-- 2.5 DEFAULT - Valor por defecto
-- -------------------------------------------------------------
-- Si no se especifica un valor al insertar, MySQL usa el DEFAULT.
-- Cuándo usarlo: timestamps de creación, estados iniciales,
-- valores más comunes para un campo.

CREATE TABLE ejemplo_default (
    id         INT PRIMARY KEY AUTO_INCREMENT,
    activo     BOOLEAN NOT NULL DEFAULT TRUE,
    creado_en  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    intentos   INT NOT NULL DEFAULT 0,
    rol        VARCHAR(20) DEFAULT 'viewer'
);

-- Al insertar sin especificar esos campos, toman el DEFAULT:
-- INSERT INTO ejemplo_default (rol) VALUES ('admin');
-- → activo = TRUE, intentos = 0, creado_en = fecha actual


-- -------------------------------------------------------------
-- 2.6 AUTO_INCREMENT - Incremento automático
-- -------------------------------------------------------------
-- MySQL asigna automáticamente el siguiente número al insertar.
-- Solo funciona en columnas numéricas enteras.
-- Siempre va en la columna de PRIMARY KEY.
-- El contador nunca retrocede — si borras el último registro,
-- el siguiente INSERT continúa desde donde quedó.

CREATE TABLE ejemplo_ai (
    id     INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
);

-- Al insertar sin especificar id, MySQL lo asigna:
INSERT INTO ejemplo_ai (nombre) VALUES ('Primero');   -- id = 1
INSERT INTO ejemplo_ai (nombre) VALUES ('Segundo');   -- id = 2
INSERT INTO ejemplo_ai (nombre) VALUES ('Tercero');   -- id = 3


-- =============================================================
-- 3. ALTER TABLE - Modificar una tabla existente
-- =============================================================
-- Permite cambiar la estructura de una tabla después de crearla:
-- agregar, renombrar, modificar o eliminar columnas y restricciones.
-- Cuándo usarlo: cuando los requisitos cambian y la tabla necesita
-- adaptarse sin perder los datos existentes.

-- NOTA IMPORTANTE: en MySQL 8.0 puedes combinar varias operaciones
-- en un solo ALTER TABLE separadas por coma.


-- -------------------------------------------------------------
-- 3.1 ADD - Agregar una columna nueva
-- -------------------------------------------------------------
-- Sintaxis:
-- ALTER TABLE tabla ADD columna TIPO restricciones;
-- ALTER TABLE tabla ADD columna TIPO restricciones AFTER otra_columna;

-- Agregar columna al final de la tabla:
ALTER TABLE movies ADD duration INT;

-- Agregar columna después de una columna específica:
ALTER TABLE movies ADD duration INT AFTER title;

-- Agregar columna con restricciones:
ALTER TABLE movies ADD rating DECIMAL(3,1) CHECK (rating >= 0 AND rating <= 10);

-- Agregar columna NOT NULL con DEFAULT (obligatorio si la tabla tiene datos):
ALTER TABLE movies ADD duration_minutes INT NOT NULL DEFAULT 0;

-- Agregar restricción UNIQUE a una columna existente:
ALTER TABLE countries ADD CONSTRAINT uq_country UNIQUE (country_name);

-- Agregar FOREIGN KEY:
ALTER TABLE movies
ADD CONSTRAINT fk_studio
FOREIGN KEY (studio_id) REFERENCES studios(studio_id);


-- -------------------------------------------------------------
-- 3.2 RENAME COLUMN - Renombrar una columna
-- -------------------------------------------------------------
-- Cambia el nombre de la columna manteniendo el tipo y los datos.
-- Sintaxis:
-- ALTER TABLE tabla RENAME COLUMN nombre_viejo TO nombre_nuevo;

ALTER TABLE movies RENAME COLUMN duration TO duration_minutes;


-- -------------------------------------------------------------
-- 3.3 MODIFY COLUMN - Cambiar tipo o restricciones
-- -------------------------------------------------------------
-- Cambia el tipo de dato, restricciones o valor por defecto
-- de una columna existente.
-- Cuándo usarlo: ampliar VARCHAR, cambiar tipo, agregar DEFAULT,
-- agregar NOT NULL a una columna existente.
-- PRECAUCIÓN: si cambias a un tipo incompatible puedes perder datos.

-- Sintaxis:
-- ALTER TABLE tabla MODIFY COLUMN columna NUEVO_TIPO restricciones;

-- Ampliar VARCHAR de 100 a 80 caracteres:
ALTER TABLE studios MODIFY COLUMN studio_name VARCHAR(80) NOT NULL;

-- Establecer valor DEFAULT en columna existente:
ALTER TABLE movies MODIFY COLUMN duration_minutes INT NOT NULL DEFAULT 0;

-- Agregar NOT NULL a columna que antes aceptaba NULL:
ALTER TABLE awards MODIFY COLUMN award_name VARCHAR(100) NOT NULL UNIQUE;


-- -------------------------------------------------------------
-- 3.4 DROP COLUMN - Eliminar una columna
-- -------------------------------------------------------------
-- Elimina la columna y todos sus datos permanentemente.
-- Cuándo usarlo: limpiar columnas obsoletas, reestructurar la tabla.
-- ⚠️ No se puede deshacer — los datos de esa columna se pierden.

-- Sintaxis:
-- ALTER TABLE tabla DROP COLUMN nombre_columna;

-- Eliminar una columna:
ALTER TABLE movies DROP COLUMN duration_minutes;

-- Eliminar varias columnas en un solo ALTER TABLE:
ALTER TABLE movies DROP COLUMN duration_minutes, DROP COLUMN rating;

-- Eliminar una restricción CHECK por nombre:
ALTER TABLE movies DROP CHECK chk_rating;

-- Eliminar una restricción UNIQUE:
ALTER TABLE countries DROP INDEX uq_country;

-- Eliminar una FOREIGN KEY:
ALTER TABLE movies DROP FOREIGN KEY fk_studio;


-- =============================================================
-- 4. DROP TABLE - Eliminar una tabla
-- =============================================================
-- Elimina la tabla completa: estructura y todos sus datos.
-- Cuándo usarlo: limpiar tablas de prueba, eliminar entidades
-- obsoletas del sistema.
-- ⚠️ Es irreversible — no se puede deshacer.
-- ⚠️ Si otras tablas tienen FOREIGN KEY apuntando a esta tabla,
--    primero debes eliminar esas dependencias.

-- Sintaxis:
-- DROP TABLE nombre_tabla;

DROP TABLE movie_review;

-- DROP TABLE IF EXISTS — no da error si la tabla no existe
-- Diferencia clave con DROP TABLE simple:
--   DROP TABLE tabla           → error si la tabla no existe
--   DROP TABLE IF EXISTS tabla → no hace nada si no existe, sin error
DROP TABLE IF EXISTS movie_review;

-- Eliminar varias tablas a la vez:
DROP TABLE IF EXISTS tabla1, tabla2, tabla3;


-- =============================================================
-- 5. RESUMEN - CUÁNDO USAR CADA INSTRUCCIÓN
-- =============================================================
--
-- CREATE TABLE          → tabla nueva desde cero
-- ALTER TABLE ADD       → agregar columna o restricción a tabla existente
-- ALTER TABLE RENAME    → renombrar columna sin cambiar datos ni tipo
-- ALTER TABLE MODIFY    → cambiar tipo, restricciones o DEFAULT de columna
-- ALTER TABLE DROP      → eliminar columna o restricción (irreversible)
-- DROP TABLE            → eliminar tabla completa (irreversible)
-- DROP TABLE IF EXISTS  → igual pero sin error si no existe — preferir esta


-- =============================================================
-- 6. RESTRICCIONES AL CREAR vs AL MODIFICAR
-- =============================================================
-- Las restricciones se pueden definir de dos formas:

-- Al crear la tabla (CREATE TABLE):
CREATE TABLE productos (
    id       INT PRIMARY KEY AUTO_INCREMENT,
    nombre   VARCHAR(200) NOT NULL,
    precio   DECIMAL(10,2) NOT NULL CHECK (precio >= 0),
    stock    INT NOT NULL DEFAULT 0,
    activo   BOOLEAN NOT NULL DEFAULT TRUE
);

-- Después de crear la tabla (ALTER TABLE):
ALTER TABLE productos ADD CONSTRAINT chk_precio CHECK (precio >= 0);
ALTER TABLE productos MODIFY COLUMN nombre VARCHAR(200) NOT NULL;
ALTER TABLE productos ALTER COLUMN stock SET DEFAULT 0;

-- REGLA PRÁCTICA:
-- Si diseñas la tabla desde cero → define todo en CREATE TABLE
-- Si la tabla ya existe con datos → usa ALTER TABLE para modificar

-- -------------------------------------------------------------
-- VALORES DEFAULT MÁS COMUNES EN MYSQL
-- -------------------------------------------------------------
-- Números:
stock        INT NOT NULL DEFAULT 0
intentos     INT NOT NULL DEFAULT 0
precio       DECIMAL(10,2) NOT NULL DEFAULT 0.00

-- Booleanos:
activo       BOOLEAN NOT NULL DEFAULT TRUE
verificado   BOOLEAN NOT NULL DEFAULT FALSE

-- Texto:
rol          VARCHAR(20) NOT NULL DEFAULT 'viewer'
estado       ENUM('activo','inactivo') NOT NULL DEFAULT 'activo'

-- Fechas y tiempo:
creado_en    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- → se llena automáticamente al hacer INSERT

actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- → se llena al INSERT y se actualiza automáticamente en cada UPDATE

fecha_inicio DATE DEFAULT (CURRENT_DATE)
-- → solo la fecha, sin hora (requiere MySQL 8.0.13+)

-- NULL como DEFAULT explícito (comportamiento por defecto si no se escribe nada):
notas        TEXT DEFAULT NULL
descripcion  VARCHAR(255) DEFAULT NULL

----------------------------------------------------
-- ENUM('valor1', 'valor2', ...)
----------------------------------------------------

    -- Solo acepta uno de los valores listados — MySQL rechaza cualquier
    -- otro valor que no esté en la lista.
    -- Internamente guarda un índice numérico, no el texto —
    -- más eficiente en disco que VARCHAR para opciones fijas.
    -- Cuándo: campos con opciones conocidas y fijas que no van a cambiar
    --         frecuentemente: estados, roles, tipos de operación.
    -- Precaución: agregar un valor nuevo requiere ALTER TABLE.
    -- Ejemplos reales:
    operation_type ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL,
    estado         ENUM('activo', 'inactivo', 'pendiente') NOT NULL DEFAULT 'activo',
    rol            ENUM('admin', 'editor', 'viewer') NOT NULL DEFAULT 'viewer',

    -- TEXT
    -- Texto largo sin límite práctico (hasta ~65,535 bytes).
    -- No puede tener valor DEFAULT.
    -- No se puede usar como PRIMARY KEY ni UNIQUE directamente.
    -- Cuándo: descripciones, comentarios, contenido de artículos,
    --         valores anteriores/nuevos en logs de auditoría.
    -- Diferencia con VARCHAR: VARCHAR tiene límite definido y es
    -- más rápido para búsquedas; TEXT es para contenido largo.
    old_values TEXT,
    new_values TEXT,

    -- TIMESTAMP
    -- Fecha y hora en formato 'YYYY-MM-DD HH:MM:SS'.
    -- Se convierte a UTC al guardar y a hora local al leer.
    -- Rango: 1970-01-01 a 2038-01-19.
    -- Cuándo: registrar cuándo ocurrió algo — creación, modificación,
    --         eventos de auditoría. Ideal para logs.
    -- Diferencia con DATETIME: TIMESTAMP maneja zonas horarias
    -- automáticamente; DATETIME guarda el valor exacto sin conversión.
    change_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- DIFERENCIA VARCHAR vs TEXT
    -- -------------------------------------------------------------
    -- Ambos guardan texto, pero tienen propósitos distintos:
    --
    -- VARCHAR(n):
    --   → Tú defines el límite máximo de caracteres
    --   → Admite DEFAULT, UNIQUE e INDEX
    --   → Más rápido en búsquedas y comparaciones
    --   → Cuándo: textos cortos y predecibles
    --             nombres, emails, títulos, códigos
    --
    -- TEXT:
    --   → Sin límite práctico definido por ti (hasta ~65,535 bytes)
    --   → NO admite DEFAULT
    --   → NO se puede usar como UNIQUE ni INDEX directamente
    --   → Más lento en búsquedas
    --   → Cuándo: textos largos e impredecibles
    --             descripciones, comentarios, contenido de artículos,
    --             logs de auditoría (old_values, new_values)
    --
    -- REGLA PRÁCTICA:
    -- Si sabes el largo máximo y es menor a 255 → VARCHAR(n)
    -- Si el texto puede ser muy largo o no sabes cuánto → TEXT
    
    ----------------------------------------------------------------
    -- DECIMAL(M, D)
    -- -------------------------------------------------------------
    -- Número con decimales EXACTO — no tiene error de redondeo.
    -- M = dígitos totales (incluyendo los decimales)
    -- D = dígitos después del punto decimal
    --
    -- Ejemplos:
    -- DECIMAL(10, 2) → hasta 99,999,999.99  (10 dígitos, 2 decimales)
    -- DECIMAL(15, 2) → hasta 9,999,999,999,999.99 (usado en total_revenue)
    -- DECIMAL(3, 1)  → hasta 9.9             (usado en rating 0.0 a 9.9)
    -- DECIMAL(5, 2)  → hasta 999.99          (porcentajes, tasas)
    --
    -- Cuándo usar DECIMAL:
    --   → Dinero, precios, salarios, recaudaciones
    --   → Ratings y calificaciones
    --   → Cualquier valor donde el redondeo no es aceptable
    --
    -- Cuándo NO usar DECIMAL:
    --   → Coordenadas GPS → usar DOUBLE
    --   → Mediciones científicas → usar FLOAT o DOUBLE
    --   → Esos tipos son aproximados pero más rápidos
    --
    -- REGLA: si el valor involucra dinero → siempre DECIMAL
    --
    -- Ejemplos reales en cineDB:
    total_revenue DECIMAL(15, 2),  -- hasta 9 billones con centavos
    rating        DECIMAL(3, 1),   -- 0.0 a 9.9
    precio        DECIMAL(10, 2),  -- hasta 99,999,999.99
    salario       DECIMAL(8, 2),   -- hasta 999,999.99