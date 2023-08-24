from flask import Flask, request, jsonify

app = Flask(__name__)

conversation_history = []

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data['message']

        # Append the user message to the conversation history
        conversation_history.append({"role": "user", "content": user_message})

        # Generate a response using the conversation history
        # In a real application, you would replace this with your AI model
        # For demonstration purposes, let's echo the user's message
        bot_response = user_message

        # Append the bot response to the conversation history
        conversation_history.append({"role": "bot", "content": bot_response})

        return jsonify({"response": bot_response})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
