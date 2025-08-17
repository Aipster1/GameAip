
from datetime import timedelta
from flask import Flask, flash, redirect, render_template, session, url_for
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, request
from flask_socketio import SocketIO
import socket

# local imports
from lobbys.mainLobby.mainLobby import mainLobbyBp
from lobbys.flip7Lobby.flip7Lobby import flip7LobbyBp
from games.gameFlip7.flip7 import gameFlip7Bp

from socketEvents import socketEventsInit, currentPlayers


app = Flask(__name__, static_url_path='/static')

app.secret_key = b'aipsterKeyWuh'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)


socketio = SocketIO(app, ping_interval=60, ping_timeout=600)


app.register_blueprint(mainLobbyBp, url_prefix='/')
app.register_blueprint(flip7LobbyBp, url_prefix='/')
app.register_blueprint(gameFlip7Bp, url_prefix='/')



connectedIpAddresses = {}



@app.route('/')
def index():
    session.clear()
    print("[ROUTE] Aufgerufen: / (index)")
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    print("[ROUTE] Aufgerufen: / (register)")
    

    if request.method == 'POST':
        username = (request.form.get('name') or '').strip()
        if any(u.lower() == username.lower() for u in currentPlayers):
            flash('Username already taken. Please choose another.', 'error')
            # Either re-render the form:
            return render_template('register.html', username=username), 409
        
        # todo: check if user is already registered so you can not register 2 times with different usernames

        session["uid"] = username

        lowerCaseName = username.lower()
        ipAddress = request.remote_addr

        if lowerCaseName in currentPlayers and currentPlayers[lowerCaseName]["status"] == "disconnected":
            currentPlayers[lowerCaseName]["status"] = "connected"
            print(f"Spieler RECONNECTED: {username} (IP: {ipAddress})")
            return

        playerData = {
            'username': username,
            'sid': "",
            'ip': ipAddress,
            'status': "connected"
        }

        currentPlayers[lowerCaseName] = playerData

        print(currentPlayers)

        return redirect(url_for('mainLobbyBp.lobby',))
    
    return render_template('register.html')


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
    print("=================================\n")

    # Init for all socketEvents
    socketEventsInit(socketio, connectedIpAddresses)

    socketio.run(app, host=host, port=port, debug=True)
