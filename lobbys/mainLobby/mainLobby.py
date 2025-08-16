from flask import render_template, Blueprint, session
from lobbys.lobbyManager import lobbyStorage
from socketEvents import currentPlayers

mainLobbyBp = Blueprint('mainLobbyBp', __name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='/mainLobby')
                    


@mainLobbyBp.route('/lobby')
def lobby():
    print("[ROUTE] Aufgerufen: / (lobby)")
    

    print(currentPlayers)

    # todo: username in session["uid"] speichern somit ist playerdata und lobby verknüpft
    session["uid"] = currentPlayers["username"]

    return render_template('lobby.html')
