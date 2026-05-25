-- =============================================================
-- MYSQL - TABLAS Y TIPOS DE DATOS
-- Fuentes: MySQL 8.0 Docs + W3Schools
-- =============================================================


-- =============================================================
-- 1. TIPOS DE DATOS
-- =============================================================
-- MySQL agrupa los tipos de datos en tres categorías:
-- numéricos, texto y fechas/tiempo.
-- Elegir el tipo correcto importa porque afecta:
--   - Cuánto espacio ocupa en disco
--   - Qué valores acepta o rechaza
--   - El rendimiento de las consultas


-- -------------------------------------------------------------
-- 1.1 NUMÉRICOS ENTEROS
-- -------------------------------------------------------------

-- TINYINT
-- Rango: -128 a 127 (con signo) / 0 a 255 (sin signo)
-- Ocupa: 1 byte
-- Cuándo usarlo: valores muy pequeños y acotados
-- Ejemplo real: estado activo/inactivo (0 o 1), edad de una mascota
edad_mascota TINYINT,

-- SMALLINT
-- Rango: -32,768 a 32,767
-- Ocupa: 2 bytes
-- Cuándo usarlo: contadores pequeños, códigos de área, año de nacimiento
año_nacimiento SMALLINT,

-- INT (= INTEGER)
-- Rango: -2,147,483,648 a 2,147,483,647
-- Ocupa: 4 bytes
-- Cuándo usarlo: IDs, cantidades, precios enteros — el tipo más común
-- Es el tipo por defecto cuando necesitas un número entero sin decimales
id INT,
cantidad INT,

-- BIGINT
-- Rango: ±9.2 × 10^18
-- Ocupa: 8 bytes
-- Cuándo usarlo: IDs en sistemas con millones de registros,
--               timestamps en milisegundos, contadores de redes sociales
visitas_totales BIGINT,


-- -------------------------------------------------------------
-- 1.2 NUMÉRICOS CON DECIMALES
-- -------------------------------------------------------------

-- DECIMAL(M, D)  también escrito NUMERIC(M, D)
-- M = dígitos totales, D = dígitos después del punto
-- Cuándo usarlo: dinero, precios, valores financieros
--   → usa DECIMAL porque es exacto (no tiene error de redondeo)
precio DECIMAL(10, 2),     -- hasta 99,999,999.99
salario DECIMAL(8, 2),     -- hasta 999,999.99

-- FLOAT y DOUBLE
-- Cuándo usarlos: mediciones científicas, coordenadas GPS, estadísticas
--   → son aproximados (pueden tener mínimos errores de redondeo)
--   → NUNCA los uses para dinero
latitud DOUBLE,
temperatura FLOAT,


-- -------------------------------------------------------------
-- 1.3 TEXTO
-- -------------------------------------------------------------

-- CHAR(n)
-- Longitud FIJA: siempre ocupa exactamente n caracteres (rellena con espacios)
-- Máximo: 255 caracteres
-- Cuándo usarlo: datos de longitud siempre igual — códigos, siglas, abreviaciones
-- Ejemplo: código de país ('CO', 'US'), género ('M', 'F'), código postal
codigo_pais CHAR(2),       -- siempre 2 caracteres
codigo_postal CHAR(6),     -- siempre 6 caracteres

-- VARCHAR(n)
-- Longitud VARIABLE: solo ocupa el espacio que necesita + 1-2 bytes extra
-- n = número MÁXIMO de caracteres que puede guardar (tú decides el límite)
-- Máximo teórico: 65,535 — pero en la práctica usa valores razonables
-- Cuándo usarlo: texto de longitud variable — nombres, emails, títulos
--
-- ¿Qué número va dentro del paréntesis?
--   → El máximo de caracteres que esperas para ese campo
--   → Ejemplos comunes en backends:
nombre VARCHAR(100),       -- nombres de persona: raro que pasen de 100
email VARCHAR(150),        -- emails: estándar de la industria es 254, usa 150-255
ciudad VARCHAR(100),
titulo_producto VARCHAR(200),
contraseña_hash VARCHAR(255),  -- hashes siempre tienen longitud fija conocida

-- TEXT
-- Para textos largos sin límite práctico (hasta ~65,535 bytes)
-- Cuándo usarlo: descripciones, comentarios, contenido de artículos
-- No puede tener valor por defecto (DEFAULT) — diferencia clave con VARCHAR
descripcion TEXT,
contenido_articulo TEXT,

-- ENUM('valor1', 'valor2', ...)
-- Solo acepta uno de los valores listados
-- Cuándo usarlo: campos con opciones fijas y conocidas
-- Ventaja: MySQL rechaza cualquier valor que no esté en la lista
estado ENUM('activo', 'inactivo', 'pendiente'),
rol ENUM('admin', 'editor', 'viewer'),


-- -------------------------------------------------------------
-- 1.4 FECHAS Y TIEMPO
-- -------------------------------------------------------------

-- DATE
-- Formato: 'YYYY-MM-DD'
-- Cuándo usarlo: fechas sin hora — cumpleaños, fecha de contrato, fecha de entrega
fecha_nacimiento DATE,
fecha_contrato DATE,

-- DATETIME
-- Formato: 'YYYY-MM-DD HH:MM:SS'
-- Cuándo usarlo: registrar cuándo ocurrió algo exactamente
-- No cambia con la zona horaria del servidor
creado_en DATETIME,
ultima_modificacion DATETIME,

-- TIMESTAMP
-- Igual que DATETIME en formato, pero:
--   → Se convierte automáticamente a UTC al guardar
--   → Se convierte a la zona horaria local al leer
--   → Rango limitado: 1970-01-01 a 2038-01-19
--   → Muy útil para auditoría (cuándo se insertó/modificó un registro)
creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

-- TIME
-- Formato: 'HH:MM:SS'
-- Cuándo usarlo: duración de algo, horario de apertura
hora_apertura TIME,
duracion_llamada TIME,

-- YEAR
-- Solo guarda el año: 1901 a 2155
año_publicacion YEAR,


-- -------------------------------------------------------------
-- 1.5 BOOLEAN
-- -------------------------------------------------------------

-- MySQL no tiene tipo BOOLEAN nativo.
-- BOOLEAN y BOOL son sinónimos de TINYINT(1)
-- 0 = FALSE, 1 = TRUE
esta_activo BOOLEAN,       -- internamente es TINYINT(1)
email_verificado BOOLEAN DEFAULT FALSE,


-- =============================================================
-- 2. FLAGS DE MYSQL WORKBENCH (columnas del editor visual)
-- =============================================================
-- Cuando creas una tabla en Workbench, ves estas casillas:
-- PK | NN | UQ | BIN | UN | ZF | AI | G
--
-- Fuente oficial: MySQL Workbench Manual - Columns Tab

-- PK → PRIMARY KEY (Llave Primaria)
--   Identifica de forma única cada fila de la tabla.
--   Automáticamente implica NN (no puede ser NULL).
--   Una tabla solo puede tener una PRIMARY KEY.
--   Equivalente en código: PRIMARY KEY

-- NN → NOT NULL (No Nulo)
--   El campo no puede quedar vacío — siempre debe tener un valor.
--   Úsalo en campos obligatorios: nombre, email, fecha, etc.
--   Equivalente en código: NOT NULL

-- UQ → UNIQUE INDEX (Índice Único)
--   Todos los valores en esta columna deben ser diferentes entre sí.
--   A diferencia de PK, puede haber varios campos UNIQUE en una tabla.
--   Ejemplo: email (dos usuarios no pueden tener el mismo email)
--   Equivalente en código: UNIQUE

-- BIN → BINARY
--   Indica que el campo guarda datos binarios en lugar de texto.
--   Afecta la comparación: distingue mayúsculas de minúsculas.
--   Uso avanzado: normalmente no lo necesitas al aprender.
--   Equivalente en código: BINARY

-- UN → UNSIGNED (Sin signo)
--   Solo válido para tipos numéricos enteros.
--   Elimina los números negativos y duplica el rango positivo.
--   Ejemplo: INT normal va de -2,147,483,648 a 2,147,483,647
--            INT UNSIGNED va de 0 a 4,294,967,295
--   Cuándo usarlo: IDs, cantidades — nunca van a ser negativos
--   Equivalente en código: UNSIGNED

-- ZF → ZEROFILL (Relleno con ceros)
--   Si el número tiene menos dígitos que el ancho definido, rellena con ceros.
--   Ejemplo: INT(3) con ZF → el número 5 se muestra como 005
--   Es una opción de visualización, no cambia el valor guardado.
--   Uso real: códigos con formato fijo (ej: número de expediente)
--   Equivalente en código: ZEROFILL

-- AI → AUTO_INCREMENT (Autoincremento)
--   MySQL asigna automáticamente el siguiente número al insertar una fila.
--   Solo se puede usar en columnas numéricas enteras.
--   Típicamente va en la columna ID junto con PK.
--   Equivalente en código: AUTO_INCREMENT

-- G → Generated Column (Columna Generada)
--   El valor de esta columna se calcula automáticamente a partir de otras columnas.
--   Tú defines la fórmula; MySQL la ejecuta solo.
--   Ejemplo: columna 'precio_total' calculada como cantidad * precio_unitario
--   Disponible desde MySQL 5.7
--   Equivalente en código: GENERATED ALWAYS AS (expresión)


-- =============================================================
-- 3. CREAR UNA TABLA - SINTAXIS COMPLETA
-- =============================================================

-- Sintaxis básica:
-- CREATE TABLE nombre_tabla (
--     nombre_columna TIPO_DE_DATO [flags/restricciones],
--     ...
--     PRIMARY KEY (columna)
-- );

-- Ejemplo completo - tabla de usuarios para un backend:
CREATE TABLE usuarios (

    -- id: numérico, sin signo, autoincremento, llave primaria
    -- PK + NN + UN + AI marcados en Workbench
    id          INT UNSIGNED NOT NULL AUTO_INCREMENT,

    -- nombre: texto variable, obligatorio
    -- NN marcado en Workbench
    nombre      VARCHAR(100) NOT NULL,

    -- email: texto variable, obligatorio y único
    -- NN + UQ marcados en Workbench
    email       VARCHAR(150) NOT NULL UNIQUE,

    -- contraseña: texto variable, obligatorio
    -- NN marcado en Workbench
    contrasena  VARCHAR(255) NOT NULL,

    -- rol: solo acepta valores definidos, por defecto 'viewer'
    rol         ENUM('admin', 'editor', 'viewer') NOT NULL DEFAULT 'viewer',

    -- activo: booleano, por defecto verdadero
    activo      BOOLEAN NOT NULL DEFAULT TRUE,

    -- fecha de registro: se llena automáticamente al insertar
    -- NN marcado en Workbench
    creado_en   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- última actualización: se actualiza automáticamente al modificar
    actualizado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                   ON UPDATE CURRENT_TIMESTAMP,

    -- definir la llave primaria
    PRIMARY KEY (id)
);


-- Ejemplo simple - tabla de productos:
CREATE TABLE productos (
    id          INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nombre      VARCHAR(200) NOT NULL,
    descripcion TEXT,                          -- puede ser NULL (no es obligatorio)
    precio      DECIMAL(10, 2) NOT NULL,
    stock       INT UNSIGNED NOT NULL DEFAULT 0,
    activo      BOOLEAN NOT NULL DEFAULT TRUE,
    creado_en   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);


-- =============================================================
-- 4. RESUMEN - CUÁNDO USAR CADA TIPO
-- =============================================================

-- IDs y contadores             → INT UNSIGNED AUTO_INCREMENT
-- Números enteros normales     → INT
-- Números muy pequeños (0/1)   → TINYINT o BOOLEAN
-- Dinero / precios             → DECIMAL(10, 2)
-- Coordenadas / mediciones     → DOUBLE o FLOAT
-- Texto longitud fija          → CHAR(n)   — códigos, siglas
-- Texto longitud variable      → VARCHAR(n) — nombres, emails, títulos
-- Texto largo / descripciones  → TEXT
-- Opciones fijas               → ENUM('a', 'b', 'c')
-- Solo fecha                   → DATE
-- Fecha y hora exacta          → DATETIME
-- Registro de auditoría        → TIMESTAMP
-- Verdadero / Falso            → BOOLEAN (= TINYINT(1))

-- REGLA DE ORO para VARCHAR(n):
--   n = el máximo razonable para ese campo en tu sistema
--   No uses VARCHAR(255) para todo por costumbre —
--   piensa cuántos caracteres necesita realmente ese dato.
--   nombres → 100, emails → 150, títulos → 200, hashes → 255