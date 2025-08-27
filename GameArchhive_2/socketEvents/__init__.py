from flask import request, session
from .lobby import initLobbySocketEvents
# from socketEvents.flip7 import flip7Init

currentPlayers = {}

def socketEventsInit(socketio, connectedIpAddresses):
    
    @socketio.on('connect')
    def handleConnect():
        session.permanent = True
        ipAddress = request.remote_addr
        
        if ipAddress not in connectedIpAddresses:
            connectedIpAddresses[ipAddress] = {
                'ip': ipAddress,
            }
    
        print("→ Aktuell verbundene IPs:")
        for ip, info in connectedIpAddresses.items():
            print(f"   - IP        : {info['ip']}")
        print("")
    

    # @socketio.on('register')
    # def handleRegister(data):

    #     name = data['username']
    #     lowerCaseName = name.lower()
    #     ipAddress = request.remote_addr

    #     if lowerCaseName in currentPlayers and currentPlayers[lowerCaseName]["status"] == "disconnected":
    #         currentPlayers[lowerCaseName]["status"] = "connected"
    #         print(f"Spieler RECONNECTED: {name} (IP: {ipAddress})")
    #         return

    #     playerData = {
    #         'username': name,
    #         'ip': ipAddress,
    #         'status': "connected"
    #     }

    #     currentPlayers[lowerCaseName] = playerData

    #     print(f"Neuer Spieler registriert: {name} (IP: {ipAddress})")


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

    #init LobbySockets
    initLobbySocketEvents(socketio)