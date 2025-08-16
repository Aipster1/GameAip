from flask import render_template, url_for
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



# @socketio.on('register')
# def handle_register(data):
#     name = data['username']



# socketevent JoinLobby(id)

# socketevent LeaveLobby(id)

# socketevent UpdateLobbyList()
