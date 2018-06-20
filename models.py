import psycopg2
import secret


try:
	conn = psycopg2.connect(secret.connect_str)
	cur = conn.cursor()
except Exception as e:
	print("Uh oh, can't connect. Invalid dbname, user or password?")
	print(e)

def clean_data(all_submissions, reverse):
	context = {
		'items':[]
		}
	for i, this_item in enumerate(all_submissions):
		if i==0:
			if reverse:
				context['last'] = this_item[0]
			else:
				context['first'] = this_item[0]
		if i==4:
			if reverse:
				context['first'] = this_item[0]
			else:
				context['last'] = this_item[0]
		context['items'].append({
			'id': this_item[0],
			'url': this_item[1],
			'image_url': this_item[2],
			'score': this_item[3]
		})
	return context
	
def get_items(item_id=None, action=None):
	reverse = False
	if item_id:
		if action == 'next':
			q_string = "SELECT * FROM submissions WHERE pk<%s ORDER BY pk DESC LIMIT 5;"
		else:
			reverse = True
			q_string = "SELECT * FROM submissions WHERE pk>%s ORDER BY pk ASC LIMIT 5;"
		cur.execute(q_string, (item_id,))
	else:
		q_string = "SELECT * FROM submissions ORDER BY pk DESC LIMIT 5;"
		cur.execute(q_string)
	all_submissions = cur.fetchall()
	return clean_data(all_submissions, reverse)

def create_submission(url, image_url, score):
	sql_statement = """
	INSERT INTO submissions
	(url, image_url, score)
	VALUES
	(%s,%s,%s)
	RETURNING "pk";
	"""
	cur.execute(sql_statement, (url, image_url, score))
	_id = cur.fetchone()[0]
	conn.commit()
	if _id:
		return 1
	return False