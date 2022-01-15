import MySQLdb

db = MySQLdb.connect('localhost', 'root', 'root')

with db:
    cursor = db.cursor()
    cursor.execute("""CREATE DATABASE IF NOT EXISTS cinematic;""")