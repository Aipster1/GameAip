from flask import request, session
from flask_socketio import emit
from datetime import datetime

def socketLogicEvents(socketio, connectedIpAddresses, currentPlayer):
    @socketio.on('connect')
    def handle_connect():
        session.permanent = True
        ip_address = request.remote_addr
        user_agent = request.headers.get('User-Agent')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if ip_address not in connectedIpAddresses:
            connectedIpAddresses[ip_address] = {
                'ip': ip_address,
                'user_agent': user_agent
            }
            print(f"[{timestamp}] Neue Verbindung: {ip_address}")
        else:
            print(f"[{timestamp}] Bekannte IP verbunden: {ip_address}")

        print("→ Aktuell verbundene IPs:")
        for ip, info in connectedIpAddresses.items():
            print(f"   - IP        : {info['ip']}")
            print(f"     UserAgent : {info['user_agent']}")
        print("")

    @socketio.on('register')
    def handle_register(data):
        name = data['username']
        lowerCaseName = name.lower()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ip_address = request.remote_addr

        if lowerCaseName in currentPlayer and currentPlayer[lowerCaseName]["status"] == "disconnected":
            currentPlayer[lowerCaseName]["status"] = "connected"
            print(f"[{timestamp}] Spieler RECONNECTED: {name} (IP: {ip_address})")
            emit('player_list', list(currentPlayer.values()), broadcast=True)
            return

        playerData = {
            'username': name,
            'ip': ip_address,
            'Score': 0,
            'status': "connected"
        }

        currentPlayer[lowerCaseName] = playerData
        print(f"[{timestamp}] Neuer Spieler registriert: {name} (IP: {ip_address})")

        emit('updateScore', list(currentPlayer.values()), broadcast=True)

    @socketio.on('disconnect')
    def handleDisconnect():
        ipAddress = request.remote_addr
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        disconnectedUser = None

        for player in currentPlayer.values():
            if player['ip'] == ipAddress:
                player['status'] = "disconnected"
                disconnectedUser = player['username']
                break

        if disconnectedUser:
            print(f"[{timestamp}] Spieler getrennt: {disconnectedUser} (IP: {ipAddress})")
        else:
            print(f"[{timestamp}] Verbindung getrennt (unregistrierte IP): {ipAddress}")
