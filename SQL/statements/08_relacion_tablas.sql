-- =============================================================
-- MYSQL - RELACIONES ENTRE TABLAS
-- 1:1 (Uno a Uno), 1:N (Uno a Muchos),
-- N:M (Muchos a Muchos), Auto-referencia
-- Fuentes: MySQL 8.0 Docs + W3Schools + GeeksforGeeks
-- =============================================================
-- Las relaciones definen cómo los datos de una tabla se conectan
-- con los datos de otra. Se implementan con FOREIGN KEY.
-- Diseñar bien las relaciones evita datos duplicados y garantiza
-- la integridad de la base de datos.
-- =============================================================


-- =============================================================
-- 1. RELACIÓN 1:1 — Uno a Uno
-- =============================================================
-- Un registro de la tabla A se relaciona con exactamente UN
-- registro de la tabla B, y viceversa.
--
-- CUÁNDO USARLA:
-- → Cuando quieres separar datos sensibles o poco usados de la
--   tabla principal para mantenerla liviana.
-- → Datos que no todos los registros van a tener (opcionales).
-- → Información que se consulta raramente (documentos, detalles).
--
-- EJEMPLOS REALES:
-- → Usuario y su DNI/cédula — un usuario tiene una sola cédula
-- → Usuario y su perfil detallado — separar datos básicos de bio
-- → Empleado y su contrato — no todos tienen contrato activo
-- → Producto y su ficha técnica detallada
--
-- CÓMO SE IMPLEMENTA:
-- La FOREIGN KEY va en la tabla "secundaria" (la que depende).
-- Se agrega UNIQUE a la FOREIGN KEY — eso garantiza que cada
-- valor solo aparezca una vez (convirtiendo 1:N en 1:1).
--
-- Sin UNIQUE en la FK → sería 1:N (un usuario con varios DNI)
-- Con UNIQUE en la FK → es 1:1 (un usuario con un solo DNI)

-- Tabla principal:
CREATE TABLE users (
    user_id  INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email    VARCHAR(150) NOT NULL UNIQUE
);

-- Tabla secundaria con relación 1:1:
CREATE TABLE dni (
    dni_id     INT PRIMARY KEY AUTO_INCREMENT,
    dni_number INT NOT NULL,
    user_id    INT UNIQUE,  -- UNIQUE garantiza la relación 1:1
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
-- Un usuario solo puede tener un DNI (UNIQUE en user_id de dni)
-- Un DNI solo puede pertenecer a un usuario (FK a users)

-- Otro ejemplo — usuario y perfil detallado:
CREATE TABLE user_profiles (
    profile_id   INT PRIMARY KEY AUTO_INCREMENT,
    user_id      INT UNIQUE,  -- UNIQUE = 1:1
    bio          TEXT,
    avatar_url   VARCHAR(255),
    website      VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- DIAGRAMA:
-- users ——|——|—— dni
-- (un usuario tiene exactamente un DNI, un DNI pertenece a un usuario)


-- =============================================================
-- 2. RELACIÓN 1:N — Uno a Muchos
-- =============================================================
-- Un registro de la tabla A puede relacionarse con MUCHOS registros
-- de la tabla B, pero cada registro de B se relaciona con UN SOLO
-- registro de A.
--
-- ES LA RELACIÓN MÁS COMÚN en bases de datos relacionales.
--
-- CUÁNDO USARLA:
-- → Una entidad "padre" tiene múltiples entidades "hijo"
-- → El "hijo" siempre pertenece a un solo "padre"
--
-- EJEMPLOS REALES:
-- → Una empresa tiene muchos empleados (empleado pertenece a una empresa)
-- → Un director dirige muchas películas (película tiene un director)
-- → Un cliente tiene muchos pedidos (pedido pertenece a un cliente)
-- → Una categoría tiene muchos productos
-- → Un país tiene muchas ciudades
--
-- CÓMO SE IMPLEMENTA:
-- La FOREIGN KEY va en la tabla del lado "muchos" (la tabla hijo).
-- NO lleva UNIQUE — eso permite que múltiples filas tengan el mismo valor.
-- La tabla padre tiene la PRIMARY KEY que referencia la FK del hijo.

-- Tabla padre (lado "uno"):
CREATE TABLE companies (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    name       VARCHAR(100) NOT NULL
);

-- Tabla hijo (lado "muchos") — un empleado pertenece a una empresa:
ALTER TABLE users ADD company_id INT;
ALTER TABLE users
ADD CONSTRAINT fk_companies
FOREIGN KEY (company_id) REFERENCES companies(company_id);
-- Una empresa puede tener muchos usuarios (employees)
-- Un usuario solo pertenece a una empresa

-- Ejemplo completo desde cero — director y películas:
-- (ya existe en cineDB: un director dirige muchas películas,
--  pero cada película tiene un solo director)
CREATE TABLE directors (
    director_id INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL
);

CREATE TABLE films (
    film_id     INT PRIMARY KEY AUTO_INCREMENT,
    title       VARCHAR(200) NOT NULL,
    director_id INT,  -- FK sin UNIQUE = 1:N (varios films por director)
    FOREIGN KEY (director_id) REFERENCES directors(director_id)
);

-- DIAGRAMA:
-- companies ||——< users
-- (una empresa tiene muchos usuarios, un usuario pertenece a una empresa)
-- directors ||——< films
-- (un director dirige muchas películas, cada película tiene un director)


-- =============================================================
-- 3. RELACIÓN N:M — Muchos a Muchos
-- =============================================================
-- Un registro de la tabla A puede relacionarse con MUCHOS registros
-- de la tabla B, Y un registro de B puede relacionarse con MUCHOS
-- de A.
--
-- CUÁNDO USARLA:
-- → Cuando ambas entidades pueden tener múltiples relaciones entre sí
--
-- EJEMPLOS REALES:
-- → Un usuario habla muchos idiomas, un idioma lo hablan muchos usuarios
-- → Una película tiene muchos actores, un actor actúa en muchas películas
-- → Un estudiante cursa muchas materias, una materia la cursan muchos estudiantes
-- → Un pedido tiene muchos productos, un producto está en muchos pedidos
-- → Una película tiene muchos géneros, un género tiene muchas películas
--
-- CÓMO SE IMPLEMENTA:
-- Las bases de datos relacionales NO pueden representar N:M directamente.
-- Se necesita una TABLA INTERMEDIA (o tabla de unión/pivote) que:
--   → Tiene una FK a la tabla A
--   → Tiene una FK a la tabla B
--   → Su PRIMARY KEY es la combinación de las dos FK (compuesta)
--   → La combinación garantiza que no se repita la misma relación
--
-- La tabla intermedia puede tener columnas adicionales para
-- guardar datos propios de la relación (fecha, rol, cantidad).

-- Tablas principales:
CREATE TABLE languages (
    language_id INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL
);

-- Tabla intermedia users_languages:
CREATE TABLE users_languages (
    users_language_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id           INT,
    language_id       INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (language_id) REFERENCES languages(language_id),
    UNIQUE (user_id, language_id)  -- evita registrar el mismo par dos veces
);
-- Un usuario puede conocer muchos lenguajes
-- Un lenguaje puede ser conocido por muchos usuarios

-- Ejemplo con PRIMARY KEY compuesta (alternativa — sin ID propio):
CREATE TABLE movie_actor (
    movie_id INT,
    actor_id INT,
    PRIMARY KEY (movie_id, actor_id),  -- compuesta = no se repite el par
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (actor_id) REFERENCES people(people_id)
);

-- Tabla intermedia CON datos propios de la relación:
-- (un actor tiene un personaje específico en cada película)
CREATE TABLE movie_cast (
    movie_id      INT,
    actor_id      INT,
    character_name VARCHAR(100),  -- dato propio de la relación
    is_protagonist BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (actor_id) REFERENCES people(people_id)
);

-- DIAGRAMA:
-- users >——< languages   (a través de users_languages)
-- movies >——< people     (a través de movie_actor)


-- =============================================================
-- 4. AUTO-REFERENCIA (Relación Recursiva)
-- =============================================================
-- Un registro de la tabla A se relaciona con OTRO registro de
-- la misma tabla A.
--
-- CUÁNDO USARLA:
-- → Jerarquías dentro de la misma entidad
-- → Estructuras de árbol o categorías anidadas
--
-- EJEMPLOS REALES:
-- → Empleados y sus jefes (jefe también es empleado)
-- → Categorías con subcategorías (categoría padre)
-- → Comentarios con respuestas (respuesta es un comentario)
-- → Menús de navegación con submenús
-- → Personas que refieren a otras personas (referidos)
--
-- CÓMO SE IMPLEMENTA:
-- La FOREIGN KEY apunta a la PRIMARY KEY de la misma tabla.
-- La columna FK puede ser NULL (para el registro raíz que no
-- tiene padre — el CEO, la categoría principal, etc.).

-- Ejemplo 1 — empleados con jefes (1:N auto-referencia):
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL,
    position    VARCHAR(100),
    manager_id  INT,  -- NULL si es el jefe máximo (CEO)
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);
-- Un empleado tiene un solo jefe (manager_id)
-- Un jefe puede tener muchos empleados a cargo

-- Insertar datos de ejemplo:
INSERT INTO employees (name, position, manager_id) VALUES
('Ana García', 'CEO', NULL),           -- employee_id = 1, sin jefe
('Carlos López', 'CTO', 1),            -- reporta a Ana (id=1)
('María Pérez', 'Backend Dev', 2),     -- reporta a Carlos (id=2)
('Juan Torres', 'Frontend Dev', 2),    -- reporta a Carlos (id=2)
('Laura Gómez', 'Designer', 1);        -- reporta a Ana (id=1)

-- Consultar empleados y sus jefes:
SELECT
    e.name AS empleado,
    e.position AS cargo,
    m.name AS jefe
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;

-- Ejemplo 2 — categorías con subcategorías (1:N auto-referencia):
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL,
    parent_id   INT,  -- NULL si es categoría raíz
    FOREIGN KEY (parent_id) REFERENCES categories(category_id)
);

INSERT INTO categories (name, parent_id) VALUES
('Tecnología', NULL),        -- categoría raíz
('Programación', 1),         -- subcategoría de Tecnología
('Bases de Datos', 1),       -- subcategoría de Tecnología
('MySQL', 3),                -- subcategoría de Bases de Datos
('PostgreSQL', 3);           -- subcategoría de Bases de Datos

-- DIAGRAMA:
-- employees ||——< employees  (un empleado tiene un jefe que también es empleado)
-- categories ||——< categories (una categoría tiene subcategorías que son categorías)


-- =============================================================
-- 5. RESUMEN — CÓMO ELEGIR EL TIPO DE RELACIÓN
-- =============================================================
--
-- Pregunta: ¿cuántos registros de B puede tener un registro de A?
--           ¿y cuántos de A puede tener un registro de B?
--
-- A tiene 1  ←→ B tiene 1   → Relación 1:1
--   Implementación: FK en tabla secundaria + UNIQUE en FK
--   Ejemplo: usuario ←→ DNI
--
-- A tiene 1  ←→ B tiene N   → Relación 1:N
--   Implementación: FK en tabla del lado "muchos" (sin UNIQUE)
--   Ejemplo: empresa ←→ empleados
--
-- A tiene N  ←→ B tiene M   → Relación N:M
--   Implementación: tabla intermedia con FK a ambas tablas
--   Ejemplo: películas ←→ actores (tabla movie_actor)
--
-- A tiene N  ←→ A tiene M   → Auto-referencia
--   Implementación: FK en la misma tabla apuntando a su PK
--   Ejemplo: empleados ←→ jefes (misma tabla employees)
--
-- DIFERENCIA CLAVE 1:1 vs 1:N:
--   La única diferencia técnica es el UNIQUE en la FK.
--   Con UNIQUE → 1:1
--   Sin UNIQUE → 1:N
--
-- TABLA INTERMEDIA en N:M:
--   Puede tener columnas adicionales para datos de la relación.
--   La PK puede ser compuesta (movie_id + actor_id) o
--   tener un ID propio (users_language_id) + UNIQUE en el par.
EOF 