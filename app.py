import socket
import json

from flask import Flask, session, request, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'aipsterKeyWuh'

questions = 'static/data/json/questions.json'
with open(questions, 'r', encoding='utf-8') as f:
    quizQuestions = json.load(f)

questionCounter = 1

connectedIpAddresses = {}
currentPlayer = {}

socketio = SocketIO(app, ping_interval=60, pingTimeout= 600)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quizGame')
def game():
    #emit(setfirstQuestion)
    return render_template('quizGame.html')

@app.route('/dummyPage')
def dummy():
    return render_template('dummyPage.html')

@socketio.on('connect')
def handle_connect():
    session.permanent = True
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    if ip_address not in connectedIpAddresses:
        connectedIpAddresses[ip_address] = {
            'ip': ip_address,
            'user_agent': user_agent
        }
        print("Neue IP-Adresse erstellt:", ip_address)
    else:
        print("Vorhandene IP-Adresse gefunden:", ip_address)

    print("")
    print("Aktuell verbundene Clients:")
    for ip, info in connectedIpAddresses.items():
        print(f"      IP       : {info['ip']}")
        print(f"      UserAgent: {info['user_agent']}")
        print("")

@socketio.on('register')
def handle_register(data):
    name = data['username']
    lowerCaseName = name.lower()

    if lowerCaseName in currentPlayer and currentPlayer[lowerCaseName]["status"] == "disconnected":
        print(f"Nutzer '{name}' existiert bereits.")

        currentPlayer[lowerCaseName]["status"] = "connected"

        emit('player_list', list(currentPlayer.values()), broadcast=True)
        return

    #TODO: Hinweis "Spieler ist bereits vorhanden" "Bruder dein Name war X"

    playerData = {
        'username': name,
        'ip': request.remote_addr,
        'Score': 0,
        'status': "connected"
    }

    currentPlayer[name.lower()] = playerData

    print(f"\nNeuer Spieler registriert:")
    print(f"  Name : {name}")
    print(f"  IP   : {request.remote_addr}")
    print(f"\nAktuelle Spieler im currentPlayer:")
    for username, pdata in currentPlayer.items():
        print(f"  - {username}: IP={pdata['ip']}, Score={pdata['Score']}")
    print("")

    emit('updateScore', list(currentPlayer.values()), broadcast=True)

"""
@socketio.on('updateQuestion')
def updateQuestion(data=None):
    allAnswersGiven = all(player.get('gaveAnswer', False) for player in currentPlayer.values())
    print(f"allAnswersGiven ist:  {allAnswersGiven}")

    if allAnswersGiven:
        emit('changeQuestion', broadcast=True)
        global questionCounter
        questionCounter += 1
"""

@socketio.on('answer')
def handle_answer(data):

    answer = data['answer']
    name = data['username']
    print(f"Name ist {name}")
    print(f"Answer ist {answer}")
    global questionCounter

    for item in quizQuestions["quiz"]:
        if item["id"] == questionCounter:
            currentQuestion = item['frage']
            correctAnswer = item['antwort']
            print(f"Answer ist {currentQuestion}")
            print(f"Answer ist {correctAnswer}")

    lowerCaseName = data.get('username').lower()
    if not lowerCaseName or lowerCaseName not in currentPlayer:
        print(f"Antwort erhalten, aber Spieler '{name}' nicht bekannt.")
        return

    if answer.lower() == correctAnswer.lower():
        currentPlayer[lowerCaseName]['Score'] += 1
        print(f"Punkt für {name}! Neuer Punktestand: {currentPlayer[lowerCaseName]['Score']}")
        for player in currentPlayer.values():
            if player['ip'] == request.remote_addr:
                player['gaveAnswer'] = True
    else:
        print(f"Falsche Antwort von {name}: '{answer}'")

    print("\nAktueller Punktestand aller Spieler:")
    for pname, pdata in currentPlayer.items():
        print(f"  - {pname}: {pdata['Score']} Punkte")
    print("")

    allAnswersGiven = all(player.get('gaveAnswer', False) for player in currentPlayer.values())
    print(f"allAnswersGiven ist:  {allAnswersGiven}")
    if allAnswersGiven:
        questionCounter += 1
        data = {
            "players": list(currentPlayer.values()),
            "questionCounter": questionCounter,
        }

        for key, value in data.items():
            print(f"{key}: {value}")

        emit('updateScore', data, broadcast=True)


@socketio.on('disconnect')
def handle_disconnect():
    for player in currentPlayer.values():
        if player['ip'] == request.remote_addr:
            player['status'] = "disconnected"

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        return s.getsockname()[0]
    finally:
        s.close()


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    local_ip = get_local_ip()

    print(f"Server läuft unter:")
    print(f"  http://localhost:{port}")
    print(f"  http://{local_ip}:{port} (im lokalen Netzwerk)")

    socketio.run(app, host=host, port=port)

