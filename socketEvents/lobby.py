from flask import redirect, render_template, request, session, url_for
from flask_socketio import emit, join_room
import socketio
from lobbys.lobbyManager import lobbyStorage
from utils.utils import currentUserId

# socketevent CreateLobby(type)
def initLobbySocketEvents(socketio):

    @socketio.on('socketEventCreateLobby')
    def socketEventCreateLobby(data):
        print("creating lobby...")
        lobbyName = data[0]
        lobbyType = data[1]
        userId = currentUserId()

        lobbyStorage.create(lobbyName, lobbyType, userId)
        
        # todo:
        # method for getting the lobby where this userId is the hostid
        # and redirect to the lobby with this id
        
        print(lobbyStorage.listOpen())
        print("Lobby created!")


    @socketio.on('join_lobby')
    def on_join_lobby(data):
        
        lobbyId = data.get('lobbyId')
        username = session["uid"]

        lobby = lobbyStorage.get(lobbyId)

        if not lobbyId or not lobbyStorage.get(lobbyId):
            # If the client used an ack callback, send False/err
            return emit('error', {'message': 'Lobby not found'})

        # if username in lobby.members:
        #     join_room(_lobby_room(lobby_id))
        #     print(lobby.members)
        #     emit('redirect', { 'url': url_for('flip7LobbyBp.flip7GameLobby', id=lobby_id) })
        #     return

        if len(lobby.members) >= lobby.maxMemberCount:
            return emit('error', {'message': 'Lobby full'})
        
        join_room(_lobby_room(lobbyId))
        
        lobby.members.append(username)

        print(f"{username} ist der lobby mit der lobbyId: {lobbyId} beigetreten")

        emit('redirect', {
        'url': url_for('flip7LobbyBp.flip7GameLobby', id=lobbyId)
    })
    


    def _lobby_room(lobbyId): return f"lobby:{lobbyId}"
        



# socketevent LeaveLobby(id)

# socketevent UpdateLobbyList()
