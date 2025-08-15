from lobbys.lobbyManager import lobbyStorage

# socketevent CreateLobby(type)
def initLobbySocketEvents(socketio):

    @socketio.on('socketEventCreateLobby')
    def socketEventCreateLobby(data):
        print("cool")
        print("try to create lobby")
        lobbyName = data[0]
        lobbyType = data[1]
        userId = data[2]

        lobbyStorage.create(lobbyName, lobbyType, userId)
        print(lobbyStorage.list_open())



# @socketio.on('register')
# def handle_register(data):
#     name = data['username']



# socketevent JoinLobby(id)

# socketevent LeaveLobby(id)

# socketevent UpdateLobbyList()
