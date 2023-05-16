from flask import Flask, request
import hashlib
import jwt
from flask_cors import CORS
from database import create_question_table, save_question_to_database, sqlite3

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

@app.route('/rebuild-db', methods=['POST'])
def BuildDatabase():
    # Code pour reconstruire la base de données
    try:
        # Établir une connexion à la base de données
        conn = sqlite3.connect(DATABASE_PATH)
        
        # Créer une instance de curseur pour exécuter des requêtes SQL
        cursor = conn.cursor()
        
        # Supprimer les tables existantes
        cursor.execute("DROP TABLE IF EXISTS table1")
        cursor.execute("DROP TABLE IF EXISTS table2")
        
        # Créer les nouvelles tables
        cursor.execute("CREATE TABLE table1 (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute("CREATE TABLE table2 (id INTEGER PRIMARY KEY, value INTEGER)")
        
        # Effectuer d'autres opérations de reconstruction de la base de données si nécessaire
        
        # Valider les modifications
        conn.commit()
        
        return "Database rebuilt successfully", 200
        
    except Exception as e:
        return str(e), 500

@app.route('/post-question', methods=['POST'])
def post_question():
    # Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    
    # Récupérer l'objet JSON envoyé dans le corps de la requête
    question_data = request.get_json()
    
    # Récupérer les informations de la question
    position = question_data['position']
    titre = question_data['titre']
    texte = question_data['texte']
    image = question_data['image']
    
    # Enregistrer la question en base de données
    success = save_question_to_database(position, titre, texte, image)
    
    if success:
        return 'Question enregistrée avec succès', 200
    else:
        return 'Erreur lors de l\'enregistrement de la question', 500


if __name__ == '__main__':
    create_question_table()
    app.run()