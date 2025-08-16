
from flask import Flask, render_template, session
from flask_socketio import SocketIO
import socket
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

# local imports
from lobbys.mainLobby.mainLobby import mainLobbyBp
from lobbys.flip7Lobby.flip7Lobby import flip7LobbyBp
from games.gameFlip7.flip7 import gameFlip7Bp

from socketEvents import socketEventsInit

from datetime import timedelta

from utils.utils import currentUserId

# from GameAip.socketEvents import socketEventsInit

app = Flask(__name__, static_url_path='/static')

app.secret_key = b'aipsterKeyWuh'
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)


socketio = SocketIO(app, ping_interval=60, ping_timeout=600)


app.register_blueprint(mainLobbyBp, url_prefix='/')
app.register_blueprint(flip7LobbyBp, url_prefix='/')
app.register_blueprint(gameFlip7Bp, url_prefix='/')

connectedIpAddresses = {}

@app.route('/')
def index():
    session.clear()
    # currentUserId()
    
    print("[ROUTE] Aufgerufen: / (index)")
    return render_template('index.html')


@app.route('/register')
def register():
    print("[ROUTE] Aufgerufen: / (register)")
    
    return render_template('register.html')


# Init for all socketEvents
socketEventsInit(socketio, connectedIpAddresses)

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

    socketio.run(app, host=host, port=port, debug=True)
