-- =============================================================
-- MYSQL - ESCRITURA DE DATOS RELACIONADOS
-- INSERT, UPDATE, DELETE en tablas con relaciones 1:1, 1:N, N:M
-- Fuentes: MySQL 8.0 Docs + W3Schools
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
--             → intentaste insertar/actualizar un hijo con padre inexistente
-- ERROR 1451: Cannot delete or update a parent row: foreign key constraint fails
--             → intentaste eliminar un padre que todavía tiene hijos
-- ERROR 1093: You can't specify target table for update in FROM clause
--             → subquery que consulta la misma tabla del DELETE/UPDATE


-- =============================================================
-- 2. RELACIÓN 1:1 — Un registro de A con exactamente uno de B
-- =============================================================
-- La FK está en la tabla secundaria CON UNIQUE.
-- Tablas de ejemplo:
--   clientes  (cliente_id PK, nombre, email)
--   pasaportes (pasaporte_id PK, numero, cliente_id FK UNIQUE → clientes)


-- -------------------------------------------------------------
-- 2.1 INSERT en 1:1
-- -------------------------------------------------------------
-- Para qué: agregar el registro secundario vinculado al principal.
-- Cuándo: al crear datos que dependen de otro registro —
--         pasaporte de cliente, perfil de usuario, contrato de empleado.
-- Cómo: primero insertar el padre, luego el hijo con la FK del padre.

-- Sintaxis:
-- INSERT INTO tabla_padre (columnas) VALUES (valores);
-- INSERT INTO tabla_secundaria (columnas, fk_columna)
-- VALUES (valores, id_del_padre);
-- o con subquery:
-- INSERT INTO tabla_secundaria (columnas, fk_columna)
-- VALUES (valores, (SELECT pk FROM tabla_padre WHERE condición));

-- Ejemplo:
INSERT INTO clientes (nombre, email)
VALUES ('María López', 'maria@email.com');

INSERT INTO pasaportes (numero, cliente_id)
VALUES ('AB123456',
    (SELECT cliente_id FROM clientes WHERE email = 'maria@email.com')
);

-- ERROR — insertar dos pasaportes para el mismo cliente:
-- INSERT INTO pasaportes (numero, cliente_id) VALUES ('ZZ999', 1);
-- Error: Duplicate entry '1' for key 'cliente_id' (viola el UNIQUE)

-- ERROR — insertar con cliente inexistente:
-- INSERT INTO pasaportes (numero, cliente_id) VALUES ('AB123', 999);
-- Error: Cannot add or update a child row: foreign key constraint fails


-- -------------------------------------------------------------
-- 2.2 UPDATE en 1:1
-- -------------------------------------------------------------
-- Para qué: modificar el dato del registro secundario.
-- Cuándo: renovación de pasaporte, actualización de contrato.
-- Cómo: UPDATE en la tabla secundaria filtrando por la FK del padre.

-- Sintaxis:
-- UPDATE tabla_secundaria
-- SET columna = nuevo_valor
-- WHERE fk_columna = (SELECT pk FROM tabla_padre WHERE condición);

UPDATE pasaportes
SET numero = 'CD789012'
WHERE cliente_id = (SELECT cliente_id FROM clientes WHERE email = 'maria@email.com');


-- -------------------------------------------------------------
-- 2.3 DELETE en 1:1
-- -------------------------------------------------------------
-- Para qué: eliminar el registro y su dependiente.
-- Cuándo: dar de baja un cliente y todos sus datos asociados.
-- Cómo: primero eliminar el hijo, luego el padre.

-- Sintaxis:
-- DELETE FROM tabla_secundaria
-- WHERE fk_columna = (SELECT pk FROM tabla_padre WHERE condición);
-- DELETE FROM tabla_padre WHERE condición;

DELETE FROM pasaportes
WHERE cliente_id = (SELECT cliente_id FROM clientes WHERE email = 'maria@email.com');

DELETE FROM clientes WHERE email = 'maria@email.com';

-- ERROR — intentar eliminar el padre sin eliminar el hijo primero:
-- DELETE FROM clientes WHERE email = 'maria@email.com';
-- Error: Cannot delete or update a parent row: foreign key constraint fails


-- =============================================================
-- 3. RELACIÓN 1:N — Un padre con muchos hijos
-- =============================================================
-- La FK está en la tabla hijo SIN UNIQUE.
-- ES LA RELACIÓN MÁS COMÚN en bases de datos relacionales.
-- Tablas de ejemplo:
--   categorias (categoria_id PK, nombre)
--   productos  (producto_id PK, nombre, precio, categoria_id FK → categorias)


-- -------------------------------------------------------------
-- 3.1 INSERT en 1:N
-- -------------------------------------------------------------
-- Para qué: agregar múltiples registros hijo a un mismo padre.
-- Cuándo: agregar productos a una categoría, pedidos a un cliente,
--         empleados a una empresa, comentarios a un artículo.
-- Cómo: el padre ya existe, insertar los hijos con su FK.

-- Sintaxis:
-- INSERT INTO tabla_hijo (fk_columna, otras_columnas)
-- VALUES (id_padre, valores),
--        (id_padre, valores);
-- o con subquery:
-- INSERT INTO tabla_hijo (fk_columna, otras_columnas)
-- VALUES ((SELECT pk FROM tabla_padre WHERE condición), valores);

-- Con ID conocido — múltiples hijos en un INSERT:
INSERT INTO productos (nombre, precio, categoria_id)
VALUES ('Laptop Pro',    1500.00, 1),
       ('Mouse Inalámbrico', 25.00, 1),
       ('Teclado Mecánico',  80.00, 1);

-- Con subquery — sin conocer el ID:
INSERT INTO productos (nombre, precio, categoria_id)
VALUES ('Monitor 4K', 400.00,
    (SELECT categoria_id FROM categorias WHERE nombre = 'Tecnología')
);

-- Sin campo opcional — usa DEFAULT si tiene uno definido:
INSERT INTO productos (nombre, precio, categoria_id)
VALUES ('Auriculares', 60.00, 1);


-- -------------------------------------------------------------
-- 3.2 UPDATE en 1:N
-- -------------------------------------------------------------
-- Para qué: cambiar la FK de un hijo (reasignarlo a otro padre),
--           o actualizar datos de varios hijos a la vez.
-- Cuándo: mover productos a otra categoría, reasignar empleados,
--         cambiar el proveedor de varios artículos.
-- Cómo: UPDATE en la tabla hijo con WHERE que filtre correctamente.

-- Sintaxis:
-- UPDATE tabla_hijo
-- SET fk_columna = (SELECT pk FROM tabla_padre WHERE condición)
-- WHERE condición_del_hijo;

-- Mover un producto a otra categoría:
UPDATE productos
SET categoria_id = (SELECT categoria_id FROM categorias WHERE nombre = 'Accesorios')
WHERE nombre = 'Mouse Inalámbrico';

-- Mover todos los productos de una categoría a otra:
UPDATE productos
SET categoria_id = (SELECT categoria_id FROM categorias WHERE nombre = 'Electrónica')
WHERE categoria_id = (SELECT categoria_id FROM categorias WHERE nombre = 'Tecnología');


-- -------------------------------------------------------------
-- 3.3 DELETE en 1:N
-- -------------------------------------------------------------
-- Para qué: eliminar un padre y todos sus hijos.
-- Cuándo: eliminar una categoría y sus productos, dar de baja
--         un cliente y sus pedidos.
-- Cómo: primero eliminar todos los hijos, luego el padre.

-- Sintaxis:
-- DELETE FROM tabla_hijo
-- WHERE fk_columna = (SELECT pk FROM tabla_padre WHERE condición);
-- DELETE FROM tabla_padre WHERE condición;

-- Paso 1 — eliminar los hijos:
DELETE FROM productos
WHERE categoria_id = (SELECT categoria_id FROM categorias WHERE nombre = 'Tecnología');

-- Paso 2 — eliminar el padre:
DELETE FROM categorias WHERE nombre = 'Tecnología';

-- Eliminar hijos de varios padres con IN:
DELETE FROM productos
WHERE categoria_id IN (
    SELECT categoria_id FROM categorias WHERE nombre IN ('Tecnología', 'Accesorios')
);

-- ERROR — intentar eliminar el padre sin eliminar hijos primero:
-- DELETE FROM categorias WHERE nombre = 'Tecnología';
-- Error: Cannot delete or update a parent row: foreign key constraint fails


-- =============================================================
-- 4. RELACIÓN N:M — Muchos de A con muchos de B
-- =============================================================
-- Requiere tabla intermedia con FK a ambas tablas y PK compuesta.
-- Tablas de ejemplo:
--   estudiantes   (estudiante_id PK, nombre)
--   materias      (materia_id PK, nombre)
--   inscripciones (estudiante_id FK + materia_id FK → tabla intermedia)


-- -------------------------------------------------------------
-- 4.1 INSERT en N:M
-- -------------------------------------------------------------
-- Para qué: crear una relación entre dos registros existentes.
-- Cuándo: inscribir estudiantes en materias, asociar etiquetas
--         a artículos, agregar ingredientes a recetas.
-- Cómo: insertar en la tabla intermedia un par de IDs.
--       Ambos registros deben existir antes de insertar la relación.

-- Sintaxis con IDs conocidos:
-- INSERT INTO tabla_intermedia (fk_a, fk_b)
-- VALUES (id_a, id_b),
--        (id_a, id_b);

-- Sintaxis con subqueries — una relación:
-- INSERT INTO tabla_intermedia (fk_a, fk_b)
-- VALUES (
--     (SELECT pk FROM tabla_a WHERE condición),
--     (SELECT pk FROM tabla_b WHERE condición)
-- );

-- Sintaxis con subqueries — múltiples relaciones:
-- INSERT INTO tabla_intermedia (fk_a, fk_b)
-- VALUES
--     ((SELECT pk FROM tabla_a WHERE condición), (SELECT pk FROM tabla_b WHERE condición_1)),
--     ((SELECT pk FROM tabla_a WHERE condición), (SELECT pk FROM tabla_b WHERE condición_2));

-- Con IDs conocidos:
INSERT INTO inscripciones (estudiante_id, materia_id)
VALUES (1, 3),   -- Juan - Bases de Datos
       (1, 5),   -- Juan - Programación
       (2, 3);   -- Ana  - Bases de Datos

-- Con subqueries — una relación:
INSERT INTO inscripciones (estudiante_id, materia_id)
VALUES (
    (SELECT estudiante_id FROM estudiantes WHERE nombre = 'Juan'),
    (SELECT materia_id FROM materias WHERE nombre = 'Algoritmos')
);

-- Con subqueries — múltiples relaciones:
INSERT INTO inscripciones (estudiante_id, materia_id)
VALUES
    ((SELECT estudiante_id FROM estudiantes WHERE nombre = 'Ana'),
     (SELECT materia_id FROM materias WHERE nombre = 'Programación')),
    ((SELECT estudiante_id FROM estudiantes WHERE nombre = 'Ana'),
     (SELECT materia_id FROM materias WHERE nombre = 'Algoritmos'));

-- ERROR — el par ya existe (viola la PK compuesta):
-- INSERT INTO inscripciones (estudiante_id, materia_id) VALUES (1, 3);
-- Error: Duplicate entry '1-3' for key 'PRIMARY'

-- ERROR — alguno de los IDs no existe:
-- INSERT INTO inscripciones (estudiante_id, materia_id) VALUES (999, 3);
-- Error: Cannot add or update a child row: foreign key constraint fails


-- -------------------------------------------------------------
-- 4.2 UPDATE en N:M
-- -------------------------------------------------------------
-- Para qué: cambiar uno de los valores de la relación.
-- Cuándo: cambiar una materia por otra en la inscripción de un estudiante.
-- Cómo: UPDATE en la tabla intermedia filtrando por ambas FK.
-- NOTA: en N:M suele ser más limpio DELETE + INSERT porque la
--       PK compuesta incluye el valor que quieres cambiar.

-- Sintaxis:
-- UPDATE tabla_intermedia
-- SET fk_b = (SELECT pk FROM tabla_b WHERE condición_nueva)
-- WHERE fk_a = (SELECT pk FROM tabla_a WHERE condición)
--   AND fk_b = (SELECT pk FROM tabla_b WHERE condición_vieja);

-- Cambiar la materia "Algoritmos" por "Redes" en la inscripción de Juan:
UPDATE inscripciones
SET materia_id = (SELECT materia_id FROM materias WHERE nombre = 'Redes')
WHERE estudiante_id = (SELECT estudiante_id FROM estudiantes WHERE nombre = 'Juan')
  AND materia_id = (SELECT materia_id FROM materias WHERE nombre = 'Algoritmos');


-- -------------------------------------------------------------
-- 4.3 DELETE en N:M
-- -------------------------------------------------------------
-- Para qué: eliminar una o todas las relaciones de un registro.
-- Cuándo: desinscribir un estudiante de una materia, quitar
--         todas las etiquetas de un artículo antes de eliminarlo.
-- Cómo: DELETE en la tabla intermedia filtrando por las FK necesarias.

-- Sintaxis — eliminar UNA relación específica:
-- DELETE FROM tabla_intermedia
-- WHERE fk_a = (SELECT pk FROM tabla_a WHERE condición)
--   AND fk_b = (SELECT pk FROM tabla_b WHERE condición);

-- Sintaxis — eliminar TODAS las relaciones de un registro:
-- DELETE FROM tabla_intermedia
-- WHERE fk_a = (SELECT pk FROM tabla_a WHERE condición);

-- Sintaxis — eliminar relaciones de múltiples registros con IN:
-- DELETE FROM tabla_intermedia
-- WHERE fk_b IN (SELECT pk FROM tabla_b WHERE condición);

-- Eliminar una inscripción específica:
DELETE FROM inscripciones
WHERE estudiante_id = (SELECT estudiante_id FROM estudiantes WHERE nombre = 'Juan')
  AND materia_id    = (SELECT materia_id FROM materias WHERE nombre = 'Programación');

-- Eliminar todas las inscripciones de un estudiante:
DELETE FROM inscripciones
WHERE estudiante_id = (SELECT estudiante_id FROM estudiantes WHERE nombre = 'Ana');

-- Eliminar inscripciones de varias materias:
DELETE FROM inscripciones
WHERE materia_id IN (
    SELECT materia_id FROM materias WHERE nombre IN ('Algoritmos', 'Redes')
);

-- Eliminar un registro con todas sus relaciones:
-- Orden: limpiar tabla intermedia, luego eliminar el registro
DELETE FROM inscripciones
WHERE estudiante_id = (SELECT estudiante_id FROM estudiantes WHERE nombre = 'Juan');
DELETE FROM estudiantes WHERE nombre = 'Juan';

-- Eliminar registros que no tienen ninguna relación:
DELETE FROM estudiantes
WHERE estudiante_id NOT IN (SELECT DISTINCT estudiante_id FROM inscripciones);


-- =============================================================
-- 5. TABLA INTERMEDIA CON DATOS PROPIOS
-- =============================================================
-- Para qué: cuando la relación en sí tiene atributos propios.
-- Cuándo: nota de un estudiante en una materia, cantidad de un
--         producto en un pedido, rol de un empleado en un proyecto.
-- Cómo: agregar columnas adicionales a la tabla intermedia.

-- Sintaxis:
-- CREATE TABLE tabla_intermedia (
--     fk_a        INT,
--     fk_b        INT,
--     dato_propio TIPO NOT NULL,
--     PRIMARY KEY (fk_a, fk_b),
--     FOREIGN KEY (fk_a) REFERENCES tabla_a(pk),
--     FOREIGN KEY (fk_b) REFERENCES tabla_b(pk)
-- );

-- Tabla sin datos propios — solo relaciona:
CREATE TABLE inscripciones (
    estudiante_id INT,
    materia_id    INT,
    PRIMARY KEY (estudiante_id, materia_id),
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(estudiante_id),
    FOREIGN KEY (materia_id)    REFERENCES materias(materia_id)
);

-- Tabla con dato propio — nota del estudiante en la materia:
CREATE TABLE inscripciones_con_nota (
    estudiante_id INT,
    materia_id    INT,
    nota          DECIMAL(4,2) NOT NULL DEFAULT 0.00,
    fecha_inicio  DATE,
    PRIMARY KEY (estudiante_id, materia_id),
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(estudiante_id),
    FOREIGN KEY (materia_id)    REFERENCES materias(materia_id)
);

-- INSERT con dato propio:
INSERT INTO inscripciones_con_nota (estudiante_id, materia_id, nota)
VALUES (1, 3, 4.5),   -- Juan - Bases de Datos - 4.5
       (1, 5, 3.8),   -- Juan - Programación   - 3.8
       (2, 3, 4.0);   -- Ana  - Bases de Datos - 4.0


-- =============================================================
-- 6. FLUJO SEGURO PARA OPERACIONES EN TABLAS RELACIONADAS
-- =============================================================

-- ANTES DE INSERT:
-- 1. Verificar que el padre existe
SELECT pk FROM tabla_padre WHERE condición;
-- 2. Verificar que la relación no existe ya (en N:M)
SELECT * FROM tabla_intermedia WHERE fk_a = id AND fk_b = id;
-- 3. Insertar

-- ANTES DE DELETE en tabla padre:
-- 1. Verificar qué hijos dependen del padre
SELECT * FROM tabla_intermedia WHERE fk_columna = id;
-- 2. Eliminar todos los hijos primero
-- 3. Eliminar el padre

-- ANTES DE UPDATE con FK:
-- 1. Verificar que el nuevo valor referenciado existe
SELECT pk FROM tabla_padre WHERE condición;
-- 2. Ejecutar el UPDATE

-- VERIFICAR TODAS LAS RELACIONES DE UN REGISTRO:
-- Con ID conocido:
SELECT * FROM tabla_intermedia WHERE fk_columna = id;

-- Con subquery:
SELECT * FROM tabla_intermedia
WHERE fk_columna = (SELECT pk FROM tabla_padre WHERE condición);

-- REGLA: si alguna consulta devuelve filas →
--        elimina esas relaciones antes de eliminar el padre.
--        Si todas devuelven 0 filas → puedes eliminar directamente.