NOTA: luego de ejecutar cada instrucción de los ejercicios, utiliza MysQL Workbench para inspeccionar las tablas, 
      ver los cambios realizados en su estructura, e intenta cargar datos para verificar si todo funciona correctamente.

1. Crea dos nuevas tablas: 
	- tabla "awards", con los siguientes campos:
		- award_id (entero, clave primaria, autoincremental)
		- award_name (texto de longitud 100)
    
    - tabla "audit_log", con los siguientes campos:
		- audit_id (entero, clave primaria, autoincremental)
		- table_name (texto de longitud 100, no nulo)
		- operation_type (tipo ENUM, con los valores 'INSERT', 'UPDATE' y 'DELETE', no nulo)
		- record_id (entero, no nulo)
		- changed_by (texto de longitud 100, no nulo)
		- change_timestamp (tipo TIMESTAMP, valor por defecto la fecha y hora actual)
		- old_values (tipo TEXT)
		- new_values (tipo TEXT)

USE cineDB;



CREATE TABLE awards (
    award_id   INT PRIMARY KEY AUTO_INCREMENT,
    award_name VARCHAR(100)
);

CREATE TABLE audit_log (
    audit_id         INT PRIMARY KEY AUTO_INCREMENT,
    table_name       VARCHAR(100) NOT NULL,
    operation_tipe   ENUM('INSERT','UPDATE','DELETE') NOT NULL,
    record_id        INT NOT NULL,
    changed_by       VARCHAR(100) NOT NULL,
    change_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    old_values       TEXT,
    new_values       TEXT
);

2. Agregar una nueva columna "duration", de tipo entero, a la tabla "movies".

ALTER TABLE cineDB.movies ADD COLUMN duration INT;

3. Agrega una nueva columna "rating" a la tabla "movies". El campo debe permitir numeros de 2 digitos y 1 decimal, y estar restringido sólo a números entre 0 y 10. 

ALTER TABLE cineDB.movies ADD COLUMN rating DECIMAL(3,1) 
CHECK (rating >= 0 AND rating<= 10);

4. En la tabla "movies", modifica el nombre de la columna "duration" a "duration_minutes".

ALTER TABLE cineDB.movies RENAME COLUMN duration 
TO duration_minutes;

5. Modifica el tipo de dato de la columna "studio_name" en la tabla "studios" para aceptar hasta 80 caracteres.

6. Establece el valor por defecto de la columna "duration_minutes" en 0.

7. Agrega la restricción UNIQUE al campo "country_name" de la tabla "countries". Intenta insertar el país "España" y revisa que sucede.

8. Establece a "No Nulo" y "único" el campo "award_name" de la tabla "awards".

9. En la tabla "movies", agrega una clave foránea que relacione el campo "studio_id" de esta tabla con el campo "studio_id" de la tabla "studios".

10. Elimina la tabla "movie_review".

11. Elimina, si existe, la tabla "movie_review". Compara la diferencia y resultado de esta sentencia con la del ejercicio 10.

12. Elimina las columnas "duration_minutes" y "rating" de la tabla "movies".