-- =============================================================
-- MYSQL - JOIN
-- INNER JOIN, LEFT JOIN, RIGHT JOIN, UNION, UNION ALL
-- Fuentes: MySQL 8.0 Docs + W3Schools
-- =============================================================
-- JOIN combina filas de dos o más tablas basándose en una columna
-- relacionada entre ellas. Es la forma principal de consultar datos
-- distribuidos en múltiples tablas en una base de datos normalizada.
--
-- En backend los JOINs son esenciales — los datos rara vez están
-- en una sola tabla. Un endpoint de "detalle de pedido" puede
-- necesitar datos de: pedidos, clientes, productos, categorías.
-- =============================================================


-- =============================================================
-- 1. CONCEPTOS CLAVE ANTES DE EMPEZAR
-- =============================================================

-- TABLA IZQUIERDA (LEFT) y TABLA DERECHA (RIGHT):
-- En un JOIN siempre hay dos tablas.
-- La tabla que va en el FROM es la IZQUIERDA.
-- La tabla que va después del JOIN es la DERECHA.
-- Esto importa especialmente en LEFT JOIN y RIGHT JOIN.

-- ON: define la condición de unión — qué columnas relacionan las tablas.
-- Siempre va después del JOIN.
-- Sintaxis: ON tabla_a.columna = tabla_b.columna

-- ALIAS DE TABLA: se usa para escribir menos y evitar ambigüedad.
-- Cuando dos tablas tienen columnas con el mismo nombre (ej: name),
-- debes especificar de qué tabla viene: tabla.columna o alias.columna.
-- Ejemplo: FROM empleados e → e es el alias de empleados

-- CUÁNDO USAR JOIN vs SUBQUERY:
-- JOIN      → cuando necesitas columnas de varias tablas en el resultado
-- SUBQUERY  → cuando solo necesitas un valor de otra tabla para filtrar


-- =============================================================
-- 2. INNER JOIN — Solo filas con coincidencia en ambas tablas
-- =============================================================
-- Para qué: obtener datos que existen en AMBAS tablas relacionadas.
-- Cuándo: cuando solo te interesan los registros completos —
--         pedidos con cliente, productos con categoría, empleados
--         con departamento. Excluye automáticamente los NULL.
-- Resultado: solo las filas donde ON encuentra coincidencia en las dos tablas.
-- Nota: JOIN sin especificar tipo es lo mismo que INNER JOIN.

-- Sintaxis:
-- SELECT tabla_a.col, tabla_b.col
-- FROM tabla_a
-- INNER JOIN tabla_b ON tabla_a.fk = tabla_b.pk;

-- Con alias (forma más común en la práctica):
-- SELECT a.col, b.col
-- FROM tabla_a a
-- INNER JOIN tabla_b b ON a.fk = b.pk;

-- Ejemplo — pedidos con su cliente (solo pedidos que tienen cliente):
SELECT p.pedido_id, p.fecha, c.nombre AS cliente
FROM pedidos p
INNER JOIN clientes c ON p.cliente_id = c.cliente_id;
-- Resultado: solo pedidos que tienen un cliente_id válido en clientes.
-- Los pedidos sin cliente_id o con cliente_id inexistente → no aparecen.

-- Ejemplo — productos con su categoría:
SELECT pr.nombre AS producto, pr.precio, cat.nombre AS categoria
FROM productos pr
INNER JOIN categorias cat ON pr.categoria_id = cat.categoria_id
ORDER BY cat.nombre;

-- JOIN encadenado — múltiples tablas:
-- Se puede encadenar varios JOIN para unir más de dos tablas.
-- Cada JOIN agrega una tabla al resultado.
-- Sintaxis:
-- FROM tabla_a a
-- INNER JOIN tabla_b b ON a.fk = b.pk
-- INNER JOIN tabla_c c ON b.fk = c.pk;

-- Ejemplo — pedidos con cliente y con los productos del pedido:
SELECT p.pedido_id, c.nombre AS cliente, pr.nombre AS producto
FROM pedidos p
INNER JOIN clientes c ON p.cliente_id = c.cliente_id
INNER JOIN pedido_detalle pd ON p.pedido_id = pd.pedido_id
INNER JOIN productos pr ON pd.producto_id = pr.producto_id;

-- JOIN con WHERE — filtrar después de unir:
-- Ejemplo — pedidos de un cliente específico:
SELECT p.pedido_id, p.fecha, c.nombre
FROM pedidos p
INNER JOIN clientes c ON p.cliente_id = c.cliente_id
WHERE c.nombre = 'María López'
ORDER BY p.fecha DESC;

-- JOIN con tabla intermedia N:M:
-- Para unir dos tablas con relación N:M necesitas pasar por la intermedia.
-- Ejemplo — estudiantes y sus materias (a través de inscripciones):
SELECT e.nombre AS estudiante, m.nombre AS materia
FROM estudiantes e
INNER JOIN inscripciones i ON e.estudiante_id = i.estudiante_id
INNER JOIN materias m ON i.materia_id = m.materia_id
ORDER BY e.nombre, m.nombre;

-- ERROR común — INNER JOIN sin ON:
-- SELECT * FROM pedidos INNER JOIN clientes;
-- Resultado: producto cartesiano — cada pedido con cada cliente (incorrecto)
-- Siempre especifica el ON.


-- =============================================================
-- 3. LEFT JOIN — Todas las filas de la izquierda
-- =============================================================
-- Para qué: obtener TODOS los registros de la tabla izquierda,
--           con los datos de la derecha si existen, NULL si no.
-- Cuándo: cuando el registro de la izquierda es importante aunque
--         no tenga relación — clientes sin pedidos, productos sin
--         categoría, empleados sin asignación.
-- Resultado: todas las filas de la tabla izquierda (FROM).
--            Si no hay coincidencia en la derecha → NULL en esas columnas.

-- Sintaxis:
-- SELECT a.col, b.col
-- FROM tabla_izquierda a
-- LEFT JOIN tabla_derecha b ON a.fk = b.pk;

-- Ejemplo — todos los clientes, tengan o no pedidos:
SELECT c.nombre AS cliente, p.pedido_id, p.fecha
FROM clientes c
LEFT JOIN pedidos p ON c.cliente_id = p.cliente_id;
-- Clientes con pedidos → aparecen con sus datos de pedido
-- Clientes sin pedidos → aparecen con NULL en pedido_id y fecha

-- Ejemplo — encontrar registros SIN relación (patrón muy común en backend):
-- Filtrar los NULL del LEFT JOIN para obtener solo los que no tienen relación.
SELECT c.nombre AS cliente_sin_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.cliente_id = p.cliente_id
WHERE p.pedido_id IS NULL;
-- Este patrón (LEFT JOIN + WHERE IS NULL) es equivalente a NOT IN con subquery
-- pero más eficiente en tablas grandes.

-- Ejemplo — todos los productos con su categoría (tengan o no categoría):
SELECT pr.nombre AS producto, cat.nombre AS categoria
FROM productos pr
LEFT JOIN categorias cat ON pr.categoria_id = cat.categoria_id
ORDER BY pr.nombre;

-- LEFT JOIN encadenado con tabla intermedia N:M:
-- Ejemplo — todos los estudiantes con sus materias (tengan o no):
SELECT e.nombre AS estudiante, m.nombre AS materia
FROM estudiantes e
LEFT JOIN inscripciones i ON e.estudiante_id = i.estudiante_id
LEFT JOIN materias m ON i.materia_id = m.materia_id;
-- Estudiante sin materias → aparece con NULL en materia

-- Diferencia clave con INNER JOIN:
-- INNER JOIN → solo estudiantes CON materias
-- LEFT JOIN  → todos los estudiantes, con o sin materias


-- =============================================================
-- 4. RIGHT JOIN — Todas las filas de la derecha
-- =============================================================
-- Para qué: obtener TODOS los registros de la tabla derecha,
--           con los datos de la izquierda si existen, NULL si no.
-- Cuándo: cuando el registro de la derecha es el importante —
--         todos los departamentos aunque no tengan empleados,
--         todos los géneros aunque no tengan productos.
-- Resultado: todas las filas de la tabla derecha (la del JOIN).
--            Si no hay coincidencia en la izquierda → NULL en esas columnas.
-- NOTA PRÁCTICA: en la mayoría de casos puedes evitar RIGHT JOIN
--                invirtiendo el orden de las tablas y usando LEFT JOIN.
--                Es más común ver LEFT JOIN en código real.

-- Sintaxis:
-- SELECT a.col, b.col
-- FROM tabla_izquierda a
-- RIGHT JOIN tabla_derecha b ON a.fk = b.pk;

-- Ejemplo — todos los departamentos, tengan o no empleados:
SELECT d.nombre AS departamento, e.nombre AS empleado
FROM empleados e
RIGHT JOIN departamentos d ON e.departamento_id = d.departamento_id;
-- Departamentos con empleados → aparecen con nombre del empleado
-- Departamentos sin empleados → aparecen con NULL en nombre del empleado

-- El mismo resultado con LEFT JOIN invirtiendo el orden:
SELECT d.nombre AS departamento, e.nombre AS empleado
FROM departamentos d
LEFT JOIN empleados e ON e.departamento_id = d.departamento_id;
-- Ambas queries producen el mismo resultado — LEFT JOIN es más legible.

-- Ejemplo — todos los géneros aunque no tengan productos:
SELECT g.nombre AS genero, COUNT(p.producto_id) AS total_productos
FROM productos p
RIGHT JOIN generos g ON p.genero_id = g.genero_id
GROUP BY g.nombre;

-- Diferencia LEFT vs RIGHT:
-- LEFT JOIN  → prioriza la tabla del FROM (izquierda)
-- RIGHT JOIN → prioriza la tabla del JOIN (derecha)
-- En la práctica: usa LEFT JOIN y organiza tus tablas en consecuencia.


-- =============================================================
-- 5. UNION y UNION ALL — Combinar resultados de dos queries
-- =============================================================
-- Para qué: combinar los resultados de dos SELECT en un solo resultado.
-- Cuándo: consultar datos de dos tablas que no están relacionadas,
--         simular FULL OUTER JOIN (que MySQL no soporta nativamente),
--         combinar resultados de dos condiciones distintas.
-- Requisito: ambos SELECT deben tener el mismo número de columnas
--            y tipos de dato compatibles en el mismo orden.

-- Sintaxis:
-- SELECT col1, col2 FROM tabla_a WHERE condición
-- UNION
-- SELECT col1, col2 FROM tabla_b WHERE condición;

-- UNION     → elimina filas duplicadas del resultado combinado
-- UNION ALL → mantiene todas las filas incluyendo duplicados (más rápido)

-- Ejemplo — combinar emails de clientes y proveedores en una lista:
SELECT nombre, email, 'Cliente' AS tipo
FROM clientes
UNION
SELECT nombre, email, 'Proveedor' AS tipo
FROM proveedores
ORDER BY nombre;

-- Ejemplo — FULL OUTER JOIN simulado con UNION:
-- MySQL no tiene FULL OUTER JOIN — se simula con LEFT JOIN + RIGHT JOIN + UNION
SELECT c.nombre AS cliente, p.pedido_id
FROM clientes c
LEFT JOIN pedidos p ON c.cliente_id = p.cliente_id
UNION
SELECT c.nombre AS cliente, p.pedido_id
FROM clientes c
RIGHT JOIN pedidos p ON c.cliente_id = p.cliente_id;
-- Resultado: todos los clientes + todos los pedidos, con NULL donde no hay relación.

-- Ejemplo — UNION ALL (mantiene duplicados):
SELECT categoria_id FROM productos WHERE precio > 100
UNION ALL
SELECT categoria_id FROM productos WHERE stock < 10;
-- Si un categoria_id cumple ambas condiciones → aparece dos veces

-- Cuándo usar UNION ALL en vez de UNION:
-- Cuando sabes que no habrá duplicados → UNION ALL es más rápido
-- Cuando necesitas contar ocurrencias → UNION ALL (los duplicados importan)
-- Cuando quieres resultado limpio sin duplicados → UNION


-- =============================================================
-- 6. ALIAS EN JOIN — Buenas prácticas
-- =============================================================
-- Los alias son casi obligatorios en queries con JOIN para:
-- → Escribir menos código
-- → Evitar ambigüedad cuando dos tablas tienen columnas con el mismo nombre
-- → Hacer el código más legible

-- Sin alias — verboso y difícil de leer:
SELECT pedidos.pedido_id, clientes.nombre, productos.nombre
FROM pedidos
INNER JOIN clientes ON pedidos.cliente_id = clientes.cliente_id
INNER JOIN pedido_detalle ON pedidos.pedido_id = pedido_detalle.pedido_id
INNER JOIN productos ON pedido_detalle.producto_id = productos.producto_id;

-- Con alias — limpio y legible:
SELECT p.pedido_id, c.nombre AS cliente, pr.nombre AS producto
FROM pedidos p
INNER JOIN clientes c ON p.cliente_id = c.cliente_id
INNER JOIN pedido_detalle pd ON p.pedido_id = pd.pedido_id
INNER JOIN productos pr ON pd.producto_id = pr.producto_id;

-- Convención de alias comunes en backend:
-- u  → users / usuarios
-- c  → clientes / customers
-- p  → pedidos / products (depende del contexto)
-- pr → productos (cuando p ya está usado)
-- e  → empleados
-- d  → departamentos
-- m  → movies / materias (depende del contexto)
-- mg → movie_genre (tablas intermedias)
-- ma → movie_actor


-- =============================================================
-- 7. RESUMEN — CUÁNDO USAR CADA JOIN
-- =============================================================
--
-- INNER JOIN → solo registros con relación en AMBAS tablas
--   Cuándo: datos completos — pedido con cliente, producto con categoría
--   Excluye: registros sin relación (NULL)
--
-- LEFT JOIN  → TODOS los de la izquierda + coincidencias de la derecha
--   Cuándo: la tabla izquierda es la principal — todos los clientes
--           aunque no tengan pedidos
--   Patrón + WHERE IS NULL → encontrar registros SIN relación
--
-- RIGHT JOIN → TODOS los de la derecha + coincidencias de la izquierda
--   Cuándo: la tabla derecha es la principal — todos los departamentos
--           aunque no tengan empleados
--   En práctica: se puede reemplazar con LEFT JOIN invirtiendo tablas
--
-- UNION      → combinar resultados de dos SELECT sin duplicados
--   Cuándo: datos de tablas no relacionadas, simular FULL OUTER JOIN
--
-- UNION ALL  → combinar resultados de dos SELECT manteniendo duplicados
--   Cuándo: cuando los duplicados importan o cuando sabes que no hay
--           duplicados y quieres mejor rendimiento
--
-- REGLA PRÁCTICA PARA ELEGIR:
-- ¿Necesito solo registros con relación completa?   → INNER JOIN
-- ¿Necesito todos los de una tabla + los que tenga? → LEFT JOIN
-- ¿Necesito combinar dos consultas independientes?  → UNION
--
-- MySQL NO soporta FULL OUTER JOIN nativamente.
-- Se simula con: LEFT JOIN UNION RIGHT JOIN
EOF