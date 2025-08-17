from flask import redirect, render_template, Blueprint, session, url_for
from lobbys.lobbyManager import lobbyStorage
from socketEvents import currentPlayers

mainLobbyBp = Blueprint('mainLobbyBp', __name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='/mainLobby')
                    


@mainLobbyBp.route('/lobby')
def lobby():
    print("[ROUTE] Aufgerufen: / (lobby)")
    
    if 'uid' not in session:
        # not registered so return to /register
        return redirect(url_for('register'))
    

    print(currentPlayers)
    print("session uid:", session["uid"])
    # todo: username in session["uid"] speichern somit ist playerdata und lobby verknüpft
    # session["uid"] = currentPlayers["username"]

    return render_template('lobby.html')
