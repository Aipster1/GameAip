from flask import render_template, Blueprint
from lobbys.lobbyManager import lobbyStorage


flip7LobbyBp = Blueprint('flip7LobbyBp', __name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='/flip7Lobby')


@flip7LobbyBp.route('/lobby/flip7')
def flip7MainLobby():
    print("[ROUTE] Aufgerufen: /lobby/flip7")

    # shows all existing lobbys
    open_lobbies = lobbyStorage.list_open()

    return render_template('flip7MainLobby.html', open_lobbies = open_lobbies)



@flip7LobbyBp.route('/lobby/flip7/create')
def flip7CreateLobby():
    print("[ROUTE] Aufgerufen: /lobby/flip7/create")

    

    return render_template('flip7CreateLobby.html')


@flip7LobbyBp.route('/lobby/flip7/<int:id>', methods=['GET', 'POST'])
def flip7GameLobby(id):
    print("[ROUTE] Aufgerufen: /lobby/flip7")

    # shows all existing lobbys

    return render_template('flip7GameLobby.html')

