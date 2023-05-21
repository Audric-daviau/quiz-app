from flask import Flask, request
import hashlib
import jwt
from flask_cors import CORS
import sqlite3
import json
import Question

app = Flask(__name__)
CORS(app)

SECRET_KEY = 'votre_clé_secrète'
HASHED_PASSWORD = b'\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@'  # Mot de passe hashé

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    password = payload.get('password')

    # Hasher le mot de passe à tester
    hashed_password = hashlib.md5(password.encode('utf-8')).digest()

    if hashed_password == HASHED_PASSWORD:
        # Générer un token JWT
        token = jwt.encode({'username': 'votre_utilisateur'}, SECRET_KEY, algorithm='HS256')
        return {'token': token}

    return 'Unauthorized', 401

# Chemin vers le fichier de base de données SQLite
DATABASE_PATH = 'bdd_quiz.db'

@app.route('/questions', methods=['POST'])
def addQuestion():
    #Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    if token is None:
        return 'Unauthorized', 401
    #récupèrer un l'objet json envoyé dans le body de la requète
    payload = request.get_json()
    title = payload.get('title')
    text = payload.get('text')
    image = payload.get('image')
    position = payload.get('position')
    possibleAnswers = payload.get('possibleAnswers')
    json_string = json.dumps(payload)
    quest = Question.from_json(json_string)
    Question.generate_insert_sql(quest)
    print(quest.title)
    print(Question.to_json(quest))
    if payload:
        return {'id': 1}

@app.route('/questions', methods=['GET'])
def getQuestionByPosition():
    position = request.args.get('position', type = int)
    params = (position,)
    conn = sqlite3.connect('bdd_quiz.db')
    cursor = conn.cursor()
    cursor.execute('select * from Question where position = ?', params)
    result = cursor.fetchone()
    conn.close()
    if result is None:
        return {"status": "error", "message": "Question not found"}, 404
    else :
        id, title, text, image, position, possibleAnswers = result
        quest = {
        'title': title,
        'text': text,
        'image': image,
        'position': position,
        'possibleAnswers': json.loads(possibleAnswers)
        }
        return {"id": id, "title": quest.title, "text": quest.text, "position": quest.position, "image": quest.image, "possibleAnswers": quest.possibleAnswers}
        


@app.route('/questions/<int:questionId>', methods=['GET'])
def getQuestionById(questionId):
    params = (questionId,)
    conn = sqlite3.connect('bdd_quiz.db')
    cursor = conn.cursor()
    cursor.execute('select * from Question where id = ?', params)
    result = cursor.fetchone()
    conn.close()
    if result is None:
        return {"status": "error", "message": "Question not found"}, 404
    else :
        id, title, text, image, position, possibleAnswers = result
        quest = {
            'title': title,
            'text': text,
            'image': image,
            'position': position,
            'possibleAnswers': json.loads(possibleAnswers)
        }
        return {"id": id, "title": quest.title, "text": quest.text, "position": quest.position, "image": quest.image, "possibleAnswers": quest.possibleAnswers}
    


@app.route('/questions/<int:questionId>', methods=['PUT'])
def updateQuestionById(questionId):
    #Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    if token is None:
        return 'Unauthorized', 401
    data = request.get_json()
    title = data.get('title')
    text = data.get('text')
    image = data.get('image')
    position = data.get('position')
    possibleAnswers = data.get('possibleAnswers')
    query = '''UPDATE question
               SET title = ?, text = ?, image = ?, position = ?, possibleAnswers = ?
               WHERE id = ?'''
    params = (title, text, image, position, json.dumps(possibleAnswers), questionId)
    response = Question.update_question(query, params)
    
    if response == 204:
        return {"status": "success", "message": "Question updated successfully"}, response
    else :
        return {"status": "error", "message": "Question not found"}, response


@app.route('/questions/<int:questionId>', methods=['DELETE'])
def deleteQuestionById(questionId):
    token = request.headers.get('Authorization')
    if token is None:
        return 'Unauthorized', 401
    # Delete the question from the database
    conn = sqlite3.connect('bdd_quiz.db')
    cursor = conn.cursor()
    
    query = '''DELETE FROM question WHERE id = ?'''
    params = (questionId, )

    cursor.execute(query, params)
    affected_rows = cursor.rowcount
    conn.commit()
    conn.close()

    if affected_rows != 0:
        return {"status": "success", "message": "Question deleted successfully"}, 204
    else :
        return {"status": "error", "message": "Question not found"}, 404


@app.route('/questions/all', methods=['DELETE'])
def deleteAllQuestions():
    token = request.headers.get('Authorization')
    if token is None:
        return 'Unauthorized', 401
    # Delete the question from the database
    conn = sqlite3.connect('bdd_quiz.db')
    cursor = conn.cursor()
    
    query = '''DELETE FROM question'''
    cursor.execute(query)
    affected_rows = cursor.rowcount
    conn.commit()
    conn.close()

    if affected_rows != 0:
        return {"status": "success", "message": "Question deleted successfully"}, 204
    else :
        return {"status": "error", "message": "Question not found"}, 404

@app.route('/participations/all', methods=['DELETE'])
def deleteAllParticipations():
    token = request.headers.get('Authorization')
    if token is None:
        return 'Unauthorized', 401
    # Delete the question from the database
    conn = sqlite3.connect('bdd_quiz.db')
    cursor = conn.cursor()
    
    query = '''DELETE FROM Participant'''
    cursor.execute(query)
    affected_rows = cursor.rowcount
    conn.commit()
    conn.close()

    if affected_rows != 0:
        return {"status": "success", "message": "Question deleted successfully"}, 204
    else :
        return {"status": "error", "message": "Question not found"}, 404


if __name__ == '__main__':
    app.run()