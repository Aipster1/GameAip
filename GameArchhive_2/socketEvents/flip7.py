from flask import redirect, render_template, request, session, url_for
from flask_socketio import emit, join_room, rooms
from lobbys.lobbyManager import lobbyStorage
from games.gameManager import gameStorage
from games.members.membersManager import playerStorage
from utils.utils import currentUserId, getGameRoom, getLobbyRoom
from games.gameFlip7.flip7 import *

def initializeFlip7GameSockets(socketio):
    @socketio.on('initialize_deck')
    def initialize_deck(data):
        gameId = data.get('gameId')

        game = gameStorage.get(gameId)

        game.deck = buildDeck(game.deck)

        shuffleDeck(game.deck)


        

    

    @socketio.on('draw_card')
    def on_game_start(data):
        gameId = data.get('gameId')
        uid = data.get('uid')

        cardCount = data.get('cardCount')

        game = gameStorage.get(gameId)

        player = playerStorage.get(uid)

        cards = drawCard(cardCount, game.deck)

        player.hand.append(cards)

        print("player hand:", player.hand)


        #todo: fix the member logic, lobbys are not fixed to have the member class objects as memebers if that is necessary
        # for player in game.players:
        #     print(player, " hand:", player.hand)


# current player draw card


# selected player draw 3 cards


# 