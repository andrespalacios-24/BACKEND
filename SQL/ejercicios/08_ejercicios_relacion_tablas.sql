1. Crea una tabla llamada "movie_review" con los siguientes campos: 
    - review_id (entero, clave primaria, autoincremental)
    - movie_id (entero, foránea relacionada con la tabla "movies").
    - review_text (texto de longitud 1000, no nulo)
    - review_timestamp (tipo timestamp, valor por defecto la fecha y hora actual)
   
CREATE TABLE movie_review (
    review_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    movie_id INT NOT NULL,
    review_text VARCHAR(1000) NOT NULL,
    review_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id));

USE cineDB;
CREATE TABLE movie_review (
review_id INT PRIMARY KEY AUTO_INCREMENT,
movie_id INT NOT NULL,
review_text VARCHAR(1000) NOT NULL,
review_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (movie_id) REFERENCES movies(movie_id)

);

2. Crea una tabla llamada "movie_award" con los siguientes campos: 
    - movie_id (entero, clave principal y foránea relacionada con la tabla "movies").
    - award_id (entero, clave principal y foránea relacionada con la tabla "awards")

USE cineDB;
CREATE TABLE movie_award (
movie_id INT,
award_id INT,
PRIMARY KEY (movie_id, award_id)
FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
FOREIGN KEY (award_id) REFERENCES awards(award_id),
);