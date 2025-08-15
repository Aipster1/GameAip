from lobbys.lobbyManager import lobbyStorage
from utils.utils import current_user_id

# socketevent CreateLobby(type)
def initLobbySocketEvents(socketio):

    @socketio.on('socketEventCreateLobby')
    def socketEventCreateLobby(data):
        print("creating lobby...")
        lobbyName = data[0]
        lobbyType = data[1]
        userId = current_user_id()

        lobbyStorage.create(lobbyName, lobbyType, userId)
        print(lobbyStorage.list_open())
        print("Lobby created!")



# @socketio.on('register')
# def handle_register(data):
#     name = data['username']



# socketevent JoinLobby(id)

# socketevent LeaveLobby(id)

# socketevent UpdateLobbyList()
