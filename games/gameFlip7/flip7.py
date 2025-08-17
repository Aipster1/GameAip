from flask import Blueprint, abort, redirect, render_template, request, url_for
from .logic.flip7Manager import *
from utils.utils import createMembersDict
from games.gameManager import gameStorage
from lobbys.lobbyManager import lobbyStorage
from flask_socketio import join_room, leave_room, close_room

gameFlip7Bp = Blueprint('gameFlip7Bp', __name__,
                       template_folder='templates',
                        static_folder='static',
                        static_url_path='/gameFlip7')


@gameFlip7Bp.route('/game/flip7/create', methods=['GET', 'POST'])
def flip7CreateGame():
    
    lobby_id = request.form.get('lobbyId')

    if not lobby_id:
        abort(400, description="lobbyId required")

    # Look up authoritative lobby server-side (avoid trusting client data)
    lobby = lobbyStorage.get(lobby_id)  
    if not lobby:
        abort(404, description="Lobby not found")

    game_members_list = createMembersDict(lobby.members)

    game = gameStorage.create(lobbyId=lobby_id, gameType=lobby.lobbyType, members=game_members_list)
    
    game_id = getattr(game, "id", game) 

    print("gameid: ", game_id)

    print(gameStorage.get(game_id))

    # join_room()

    # Redirect after POST (303 is ideal to force GET)
    return redirect(url_for("gameFlip7Bp.flip7Game", id=game_id), code=303)
    


@gameFlip7Bp.route('/game/flip7/<string:id>')
def flip7Game(id):
    print("[ROUTE] Aufgerufen: /game/flip7/<string:id>")

    game = gameStorage.get(id)
    if not game:
        print("no game found")
    else:
        print(game)

    return render_template('flip7Game.html', game=game)

 