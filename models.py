import psycopg2
import secret


try:
	conn = psycopg2.connect(secret.connect_str)
	cur = conn.cursor()
except Exception as e:
	print("Uh oh, can't connect. Invalid dbname, user or password?")
	print(e)
	
def get_submissions(loginfo):
	sql_statement = "SELECT * FROM submissions;"
	cur.execute(sql_statement, loginfo)
	return cur.fetchone()

def create_submission(url, score):
	sql_statement = """
	INSERT INTO submissions
	(url, score)
	VALUES
	(%s,%s)
	RETURNING "pk";
	"""
	cur.execute(sql_statement, (url, score))
	_id = cur.fetchone()[0]
	conn.commit()
	if _id:
		return 1
	return False