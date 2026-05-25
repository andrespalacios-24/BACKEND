-- =============================================================
-- MYSQL - SELECT
-- Fuentes: MySQL 8.0 Docs + W3Schools
-- =============================================================
-- SELECT es la instrucción más usada en SQL.
-- Sirve para LEER datos de una o más tablas.
-- No modifica nada — solo consulta.
-- =============================================================


-- =============================================================
-- 1. SINTAXIS GENERAL
-- =============================================================
-- El orden de las cláusulas importa — MySQL las procesa en este orden:
--
-- SELECT   columnas
-- FROM     tabla
-- WHERE    condición de filtro
-- ORDER BY columna de ordenamiento
-- LIMIT    cantidad de filas a devolver


-- =============================================================
-- 2. FORMAS BÁSICAS DE SELECT
-- =============================================================

-- Traer TODAS las columnas de la tabla
-- El asterisco (*) significa "todo"
-- Úsalo solo en exploración/desarrollo — en producción especifica columnas
SELECT * FROM users;

-- Traer UNA columna específica
SELECT name FROM users;

-- Traer VARIAS columnas específicas (separadas por coma)
SELECT user_id, name FROM users;
SELECT name, email, age FROM users;

-- Buena práctica en backend: siempre especifica las columnas que necesitas
-- Razones: menos datos transferidos, consultas más rápidas, código más claro


-- =============================================================
-- 3. SELECT DISTINCT - Eliminar duplicados
-- =============================================================
-- Devuelve solo valores únicos, sin repeticiones.
-- Útil cuando una columna puede tener valores repetidos.

-- Sin DISTINCT: si hay 3 usuarios de Medellín, aparece "Medellín" 3 veces
SELECT city FROM users;

-- Con DISTINCT: cada ciudad aparece una sola vez
SELECT DISTINCT city FROM users;

-- Ejemplo real: obtener todos los roles que existen en el sistema
SELECT DISTINCT role FROM users;


-- =============================================================
-- 4. WHERE - Filtrar filas
-- =============================================================
-- WHERE define una condición: solo devuelve las filas que la cumplen.
-- Va después de FROM, antes de ORDER BY.

-- Filtrar por valor exacto (texto va entre comillas simples)
SELECT * FROM users WHERE city = 'Medellín';

-- Filtrar por número (sin comillas)
SELECT * FROM users WHERE age = 30;

-- Operadores de comparación disponibles:
--   =       igual
--   !=  o   <>   distinto
--   >       mayor que
--   <       menor que
--   >=      mayor o igual
--   <=      menor o igual

SELECT * FROM users WHERE age > 25;
SELECT * FROM users WHERE age >= 18;
SELECT * FROM users WHERE age != 30;

-- Combinar condiciones con AND (ambas deben cumplirse)
SELECT * FROM users WHERE age > 18 AND city = 'Bogotá';

-- Combinar condiciones con OR (al menos una debe cumplirse)
SELECT * FROM users WHERE city = 'Cali' OR city = 'Medellín';

-- Negar una condición con NOT
SELECT * FROM users WHERE NOT city = 'Bogotá';

-- Filtrar valores nulos con IS NULL / IS NOT NULL
-- No se puede usar = NULL — siempre IS NULL o IS NOT NULL
SELECT * FROM users WHERE init_date IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;


-- =============================================================
-- 5. ORDER BY - Ordenar resultados
-- =============================================================
-- Ordena las filas del resultado por una o más columnas.
-- ASC  = ascendente (A→Z, 0→9) — es el valor por defecto
-- DESC = descendente (Z→A, 9→0)

-- Ordenar por nombre de forma ascendente (A → Z)
SELECT * FROM users ORDER BY name ASC;

-- Ordenar por edad de forma descendente (mayor → menor)
SELECT * FROM users ORDER BY age DESC;

-- Ordenar por dos columnas:
-- primero por ciudad (A→Z), y si la ciudad es igual, por nombre (A→Z)
SELECT * FROM users ORDER BY city ASC, name ASC;

-- Ejemplo real backend: usuarios más recientes primero
SELECT * FROM users ORDER BY init_date DESC;


-- =============================================================
-- 6. LIMIT - Limitar cantidad de resultados
-- =============================================================
-- Devuelve solo los primeros N resultados.
-- Esencial en backends para no traer miles de filas de golpe (paginación).

-- Solo los primeros 5 usuarios
SELECT * FROM users LIMIT 5;

-- Los 10 usuarios más jóvenes
SELECT * FROM users ORDER BY age ASC LIMIT 10;

-- LIMIT con OFFSET: saltar registros (para paginación)
-- OFFSET indica desde qué registro empezar (empieza en 0)
-- Página 1: registros 1-10   → LIMIT 10 OFFSET 0
-- Página 2: registros 11-20  → LIMIT 10 OFFSET 10
-- Página 3: registros 21-30  → LIMIT 10 OFFSET 20
SELECT * FROM users LIMIT 10 OFFSET 0;   -- página 1
SELECT * FROM users LIMIT 10 OFFSET 10;  -- página 2
SELECT * FROM users LIMIT 10 OFFSET 20;  -- página 3


-- =============================================================
-- 7. AS - Alias (renombrar columnas en el resultado)
-- =============================================================
-- AS le da un nombre temporal a una columna en el resultado.
-- No cambia el nombre en la base de datos — solo en la respuesta.
-- Útil para hacer el resultado más legible o compatible con tu código.

-- Renombrar columnas en el resultado
SELECT name AS nombre, email AS correo FROM users;

-- Muy útil con funciones (los verás más adelante en el curso)
SELECT COUNT(*) AS total_usuarios FROM users;
SELECT MAX(age) AS edad_maxima FROM users;

-- El AS es opcional — también funciona sin él, pero es buena práctica usarlo
SELECT name nombre FROM users;  -- funciona, pero menos legible


-- =============================================================
-- 8. COMBINACIONES COMUNES EN BACKEND
-- =============================================================

-- Buscar un usuario por email (login)
SELECT user_id, name, email FROM users
WHERE email = 'juan@example.com';

-- Listar usuarios activos, ordenados por nombre, con paginación
SELECT user_id, name, email FROM users
WHERE activo = TRUE
ORDER BY name ASC
LIMIT 10 OFFSET 0;

-- Buscar usuarios mayores de edad en una ciudad específica
SELECT name, age, city FROM users
WHERE age >= 18 AND city = 'Medellín'
ORDER BY age DESC;

-- Contar cuántos usuarios hay en total
SELECT COUNT(*) AS total FROM users;

-- Obtener ciudades únicas donde hay usuarios registrados
SELECT DISTINCT city FROM users ORDER BY city ASC;

-- Los 5 usuarios más recientes
SELECT user_id, name, init_date FROM users
ORDER BY init_date DESC
LIMIT 5;


-- =============================================================
-- 9. RESUMEN - ORDEN OBLIGATORIO DE CLÁUSULAS
-- =============================================================
-- Las cláusulas deben ir siempre en este orden:
--
-- SELECT   → qué columnas quieres
-- FROM     → de qué tabla
-- WHERE    → qué filas (filtro)
-- ORDER BY → en qué orden
-- LIMIT    → cuántas filas máximo
--
-- No todas son obligatorias — solo SELECT y FROM son requeridos.
-- Pero cuando las uses, deben ir en ese orden exacto.

-- Ejemplo con todo junto:
SELECT DISTINCT name, city, age
FROM users
WHERE age >= 18 AND city != 'Bogotá'
ORDER BY age DESC, name ASC
LIMIT 20 OFFSET 0;