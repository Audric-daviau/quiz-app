from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app = Flask(__name__)
CORS(app)
@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

if __name__ == "__main__":
    app.run()