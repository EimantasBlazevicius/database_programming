import MySQLdb

db = MySQLdb.connect('localhost', 'root', 'root', database='cinematic')

drop_movies = """DROP TABLE movies;"""
drop_directors = """DROP TABLE directors;"""

with db:
    cursor = db.cursor()
    cursor.execute(drop_movies)
    cursor.execute(drop_directors)
