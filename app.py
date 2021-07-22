from flask import Flask, request
#from chatterbot import ChatBot
#import os 
#import gc



app = Flask(__name__)
#chatbot = ChatBot("ChineseChatBot",
#    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
#    database_uri='mongodb+srv://admin:1111@cluster0.nwewq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')


@app.route('/<faq>')
def hello(faq):
    gc.collect()
    return faq


if __name__ == 'main':
    app.run() 