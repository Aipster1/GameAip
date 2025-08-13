import socket
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

from logic.quizgameManager import loadQuizJSON, quizLogicEvents
from logic.socketEvents import socketLogicEvents

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'aipsterKeyWuh'


questions = loadQuizJSON()
connectedIpAddresses = {}
questionCounter = 1

socketio = SocketIO(app, ping_interval=60, ping_timeout=600)

socketLogicEvents(socketio, connectedIpAddresses)
quizLogicEvents(socketio, questionCounter)

@app.route('/')
def index():
    print("[ROUTE] Aufgerufen: / (index)")
    return render_template('index.html')

@app.route('/lobby')
def lobby():
    print("[ROUTE] Aufgerufen: / (lobby)")
    return render_template('lobby.html')

@app.route('/quizGame')
def game():
    print("[ROUTE] Aufgerufen: /quizGame")
    return render_template('quizGame.html')

@app.route('/keywords')
def keywords():
    print("[ROUTE] Aufgerufen: /keywords")
    return render_template('keywords.html')

@app.route('/lobby/keywordsLobby')
def keywordsLobby():
    print("[ROUTE] Aufgerufen: /lobby/keywordsLobby")
    return render_template('keywordsLobby.html')

@app.route('/lobby/quizGameLobby')
def quizGameLobby():
    print("[ROUTE] Aufgerufen: /lobby/quizGameLobby")
    return render_template('quizGameLobby.html')

@app.route('/lobby/flipSevenLobby')
def flipSevenLobby():
    print("[ROUTE] Aufgerufen: /lobby/flipSevenLobby")
    return render_template('flipSevenLobby.html')


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
