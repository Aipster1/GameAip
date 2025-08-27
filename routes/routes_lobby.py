from flask import redirect, render_template, Blueprint, request, session, url_for
from manager.LobbyManager import lobbyStorage


lobby = Blueprint('lobby', __name__,
                        template_folder='../templates/lobbys',
                        static_folder='static')
                    

# --- Main lobby route ---
@lobby.route('/lobby')
def main_lobby():
    print("[ROUTE] Aufgerufen: / (lobby)")
    print("user_Id: ", session["user_Id"])
    if 'user_Id' not in session:
        # not registered so return to /register
        return redirect(url_for('main.register'))

    return render_template('main_lobby.html')


# --- Flip7 lobby routes ---
@lobby.route('/lobby/flip7')
def flip7_main_lobby():
    print("[ROUTE] Aufgerufen: /lobby/flip7")

    # shows all existing lobbys
    openFlip7Lobbies = lobbyStorage.listOpen()

    return render_template('flip7_main_lobby.html', openFlip7Lobbies = openFlip7Lobbies)


@lobby.route('/lobby/flip7/create', methods=['GET', 'POST'])
def flip7_create_lobby():
    print("[ROUTE] Aufgerufen: /lobby/flip7/create")
    
    if request.method == 'POST':
        name = (request.form.get('name') or 'Neue Lobby').strip()
        
        lobby = lobbyStorage.create(name=name, lobbyType='flip7', hostId=session["user_Id"])

        return redirect(url_for('lobby.flip7_game_lobby', id=lobby.id))
    
    return render_template('flip7_create_lobby.html')


@lobby.route('/lobby/flip7/<string:id>', methods=['GET', 'POST'])
def flip7_game_lobby(id):
    print("[ROUTE] Aufgerufen: /lobby/flip7/id")

    flip7Lobby = lobbyStorage.get(id)

    print("lobbyId:", flip7Lobby.id)
    
    return render_template('flip7_game_lobby.html', flip7LobbyId=id, lobby=flip7Lobby, session = session)
