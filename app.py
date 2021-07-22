from flask import Flask, request
from chatterbot import ChatBot
import os

app = Flask(__name__)
chatbot = ChatBot("ChineseChatBot",
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb+srv://admin:1111@cluster0.nwewq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')


@app.route('/<faq>')
def hello(faq):
    return chatbot.get_response(faq).text


if __name__ == 'main':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)