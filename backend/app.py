from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) # Allows the frontend to talk to this backend securely

# This URL points to the Ollama container we will create later
OLLAMA_URL = "http://aiva-ollama:11434/api/chat"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK", "app": "Aiva AI Backend", "model": "tinyllama"})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    try:
        # Forward the user's message to the local Ollama container
        response = requests.post(OLLAMA_URL, json={
            "model": "tinyllama",
            "messages": data.get("messages", []),
            "stream": False
        }, timeout=90) # 90s timeout gives the model time to "warm up"
        
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": "Ollama is not reachable. Is the model running?", "details": str(e)}), 502

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
