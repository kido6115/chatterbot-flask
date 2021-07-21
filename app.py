from flask import Flask, request
from chatterbot import ChatBot

app = Flask(__name__)
chatbot = ChatBot("ChineseChatBot")


@app.route('/<faq>')
def hello(faq):
    return chatbot.get_response(faq).text


if __name__ == 'main':
    app.run() 