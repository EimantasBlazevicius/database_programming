import MySQLdb

db = MySQLdb.connect('localhost', 'root', 'root', database='cinematic')

select_movies = """SELECT * FROM movies WHERE year > 2002;"""

with db:
    cursor = db.cursor()
    cursor.execute(select_movies)

    print(cursor.fetchone())  # gets first result
    print(cursor.fetchmany(size=2))  # gets second and third result
    print(cursor.fetchall())  # gets the rest of them
