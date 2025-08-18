from flask import redirect, render_template, request, session, url_for
from flask_socketio import emit, join_room, rooms
from lobbys.lobbyManager import lobbyStorage
from games.gameManager import gameStorage
from utils.utils import currentUserId, getGameRoom, getLobbyRoom
from games.gameFlip7.flip7 import *

def initializeFlip7GameSockets(socketio):
    @socketio.on('initialize_deck')
    def initialize_deck():

        pass



# current player draw card


# selected player draw 3 cards


# 