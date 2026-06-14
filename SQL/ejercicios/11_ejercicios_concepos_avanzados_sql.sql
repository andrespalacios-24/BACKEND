1. Crear una vista llamada "vw_movie" con la siguiente información de todas las películas:
   	- ID de película
    - Nombre de película
    - Año Estreno
    - ID y nombre del director
    - ID y nombre del Estudio 
    - Total de espectadores 
    - Total de recaudación

2. Crear una vista llamada "vw_movie_90" con la siguiente información de todas las películas estrenadas en la década del '90:
   	- ID de película
    - Nombre de película
    - Año Estreno
    - Total de espectadores 
    - Total de recaudación
    
3. Crear una vista llamada "vw_movie_actor" con las películas y sus actores correspondientes.

4. Crear una vista llamada "vw_movie_director" con las películas y su correspondiente director.

5. Utilizando las vistas creadas en los ejercicios 3 y 4, y la sentencia "UNION", recupera los actores y director de la película "The Matrix":
	- Muestra los encabezados de columna como "Nombre" y "Rol"
    - En la columna "Rol", indica si es Actor o Director. 
    - Ordena los resultados por Nombre.

6. Crear cinco procedimientos: 
	- "sp_insert_movie" para insertar una nueva película.
	- "sp_delete_movie" para eliminar una película.
	- "sp_update_release_year" para actualizar el año de estreno de una película.
    - "sp_update_viewers" para actualizar la cantidad de espectadores de una película.
    - "sp_update_revenue" para actualizar la recaudación de una película.

7. Crear triggers para registrar inserciones, actualizaciones y eliminaciones en la tabla "movies".
   La información de la operación realizada se registrará en la tabla "audit_log":
	- nombre de la tabla impactada
    - el tipo de operación que se realizó (INSERT, UPDATE, DELETE)
    - el ID del registro impactado
    - el usuario y fecha y hora que se realizó
    - los datos impactados (usando la función JSON_OBJECT() para almacenar los datos previos y nuevos de manera estructurada).	

8. Insertar la película "Avatar" utilizando el procedimiento creado en el ejercicio 6.
    - Nombre: Avatar
    - Año Estreno: 2009
    - ID Director: 6
    - ID Estudio: 6
    - Total Espectadores: 331000000
    - Total Recaudación: 2923706026

9. Utiliza la vista creada en el ejercicio 1 para recuperar la información de las películas "Titanic", "Gladiator" y "Avatar".

10. Utilizando los procedimientos creados en el ejercicio 6:
	- Actualiza a 26000300 la cantidad de espectadores de "The Godfather".
    - Actualiza a 1993 el año de estreno de "Schindler’s List".
    - Actualiza a 95000000.00 la recaudación de "Edward Scissorhands".
    - Elimina la película "Avatar".
    
11. Revisa la tabla de auditoría y chequea que los triggers creados en el ejercicio 7 se ejecutaron correctamente.

12. Crear dos índices, llamados "idx_release_year" e "idx_revenue", en las columnas "release_year" y "total_revenue" de la tabla "movies". 

13. Crear un índice, llamado "idx_movie_actor", compuesto por las columnas "movie_id" y "actor_id" de la tabla "movie_actor".

14. Elimina el índice "idx_revenue" creado en el ejercicio 12.

15. Elimina la vista creada en el ejercicio 2.

16. Elimina el procedimiento "sp_update_release_year" creado en el ejercicio 6.

17. Usando "Transacciones", inserta una película con el procedimiento creado en el ejercicio 6 y luego confirma dicha operación. Verifica si la película fue insertada.

18. Usando "Transacciones", inserta una película con el procedimiento creado en el ejercicio 6 y luego vuelve atrás dicha operación. Verifica si la película fue insertada.

NOTA: para los ejercicios 17 y 18 asegúrate de tener la opción "Auto-Commit Transactions" (del menú "Query") desactivada.
