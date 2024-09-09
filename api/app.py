from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!!!"})

@app.route('/api/data')
def get_data():
    data = {
        "name": "Flask API",
        "version": "1.0",
        "description": "A simple API built with Flask"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5174)