from flask import Flask, request, jsonify
import hashlib
import jwt
from flask_cors import CORS
import sqlite3
import json
import Question
import jwt_utils as u
from datetime import datetime

def initDataBase():
    try:
        db_connection = sqlite3.connect('./bdd_quiz.db')
        cur = db_connection.cursor()
        cur.execute("begin")
        cur.execute('DROP TABLE IF EXISTS Question')
        cur.execute('DROP TABLE IF EXISTS Participation')
        cur.execute(
            'CREATE TABLE Question (id INTEGER NOT NULL UNIQUE PRIMARY KEY,  title TEXT, text TEXT, image TEXT, position INTEGER, possibleAnswers TEXT)')
        cur.execute(
            'CREATE TABLE Participant (id_particip INTEGER NOT NULL UNIQUE PRIMARY KEY, pseudo TEXT, answers TEXT, score INTEGER, date TEXT)')
        db_connection.commit()
        cur.close()
        db_connection.close()
        return 'Ok', 200
    except Exception as e:
        return f"Internal Server Error\n {e}", 500
    

def verifyAuthorization(request):
    token_bearer = request.headers.get('Authorization')
    if token_bearer == None:
        return 'Authorization not set.', 401
    try:
        u.decode_token(token_bearer.replace('Bearer ', ''))
        return 'Ok', 200
    except u.JwtError as err:
        return str(err), 401
    except Exception as e:
        return f"Internal Server Error\n {e}", 500