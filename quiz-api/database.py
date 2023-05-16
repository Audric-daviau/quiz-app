import sqlite3

DATABASE_PATH = "bdd_quiz.db"

def create_question_table():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            position INTEGER,
            title TEXT,
            text TEXT,
            image TEXT
        )
    ''')

    conn.commit()
    conn.close()

def save_question_to_database(position, titre, texte, image):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO questions (position, titre, texte, image)
            VALUES (?, ?, ?, ?)''', (position, titre, texte, image))
        conn.commit()
        return True
    except Exception as e:
        print(str(e))
        return False