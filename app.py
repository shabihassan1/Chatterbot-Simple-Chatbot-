from flask import Flask, request, render_template
from chatterbot import ChatBot

app = Flask(__name__)

# Load the pre-trained chatbot from the saved database
chatbot = ChatBot('ClassDemoBot', storage_adapter='chatterbot.storage.SQLStorageAdapter', database='db.sqlite3')

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle chatbot interaction
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = chatbot.get_response(user_input)
    if response.confidence < 0.1:
        bot_response = "I'm not sure how to respond to that. Can you ask something related to customer support, security, or brand growth?"
    else:
        bot_response = str(response)
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)