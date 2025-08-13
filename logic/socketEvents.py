from flask import request, session

def socketLogicEvents(socketio, connectedIpAddresses):
    currentPlayers = {}

    @socketio.on('connect')
    def handle_connect():
        session.permanent = True
        ip_address = request.remote_addr
        
        if ip_address not in connectedIpAddresses:
            connectedIpAddresses[ip_address] = {
                'ip': ip_address,
            }
    
        print("→ Aktuell verbundene IPs:")
        for ip, info in connectedIpAddresses.items():
            print(f"   - IP        : {info['ip']}")
        print("")


    @socketio.on('register')
    def handle_register(data):
        name = data['username']
        lowerCaseName = name.lower()
        ip_address = request.remote_addr

        if lowerCaseName in currentPlayers and currentPlayers[lowerCaseName]["status"] == "disconnected":
            currentPlayers[lowerCaseName]["status"] = "connected"
            print(f"Spieler RECONNECTED: {name} (IP: {ip_address})")
            return

        playerData = {
            'username': name,
            'ip': ip_address,
            'status': "connected"
        }

        currentPlayers[lowerCaseName] = playerData
        print(f"Neuer Spieler registriert: {name} (IP: {ip_address})")


    @socketio.on('disconnect')
    def handleDisconnect():
        ipAddress = request.remote_addr
        disconnectedUser = None

        for player in currentPlayers.values():
            if player['ip'] == ipAddress:
                player['status'] = "disconnected"
                disconnectedUser = player['username']
                break

        if disconnectedUser:
            print(f"Spieler getrennt: {disconnectedUser} (IP: {ipAddress})")
        else:
            print(f"Verbindung getrennt (unregistrierte IP): {ipAddress}")
