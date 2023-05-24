from flask import Flask, request, jsonify
import hashlib
import jwt
from flask_cors import CORS
import sqlite3
import json
import Question
from datetime import datetime
import savebdd

app = Flask(__name__)
CORS(app)

SECRET_KEY = 'votre_clé_secrète'
HASHED_PASSWORD = b'\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@'  # Mot de passe hashé

@app.route('/quiz-info', methods=['GET'])
def getQuizInfo():
    try:
        conn = sqlite3.connect('bdd_quiz.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM Question')
        result = cursor.fetchone()
        cursor.execute("select pseudo, score, date from Participant")
        rows = cursor.fetchall()
        scores = []
        for row in rows:
            score_dict = {"playerName": row[0], "score": row[1], "date": row[2]}
            scores.append(score_dict)
        conn.close()
        scores = sorted(scores, key=lambda x: x['score'], reverse=True)
        if result is not None:
            return {"size": result[0], "scores": scores}, 200
        else:
            return {"status": "error", "message": "Cannot get the questions count"}, 500

    except Exception as e:
        return {"status": "error", "message": str(e)}, 500
    

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

    return 'unauthorized', 401

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
    if payload:
        return {'id': 1}

@app.route('/questions', methods=['GET'])
def getQuestionByPosition():
    try:
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
            return {
                "id": id, 
                "title": quest['title'], 
                "text": quest['text'], 
                "position": quest['position'], 
                "image": quest['image'], 
                "possibleAnswers": quest['possibleAnswers']
            }
    
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500


@app.route('/questions/all', methods=['GET'])
def getAllQuestions():
    conn = sqlite3.connect('bdd_quiz.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Question')
    rows = cursor.fetchall()
    conn.close()

    if rows is None:
        return {"status": "error", "message": "Question not found"}, 404

    questions = []
    for row in rows:
        question = {
            "id": row[0],
            "title": row[1],
            "text": row[2],
            "image": row[3],
            "position": row[4],
            "possibleAnswers": json.loads(row[5])  # assuming this is stored as JSON string
        }
        questions.append(question)

    return questions, 200



@app.route('/questions/<int:questionId>', methods=['GET'])
def getQuestionById(questionId):
    try:
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
            return {
                "id": id, 
                "title": quest['title'], 
                "text": quest['text'], 
                "position": quest['position'], 
                "image": quest['image'], 
                "possibleAnswers": quest['possibleAnswers']
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

    


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
def deleteAllParticipants():
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


@app.route('/participations', methods=['POST'])
def addParticipants():
    payload = request.get_json()
    playerName = payload.get('playerName')
    answers = payload.get('answers')
    conn = sqlite3.connect('bdd_quiz.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Question')
    result = cursor.fetchone()
    if len(answers) != result[0] :
        return {"status": "error", "message": "not enough or too much"}, 400
    
    cursor.execute('select possibleAnswers from Question')
    try:
        rows = cursor.fetchall()
        i = 0
        score = 0
        for row in rows:
            possible_answers = json.loads(row[0])  # Convert the JSON string to a Python list
            if possible_answers[answers[i]-1]["isCorrect"] is True:
                score += 1
            i += 1
            
        answers_str = json.dumps(answers)
        sql = """
        INSERT INTO Participant (pseudo, answers, score, date)
        VALUES (?, ?, ?, ?)
        """
        # Créer un tuple contenant les valeurs à insérer
        now = datetime.now()
        date_time_string = now.strftime("%Y-%m-%d %H:%M:%S")
        values = (playerName, answers_str, score, date_time_string)
        cursor.execute(sql, values)
        cursor.execute("commit")
        conn.close()
        return {"playerName": playerName, "score": score}, 200
    except Exception as e:
        cursor.close()
        conn.close()
        return {"status": "error", "message": str(e)}, 500
    

@app.route('/participations/all', methods=['GET'])
def getScoreParticipant():
    position = request.args.get('playerName', type = str)
    params = (position,)
    conn = sqlite3.connect('bdd_quiz.db')
    cursor = conn.cursor()
    cursor.execute('SELECT score FROM Participant where pseudo = ?', params)
    score = cursor.fetchone()
    print(params, score)
    conn.close()
    if score is None:
        return {"status": "error", "message": "Question not found"}, 404
    else :
        return {"score" : score}


@app.route('/participations', methods=['GET'])
def getClassParticipant():
    conn = sqlite3.connect('bdd_quiz.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT pseudo, score FROM Participant ORDER BY score DESC LIMIT 3""")
    rows = cursor.fetchall()
    print(rows)
    scores = []
    for row in rows:
        score_dict = {"playerName": row[0], "score": row[1]}
        scores.append(score_dict)
    conn.close()
    if len(rows) == 0:
        return {"status": "error", "message": "No participants found"}, 404
    else :
        return {"scores" : scores}

@app.route('/participations/classement', methods=['GET'])
def getParticipantClass():
    try:
        position = request.args.get('playerName', type = str)
        conn = sqlite3.connect('bdd_quiz.db')
        cursor = conn.cursor()
        cursor.execute("select pseudo, score from Participant")
        rows = cursor.fetchall()
        scores = []
        for row in rows:
            score_dict = {"playerName": row[0], "score": row[1]}
            scores.append(score_dict)
        conn.close()
        scores = sorted(scores, key=lambda x: x['score'], reverse=True)
        classe = None  # Initialize classe
        for i in range(len(scores)):
            if scores[i]['playerName'] == position:  # Compare with string, not tuple
                classe = i + 1  # '+1' is for starting rank from 1 instead of 0
                break

        print(classe)
        if classe is not None:  # Check if classe is assigned
            return {"classe": classe}, 200
        else:
            return {"status": "error", "message": "Player not found"}, 404
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

@app.route('/rebuild-db', methods=['POST'])
def RebuildDb():
    status = savebdd.verifyAuthorization(request)[1]
    if status == 200:
        filename = "quiz.db"
        if not os.path.exists(filename):
            open(filename, 'x')
        return savebdd.initDataBase()
    return savebdd.verifyAuthorization(request)
    

if __name__ == '__main__':
    app.run()