from flask import redirect, render_template, Blueprint, request, url_for
from lobbys.lobbyManager import lobbyStorage
from utils.utils import currentUserId


flip7LobbyBp = Blueprint('flip7LobbyBp', __name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='/flip7Lobby')


@flip7LobbyBp.route('/lobby/flip7')
def flip7MainLobby():
    print("[ROUTE] Aufgerufen: /lobby/flip7")

    # shows all existing lobbys
    openFlip7Lobbies = lobbyStorage.listOpen()

    return render_template('flip7MainLobby.html', openFlip7Lobbies = openFlip7Lobbies)




@flip7LobbyBp.route('/lobby/flip7/create', methods=['GET', 'POST'])
def flip7CreateLobby():
    print("[ROUTE] Aufgerufen: /lobby/flip7/create")
    
    if request.method == 'POST':
        name = (request.form.get('name') or 'Neue Lobby').strip()
        
        # todo: currentUserId() generates a random id if you create a lobby and are not registered before
        
        lobby = lobbyStorage.create(name=name, lobbyType='flip7', hostId=currentUserId())
        return redirect(url_for('flip7LobbyBp.flip7GameLobby', id=lobby.id))
    
    return render_template('flip7CreateLobby.html')



@flip7LobbyBp.route('/lobby/flip7/<string:id>', methods=['GET', 'POST'])
def flip7GameLobby(id):
    print("[ROUTE] Aufgerufen: /lobby/flip7/id")

    flip7Lobby = lobbyStorage.get(id)

    print(flip7Lobby)

    return render_template('flip7GameLobby.html', flip7Lobby=flip7Lobby)

