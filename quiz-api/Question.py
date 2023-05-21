# Exemple de création de classe en python
import sqlite3
import json

class Question():
	def __init__(self, title: str, text: str, image: str, position: int, possibleAnswers: str) :
		self.title = title
		self.text = text
		self.image = image
		self.position = position
		self.possibleAnswers = possibleAnswers

	def to_dict(self):
		return {
			"title": self.title,
			"text": self.text,
			"image": self.image,
			"position": self.position,
			"possibleAnswers": self.possibleAnswers,
		}
		
	
def to_json(question: Question):
		return json.dumps(question.to_dict())
	
def from_json(json_string):
    data = json.loads(json_string)
    return Question(**data)

def generate_insert_sql(question: Question):
	db_connection = sqlite3.connect('bdd_quiz.db')
	db_connection.isolation_level = None
	cur = db_connection.cursor()
	possible_answers_str = json.dumps(question.possibleAnswers)
	cur.execute("begin")
	sql = """
    INSERT INTO Question (title, text, image, position, possibleAnswers)
    VALUES (?, ?, ?, ?, ?)
    """
	# Créer un tuple contenant les valeurs à insérer
	values = (question.title, question.text, question.image, question.position, possible_answers_str)
	cur.execute(sql, values)
	cur.execute("commit")
	db_connection.close()


def update_question(query, params):
	conn = sqlite3.connect('bdd_quiz.db')
	cursor = conn.cursor()
	result = cursor.execute(query, params)
	affected_rows = cursor.rowcount
	conn.commit()
	conn.close()
	
	if affected_rows == 0:
		return 404
	
	return 204


