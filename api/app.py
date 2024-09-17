# from urllib import request
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests  # Import requests to make HTTP requests to Ollama
import json

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API with Ollama and Llama 3.1!"})

@app.route('/api/data')
def get_data():
    data = {
        "name": "Flask API",
        "version": "2.0",
        "description": "A Flask API integrated with Ollama's Llama 3.1 model"
    }
    return jsonify(data)

# POST method to accept a prompt
# @app.route('/api/data/<prompt>')
# def get_prompt(prompt):
#     data = {
#         "prompt": prompt
#     }
#     return jsonify(data)

# New route to generate text using Llama 3.1 via Ollama
@app.route('/api/generate', methods=['POST'])
def generate():
    # Get the JSON data from the POST request
    data = request.get_json()
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    # Define the Ollama API endpoint
    ollama_url = 'http://localhost:11434/api/generate'

    # Prepare the payload for Ollama
    payload = {
        'model': 'llama3.1',
        'prompt': prompt
    }

    try:
        # Send a POST request to Ollama with streaming enabled
        with requests.post(ollama_url, json=payload, stream=True) as resp:
            resp.raise_for_status()
            generated_text = ''
            for line in resp.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    # Handle the possibility of partial JSON or plain text
                    try:
                        data = json.loads(decoded_line)
                        generated_text += data.get('response', '')
                    except json.JSONDecodeError:
                        # If not valid JSON, append the raw text
                        generated_text += decoded_line

        # Return the generated text as JSON
        return jsonify({'response': generated_text})

    except requests.exceptions.RequestException as e:
        # Handle exceptions (e.g., connection errors)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Start the Flask app on port 5174
    app.run(host='0.0.0.0', port=5174)