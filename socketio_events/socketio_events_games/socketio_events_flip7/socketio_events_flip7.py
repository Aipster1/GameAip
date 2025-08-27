from dataclasses import asdict
from flask import request, session
from flask_socketio import emit, join_room
from manager.PlayerManager import playerStorage
from manager.GameManager import gameStorage

from manager.Flip7Manager import flip7_manager

from utils.utils import getGameRoom, getLobbyRoom


def initializeFlip7GameSockets(socketio):

    def serialize_card(card):
    # return just what the client needs to render
        return {"filename": card.filename,
                "value": card.value,
                "type": card.type}

    def serialize_hand(hand):
        return [serialize_card(c) for c in hand]
    
    def serialize_player(player):
        # player.user_id, player.name, player.hand (list[Flip7Card])
        return {
            "userId": str(player.user_id),
            "name": getattr(player, "name", str(player.user_id)),
            "hand": [asdict(c) for c in player.hand],
        }

    def serialize_table(game):
        return {"players": [serialize_player(p) for p in game.players]}


    @socketio.on('initialize_deck')
    def initialize_deck(data):
        gameId = data.get('gameId')

        game = gameStorage.get(gameId)

        flip7_manager.build_deck(game)
        print("deck build successfully")

    
    @socketio.on('deal_card')
    def on_deal_card(data):
        game_id = str(data['gameId'])
        user_id = str(session['user_Id'])  # identify the drawer server-side

        game = gameStorage.get(game_id)
        if not game:
            return {"ok": False, "error": "no_such_game"}

        # mutate state
        flip7_manager.deal_to(playerStorage.get(user_id), game)

        # broadcast only that player's new full hand to everyone
        player = playerStorage.get(user_id)

        emit(
            'hand_replace',
            {"userId": user_id, "hand": [asdict(c) for c in player.hand]},
            room=getGameRoom(game_id)
        )

        # (optional) also keep a "public" event
        emit(
            'player_drew',
            {"userId": user_id, "handCount": len(player.hand)},
            room=getGameRoom(game_id)
        )

        return {"ok": True}


