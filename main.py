
from datetime import timedelta
from flask import Flask
from flask_socketio import SocketIO
import socket

# local imports
from routes.routes_main import main
from routes.routes_lobby import lobby
from routes.routes_flip7 import flip7

from socketio_events.init import init_socket_events
# from socketEvents import socketEventsInit, currentPlayers


app = Flask(__name__, static_url_path='/static')

app.secret_key = b'aipsterKeyWuh'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)


socketio = SocketIO(app, ping_interval=60, ping_timeout=600)


app.register_blueprint(main, url_prefix='/')
app.register_blueprint(lobby, url_prefix='/')
app.register_blueprint(flip7, url_prefix='/')


connectedIpAddresses = {}


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
    init_socket_events(socketio, connectedIpAddresses)

    socketio.run(app, host=host, port=port, debug=True)
