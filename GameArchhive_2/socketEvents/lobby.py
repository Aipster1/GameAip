from flask import redirect, render_template, request, session, url_for
from flask_socketio import emit, join_room, rooms
import socketio
from lobbys.lobbyManager import lobbyStorage
from games.gameManager import gameStorage
from games.members.membersManager import playerStorage
from utils.utils import currentUserId, getGameRoom, getLobbyRoom
from games.gameFlip7.flip7 import *

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
    
        
        lobby.members.append(username)

        print(f"{username} ist der lobby mit der lobbyId: {lobbyId} beigetreten")

        emit('redirect', {
        'url': url_for('flip7LobbyBp.flip7GameLobby', id=lobbyId)
    })
        

    #todo: make the join_room generic
    @socketio.on('join_room')
    def on_join_lobby(data):

        lobbyId = data.get('lobbyId')
    
        join_room(getLobbyRoom(lobbyId))
        print(f"user:{session["uid"]} und sid:{request.sid} ist dem raum beigetreten!")

    
    @socketio.on('join_game_room')
    def on_join_lobby(data):

        gameId = data.get('gameId')
    
        join_room(getGameRoom(gameId))

        playerStorage.create_flip7_player(uid=session["uid"], sid=request.sid, ip=request.remote_addr, hand=[],status="", roundScore=0, totalScore=0)

        print("player erstellt:", playerStorage.get(session["uid"]))

        print("sind dem game beigetreten")


    
    @socketio.on('start_game')
    def on_game_start(data):
        lobbyId = data.get('lobbyId')
        
        print("Das ist die lobbyId dazu: ", lobbyId)

        lobby = lobbyStorage.get(lobbyId)

        game = gameStorage.create(lobbyId=lobbyId, gameType=lobby.lobbyType, players=lobby.members)

        emit('redirect', {'url': url_for('gameFlip7Bp.flip7Game', id=game.id)}, room=getLobbyRoom(lobbyId))


        



       
