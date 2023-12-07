from flask import Flask, render_template, request, jsonify
import random
import json
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    bot_response = generate_bot_response(user_message)
    return jsonify({'message': bot_response})

def generate_bot_response(user_message):
    # Load intents from JSON file
    with open('responses.json', 'r') as file:
        data = json.load(file)
        intents = data['intents']

    # Search for a matching intent
    for intent in intents:
        for pattern in intent['patterns']:
            if re.search(pattern, user_message, re.IGNORECASE):
                return random.choice(intent['responses'])

    # If no match, provide a default response
    return "I'm sorry, I didn't understand that."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
