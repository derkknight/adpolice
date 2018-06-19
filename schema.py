
import psycopg2
import secret


try:
	conn = psycopg2.connect(secret.connect_str)
	cur = conn.cursor()
except Exception as e:
	print("Uh oh, can't connect. Invalid dbname, user or password?")
	print(e)

cur.execute("DROP TABLE IF EXISTS submissions;")

cur.execute(
    """
    CREATE TABLE submissions (
        pk SERIAL PRIMARY KEY,
        url VARCHAR,
        image_url VARCHAR,
        score INTEGER
    );
    """
)

conn.commit()
conn.close()