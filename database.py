import psycopg2

DB_HOST = "192.168.0.41"
DB_NAME = "gardendb"
DB_USER = "pi"
DB_PASSWORD = "6201"

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASSWORD, host = DB_HOST)

cur = conn.cursor()

cur.execute("SELECT * FROM general;")

print(cur.fetchall())

conn.close()
