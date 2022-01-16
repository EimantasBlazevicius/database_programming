import MySQLdb

db = MySQLdb.connect('localhost', 'root', 'root', database='cinematic')

create_tables = """
CREATE TABLE directors(
    director_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL, 
    rating INT NOT NULL
);
CREATE TABLE movies(
    movie_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
    title VARCHAR(30) NOT NULL,
    year INT UNSIGNED NOT NULL, 
    category VARCHAR(30) NOT NULL,
    director_id INT NOT NULL, 
    rating INT NOT NULL,
    FOREIGN KEY (director_id) REFERENCES directors(director_id)
);
"""

with db:
    cursor = db.cursor()
    cursor.execute(create_tables)