from socketio_events.socketio_events_lobby.socketio_events_lobby import initLobbySocketEvents
from socketio_events.socketio_events_general import socketEventsInit
from socketio_events.socketio_events_games.socketio_events_flip7.socketio_events_flip7 import initializeFlip7GameSockets

#init LobbySockets
def init_socket_events(socketio, connectedIpAddresses):
    initializeFlip7GameSockets(socketio)
    initLobbySocketEvents(socketio)
    socketEventsInit(socketio, connectedIpAddresses)

