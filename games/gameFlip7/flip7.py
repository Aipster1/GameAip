from flask import Blueprint, render_template, request, session
from .logic.flip7Manager import *
from lobbys.lobbyManager import Lobby
from dataclasses import dataclass, field
from utils.utils import createMembersDict, createGameId

gameFlip7Bp = Blueprint('gameFlip7Bp', __name__,
                       template_folder='templates',
                        static_folder='static',
                        static_url_path='/gameFlip7')


@dataclass
class Flip7Game:
    id: str
    lobbyId: str
    gameType: str
    members: dict = field(default_factory=dict)


@gameFlip7Bp.route('/game/flip7/create', methods=['GET'])
def flip7CreateGame():
    print("[ROUTE] Aufgerufen: /game/flip7/<string:id>")

    gameId = createGameId("flip7")

    lobbyId = request.args.get('lobbyId')
    gameType = request.args.get('gameType')
    membersList = request.args.getlist('membersList')

    gameMembersList = createMembersDict(membersList)


    game = Flip7Game(id=gameId, lobbyId = lobbyId, gameType = gameType, members = gameMembersList)

    print(game)
    
    return render_template('flip7Game.html')


@gameFlip7Bp.route('/game/flip7/<string:id>')
def flip7Game(id):
    print("[ROUTE] Aufgerufen: /game/flip7/<string:id>")



    # deck = build_deck()
    
    # shuffle_deck(deck)

    # hand = draw_card(6, deck)

    # player_cards = hand

    # print(get_deck_card_count(deck))

    return render_template('flip7Game.html')