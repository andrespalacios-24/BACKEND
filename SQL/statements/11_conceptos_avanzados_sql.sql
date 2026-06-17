-- =============================================================
-- MYSQL - CONCEPTOS AVANZADOS
-- VIEW, INDEX, STORED PROCEDURE, TRIGGER, TRANSACCIONES
-- Fuentes: MySQL 8.0 Docs + W3Schools
-- =============================================================
-- Estos conceptos son fundamentales en el desarrollo backend
-- profesional. Permiten encapsular lógica en la base de datos,
-- mejorar el rendimiento, automatizar acciones y garantizar
-- la integridad de los datos.
-- =============================================================


-- =============================================================
-- 1. VIEW (Vista)
-- =============================================================
-- Para qué: una vista es una consulta guardada con nombre que
--           se comporta como una tabla virtual. No guarda datos
--           — ejecuta el SELECT cada vez que se consulta.
--
-- Cuándo usarla:
-- → Simplificar queries complejas con JOIN que se repiten mucho
-- → Restringir acceso a columnas sensibles (ej: ocultar contraseñas)
-- → Estandarizar la forma en que se consultan los datos
-- → Crear capas de abstracción entre la app y la base de datos
--
-- En backend: un endpoint de "resumen de pedido" puede usar una
-- vista en lugar de repetir el mismo JOIN de 5 tablas en cada query.
--
-- IMPORTANTE:
-- → No almacena datos — solo la definición del SELECT
-- → Si las tablas base cambian, la vista refleja los cambios
-- → Se puede consultar con SELECT igual que una tabla
-- → Se puede usar en WHERE, JOIN y otras queries
-- → No se puede hacer INSERT/UPDATE/DELETE en vistas complejas

-- Sintaxis:
-- CREATE VIEW nombre_vista AS
-- SELECT ...;

-- Consultar una vista:
-- SELECT * FROM nombre_vista;
-- SELECT * FROM nombre_vista WHERE condición;

-- Eliminar una vista:
-- DROP VIEW nombre_vista;
-- DROP VIEW IF EXISTS nombre_vista;

-- Ejemplo 1 — vista de empleados activos con su departamento:
CREATE VIEW vw_empleados_activos AS
SELECT e.empleado_id, e.nombre, e.email, d.nombre AS departamento
FROM empleados e
INNER JOIN departamentos d ON e.departamento_id = d.departamento_id
WHERE e.activo = TRUE;

-- Consultar la vista:
SELECT * FROM vw_empleados_activos;
SELECT * FROM vw_empleados_activos WHERE departamento = 'Tecnología';

-- Ejemplo 2 — vista de productos con stock bajo:
CREATE VIEW vw_stock_bajo AS
SELECT p.producto_id, p.nombre, p.precio, p.stock, c.nombre AS categoria
FROM productos p
INNER JOIN categorias c ON p.categoria_id = c.categoria_id
WHERE p.stock < 10;

-- Ejemplo 3 — vista de pedidos del último mes:
CREATE VIEW vw_pedidos_recientes AS
SELECT p.pedido_id, c.nombre AS cliente, p.total, p.fecha
FROM pedidos p
INNER JOIN clientes c ON p.cliente_id = c.cliente_id
WHERE p.fecha >= DATE_SUB(NOW(), INTERVAL 1 MONTH);

-- Eliminar vista:
DROP VIEW IF EXISTS vw_stock_bajo;

-- Ver todas las vistas de la base de datos:
SHOW FULL TABLES WHERE Table_type = 'VIEW';


-- =============================================================
-- 2. INDEX (Índice)
-- =============================================================
-- Para qué: estructura de datos que MySQL usa internamente para
--           encontrar filas más rápido sin recorrer toda la tabla.
--           Como el índice de un libro — va directo a la página.
--
-- Cuándo usarlo:
-- → Columnas que usas frecuentemente en WHERE, ORDER BY, JOIN
-- → Columnas con muchos valores distintos (alta cardinalidad)
-- → Tablas grandes donde las queries son lentas
--
-- Cuándo NO usarlo:
-- → Tablas pequeñas — el índice no aporta mejora notable
-- → Columnas que se actualizan muy frecuentemente — cada INSERT/UPDATE
--   reconstruye el índice, lo que tiene un costo
-- → Columnas con pocos valores distintos (ej: activo TRUE/FALSE)
--
-- En backend: los índices son críticos para el rendimiento. Una
-- query sin índice en una tabla de 10 millones de filas puede
-- tardar segundos. Con índice, milisegundos.
--
-- NOTA: PRIMARY KEY y UNIQUE crean índices automáticamente.
--       No necesitas crear índice manual en esas columnas.

-- Sintaxis:
-- CREATE INDEX nombre ON tabla (columna);
-- CREATE INDEX nombre ON tabla (col1, col2);  ← índice compuesto
-- CREATE UNIQUE INDEX nombre ON tabla (columna);
-- DROP INDEX nombre ON tabla;

-- Ejemplo — índice en columna de búsqueda frecuente:
CREATE INDEX idx_email ON clientes (email);

-- Índice en columna de ordenamiento frecuente:
CREATE INDEX idx_fecha ON pedidos (fecha);

-- Índice compuesto — para queries que filtran por dos columnas:
CREATE INDEX idx_cliente_fecha ON pedidos (cliente_id, fecha);

-- Índice único — garantiza unicidad además de mejorar búsqueda:
CREATE UNIQUE INDEX idx_unique_email ON usuarios (email);

-- Índice compuesto en tabla intermedia N:M:
CREATE INDEX idx_movie_actor ON movie_actor (movie_id, actor_id);

-- Eliminar índice:
DROP INDEX idx_email ON clientes;

-- Ver índices de una tabla:
SHOW INDEX FROM clientes;

-- REGLA PRÁCTICA para nombrar índices:
-- idx_  → índice normal        (ej: idx_fecha, idx_email)
-- uidx_ → índice único         (ej: uidx_email)
-- o simplemente idx_tabla_columna para mayor claridad


-- =============================================================
-- 3. STORED PROCEDURE (Procedimiento Almacenado)
-- =============================================================
-- Para qué: bloque de código SQL guardado en la base de datos
--           con un nombre, que se puede ejecutar con CALL.
--           Puede recibir parámetros y contener lógica compleja.
--
-- Cuándo usarlo:
-- → Operaciones repetitivas que siempre se hacen igual
-- → Lógica de negocio que debe estar centralizada en la BD
-- → Operaciones que necesitan múltiples queries en secuencia
-- → Cuando quieres limitar qué queries puede ejecutar la app
--
-- En backend: menos común en arquitecturas modernas (la lógica
-- suele estar en el código de la app con un ORM), pero sigue
-- siendo muy usado en sistemas legacy, reportes, y empresas que
-- prefieren centralizar la lógica en la BD.
--
-- DELIMITER: cambia el delimitador de instrucciones temporalmente.
-- Por defecto MySQL usa ; para terminar instrucciones.
-- Dentro de un procedimiento necesitas ; para separar las queries
-- internas, pero no quieres que MySQL interprete eso como el fin
-- del procedimiento. DELIMITER // cambia el delimitador a //
-- para que MySQL sepa que el procedimiento termina con END //.
-- Al final siempre vuelves a ; con DELIMITER ;

-- Sintaxis:
-- DELIMITER //
-- CREATE PROCEDURE nombre_procedimiento(
--     IN param1 TIPO,
--     IN param2 TIPO
-- )
-- BEGIN
--     -- instrucciones SQL;
-- END //
-- DELIMITER ;

-- Llamar un procedimiento:
-- CALL nombre_procedimiento(valor1, valor2);

-- Eliminar un procedimiento:
-- DROP PROCEDURE nombre_procedimiento;
-- DROP PROCEDURE IF EXISTS nombre_procedimiento;

-- Tipos de parámetros:
-- IN  → valor de entrada (el más común)
-- OUT → valor de salida — el procedimiento lo modifica
-- INOUT → entrada y salida a la vez

-- Ejemplo 1 — procedimiento para insertar un cliente:
DELIMITER //
CREATE PROCEDURE sp_insertar_cliente(
    IN p_nombre    VARCHAR(100),
    IN p_email     VARCHAR(150),
    IN p_telefono  VARCHAR(20)
)
BEGIN
    INSERT INTO clientes (nombre, email, telefono)
    VALUES (p_nombre, p_email, p_telefono);
END //
DELIMITER ;

-- Llamar el procedimiento:
CALL sp_insertar_cliente('María López', 'maria@email.com', '3001234567');

-- Ejemplo 2 — procedimiento para actualizar stock:
DELIMITER //
CREATE PROCEDURE sp_actualizar_stock(
    IN p_producto_id INT,
    IN p_nuevo_stock INT
)
BEGIN
    UPDATE productos
    SET stock = p_nuevo_stock
    WHERE producto_id = p_producto_id;
END //
DELIMITER ;

CALL sp_actualizar_stock(5, 100);

-- Ejemplo 3 — procedimiento para eliminar un pedido:
DELIMITER //
CREATE PROCEDURE sp_eliminar_pedido(
    IN p_pedido_id INT
)
BEGIN
    DELETE FROM pedido_detalle WHERE pedido_id = p_pedido_id;
    DELETE FROM pedidos WHERE pedido_id = p_pedido_id;
END //
DELIMITER ;

CALL sp_eliminar_pedido(12);

-- Ver procedimientos de la base de datos:
SHOW PROCEDURE STATUS WHERE Db = 'nombre_base_datos';

-- CONVENCIÓN de nombres:
-- sp_ → stored procedure (ej: sp_insertar_cliente, sp_eliminar_pedido)


-- =============================================================
-- 4. TRIGGER (Disparador)
-- =============================================================
-- Para qué: bloque de código SQL que se ejecuta AUTOMÁTICAMENTE
--           cuando ocurre un INSERT, UPDATE o DELETE en una tabla.
--           No se llama manualmente — se dispara solo.
--
-- Cuándo usarlo:
-- → Auditoría — registrar quién cambió qué y cuándo
-- → Mantener datos sincronizados entre tablas
-- → Validaciones complejas antes de insertar/actualizar
-- → Historial de cambios automático
--
-- En backend: muy usado para auditoría de datos (quién modificó
-- un registro y cuándo), logs de cambios, y sincronización
-- automática de datos sin depender del código de la app.
--
-- Momentos de ejecución:
-- BEFORE → se ejecuta ANTES de la operación — puede modificar los datos
-- AFTER  → se ejecuta DESPUÉS de la operación — para registrar/sincronizar
--
-- Palabras clave dentro del trigger:
-- NEW → los valores nuevos (disponible en INSERT y UPDATE)
-- OLD → los valores anteriores (disponible en UPDATE y DELETE)
--
-- LIMITACIONES IMPORTANTES:
-- → No puede usar START TRANSACTION, COMMIT o ROLLBACK internamente
-- → No puede llamar procedimientos que retornen datos al cliente

-- Sintaxis:
-- DELIMITER //
-- CREATE TRIGGER nombre_trigger
-- BEFORE|AFTER INSERT|UPDATE|DELETE ON tabla
-- FOR EACH ROW
-- BEGIN
--     -- instrucciones SQL usando NEW y/o OLD;
-- END //
-- DELIMITER ;

-- Eliminar trigger:
-- DROP TRIGGER nombre_trigger;
-- DROP TRIGGER IF EXISTS nombre_trigger;

-- Ver triggers de la base de datos:
-- SHOW TRIGGERS;

-- Ejemplo 1 — AFTER INSERT: registrar cuando se crea un pedido:
DELIMITER //
CREATE TRIGGER tg_after_insert_pedido
AFTER INSERT ON pedidos
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (tabla, operacion, registro_id, usuario, fecha)
    VALUES ('pedidos', 'INSERT', NEW.pedido_id, USER(), NOW());
END //
DELIMITER ;

-- Ejemplo 2 — BEFORE UPDATE: guardar email anterior antes de cambiarlo:
DELIMITER //
CREATE TRIGGER tg_before_update_email
BEFORE UPDATE ON clientes
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        INSERT INTO historial_emails (cliente_id, email_anterior, fecha_cambio)
        VALUES (OLD.cliente_id, OLD.email, NOW());
    END IF;
END //
DELIMITER ;

-- Ejemplo 3 — AFTER UPDATE con JSON_OBJECT — guardar valores anteriores y nuevos:
-- JSON_OBJECT() convierte pares clave-valor en formato JSON
-- Muy útil para guardar múltiples campos en una sola columna TEXT
DELIMITER //
CREATE TRIGGER tg_after_update_producto
AFTER UPDATE ON productos
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (tabla, operacion, registro_id, usuario, fecha, valores_anteriores, valores_nuevos)
    VALUES (
        'productos', 'UPDATE', OLD.producto_id, USER(), NOW(),
        JSON_OBJECT('nombre', OLD.nombre, 'precio', OLD.precio, 'stock', OLD.stock),
        JSON_OBJECT('nombre', NEW.nombre, 'precio', NEW.precio, 'stock', NEW.stock)
    );
END //
DELIMITER ;

-- Ejemplo 4 — AFTER DELETE: registrar eliminación:
DELIMITER //
CREATE TRIGGER tg_after_delete_cliente
AFTER DELETE ON clientes
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (tabla, operacion, registro_id, usuario, fecha, valores_anteriores)
    VALUES (
        'clientes', 'DELETE', OLD.cliente_id, USER(), NOW(),
        JSON_OBJECT('nombre', OLD.nombre, 'email', OLD.email)
    );
END //
DELIMITER ;

-- BEFORE vs AFTER — cuándo usar cada uno:
-- BEFORE INSERT/UPDATE → validar o modificar datos antes de guardarlos
-- AFTER INSERT         → registrar en log, actualizar contadores
-- AFTER UPDATE         → guardar historial de cambios
-- AFTER DELETE         → registrar eliminación en auditoría

-- CONVENCIÓN de nombres:
-- tg_after_insert_tabla
-- tg_before_update_tabla
-- tg_after_delete_tabla


-- =============================================================
-- 5. TRANSACCIONES
-- =============================================================
-- Para qué: agrupar múltiples operaciones SQL en una unidad
--           atómica — o todas tienen éxito, o ninguna se aplica.
--           Si algo falla en el medio, se revierte todo.
--
-- Cuándo usarlas:
-- → Transferencias bancarias (débito + crédito deben ser atómicos)
-- → Crear un pedido (insertar pedido + reducir stock + registrar pago)
-- → Cualquier operación que involucra múltiples tablas y debe ser
--   consistente — si una falla, las demás no deben aplicarse
--
-- En backend: las transacciones son críticas en sistemas financieros,
-- e-commerce, reservas. Un ORM como SQLAlchemy las maneja
-- automáticamente, pero entender cómo funcionan es esencial.
--
-- PROPIEDADES ACID:
-- A (Atomicidad)   → todo o nada — no hay operaciones parciales
-- C (Consistencia) → la BD pasa de un estado válido a otro válido
-- I (Aislamiento)  → transacciones concurrentes no se interfieren
-- D (Durabilidad)  → una vez confirmada, el cambio es permanente
--
-- NOTA: MySQL tiene Auto-Commit activado por defecto — cada
-- instrucción se confirma automáticamente. START TRANSACTION
-- desactiva el auto-commit para ese bloque.
-- En Workbench: Query → Auto-Commit Transactions para controlar esto.

-- Sintaxis:
-- START TRANSACTION;
-- -- operaciones SQL;
-- COMMIT;    ← confirmar todos los cambios
-- -- o
-- ROLLBACK;  ← revertir todos los cambios

-- Ejemplo 1 — transferencia bancaria (operación atómica):
START TRANSACTION;

UPDATE cuentas SET saldo = saldo - 500000 WHERE cuenta_id = 1;  -- débito
UPDATE cuentas SET saldo = saldo + 500000 WHERE cuenta_id = 2;  -- crédito

-- Si ambas se ejecutaron bien → confirmar:
COMMIT;
-- Si algo falló → revertir:
-- ROLLBACK;

-- Ejemplo 2 — crear pedido con múltiples operaciones:
START TRANSACTION;

INSERT INTO pedidos (cliente_id, total, fecha)
VALUES (5, 150000, NOW());

INSERT INTO pedido_detalle (pedido_id, producto_id, cantidad, precio)
VALUES (LAST_INSERT_ID(), 3, 2, 75000);

UPDATE productos SET stock = stock - 2 WHERE producto_id = 3;

COMMIT;

-- Ejemplo 3 — insertar y verificar antes de confirmar:
START TRANSACTION;

INSERT INTO clientes (nombre, email)
VALUES ('Carlos Ruiz', 'carlos@email.com');

-- Verificar que se insertó correctamente:
SELECT * FROM clientes WHERE email = 'carlos@email.com';

-- Si todo está bien:
COMMIT;
-- Si algo está mal:
-- ROLLBACK;

-- Ejemplo 4 — ROLLBACK para deshacer:
START TRANSACTION;

DELETE FROM pedidos WHERE cliente_id = 10;

-- Me arrepentí — revertir:
ROLLBACK;
-- Los pedidos del cliente 10 siguen existiendo

-- SAVEPOINT — punto de guardado dentro de una transacción:
-- Permite hacer ROLLBACK parcial sin revertir todo
START TRANSACTION;

INSERT INTO clientes (nombre, email) VALUES ('Ana', 'ana@email.com');
SAVEPOINT sp1;

INSERT INTO clientes (nombre, email) VALUES ('Luis', 'luis@email.com');
SAVEPOINT sp2;

-- Revertir solo hasta sp1 (deshace la inserción de Luis, no de Ana):
ROLLBACK TO SAVEPOINT sp1;

COMMIT;  -- confirma solo la inserción de Ana


-- =============================================================
-- 6. CONCURRENCIA
-- =============================================================
-- Para qué: controlar qué pasa cuando múltiples usuarios o
--           procesos acceden y modifican los mismos datos al mismo
--           tiempo.
--
-- Cuándo importa:
-- → Sistemas con muchos usuarios simultáneos
-- → Operaciones de escritura frecuentes en las mismas tablas
-- → Sistemas financieros donde la precisión es crítica
--
-- En backend: un ORM moderno maneja gran parte de esto, pero
-- entender los conceptos te ayuda a diseñar mejor los sistemas.
--
-- PROBLEMAS COMUNES DE CONCURRENCIA:
-- Dirty Read    → leer datos no confirmados de otra transacción
-- Lost Update   → dos transacciones actualizan el mismo registro
--                 y una sobreescribe a la otra
-- Phantom Read  → una query devuelve filas diferentes si se
--                 ejecuta dos veces dentro de la misma transacción

-- NIVELES DE AISLAMIENTO en MySQL (de menor a mayor protección):
-- READ UNCOMMITTED → puede leer datos sin confirmar (Dirty Read)
-- READ COMMITTED   → solo lee datos confirmados
-- REPEATABLE READ  → garantiza que la misma query devuelve lo mismo
--                    (nivel por defecto en MySQL)
-- SERIALIZABLE     → máxima protección, mínimo rendimiento

-- Ver el nivel de aislamiento actual:
SELECT @@transaction_isolation;

-- Cambiar el nivel de aislamiento:
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- LOCK (bloqueo) — prevenir que otros modifiquen un registro:
-- SELECT ... FOR UPDATE bloquea las filas seleccionadas
-- hasta que se haga COMMIT o ROLLBACK

START TRANSACTION;
SELECT * FROM productos WHERE producto_id = 5 FOR UPDATE;
-- Nadie más puede modificar ese producto hasta que se libere el lock
UPDATE productos SET stock = stock - 1 WHERE producto_id = 5;
COMMIT;


-- =============================================================
-- 7. RESUMEN — CUÁNDO USAR CADA CONCEPTO
-- =============================================================
--
-- VIEW
--   → Simplificar queries complejas repetitivas
--   → Ocultar columnas sensibles a ciertos usuarios
--   → Capa de abstracción entre app y BD
--   → No almacena datos — solo la query
--
-- INDEX
--   → Acelerar búsquedas en columnas de WHERE, JOIN, ORDER BY
--   → Tablas grandes con queries lentas
--   → No usar en columnas que cambian constantemente
--   → PRIMARY KEY y UNIQUE ya crean índices automáticamente
--
-- STORED PROCEDURE
--   → Lógica repetitiva centralizada en la BD
--   → Operaciones de múltiples queries en secuencia
--   → Se llama con CALL — no se ejecuta solo
--   → DELIMITER // necesario para definirlo
--
-- TRIGGER
--   → Auditoría automática de cambios
--   → Historial de modificaciones
--   → Se ejecuta solo al INSERT/UPDATE/DELETE
--   → BEFORE para validar/modificar, AFTER para registrar
--   → Usa NEW (valores nuevos) y OLD (valores anteriores)
--
-- TRANSACCIONES
--   → Operaciones atómicas — todo o nada
--   → START TRANSACTION → operaciones → COMMIT o ROLLBACK
--   → Críticas en operaciones financieras y de múltiples tablas
--   → SAVEPOINT para puntos de reversión parcial
--
-- CONCURRENCIA
--   → Control de acceso simultáneo a los mismos datos
--   → SELECT ... FOR UPDATE para bloquear filas
--   → Niveles de aislamiento según necesidad de precisión
EOF