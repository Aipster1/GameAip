import socket
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

from logic.quizgameManager import loadQuizJSON, quizLogicEvents
from logic.socketEvents import socketLogicEvents

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'aipsterKeyWuh'

currentPlayer = {}
questions = loadQuizJSON()
connectedIpAddresses = {}
questionCounter = 1

socketio = SocketIO(app, ping_interval=60, ping_timeout=600)

socketLogicEvents(socketio, connectedIpAddresses, currentPlayer)
quizLogicEvents(socketio, currentPlayer, questionCounter)


@app.route('/')
def index():
    print("[ROUTE] Aufgerufen: / (index)")
    return render_template('index.html')


@app.route('/quizGame')
def game():
    print("[ROUTE] Aufgerufen: /quizGame")
    return render_template('quizGame.html')

@app.route('/keywords')
def keywords():
    print("[ROUTE] Aufgerufen: /keywords")
    return render_template('keywords.html')

@app.route('/flip7')
def keywords():
    print("[ROUTE] Aufgerufen: /flip7")
    return render_template('flip7.html')

def getLocalIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        return s.getsockname()[0]
    finally:
        s.close()


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    localIp = getLocalIp()

    print("========== SERVER-INFO ==========")
    print("Flask-QuizGame Server gestartet")
    print(f"Lokale Adresse:    http://localhost:{port}")
    print(f"Netzwerk-Adresse:  http://{localIp}:{port}")
    print(f"Fragen geladen:    {len(questions['quiz'])}")
    print("=================================\n")

    socketio.run(app, host=host, port=port, debug=True)
