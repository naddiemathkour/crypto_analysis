import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='postgres',
    user='postgres',
    password='',
    port='5432'
)

cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXIST""")

conn.commit()

#Close cursor and connection when finished
cur.close()
conn.close