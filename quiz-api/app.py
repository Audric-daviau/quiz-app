from flask import Flask
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return {"size": 0, "scores": []}, 200


# Chemin vers le fichier de base de données SQLite
DATABASE_PATH = 'path/to/your/database.db'

# pensez à ajouter un scénarion postman pour ajouter nos questions
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


if __name__ == '__main__':
    app.run()
