from flask import render_template, request, session, Blueprint


flip7LobbyBp = Blueprint('flip7LobbyBp', __name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='/flip7Lobby')


@flip7LobbyBp.route('/lobby/flip7')
def flip7Lobby():
    print("[ROUTE] Aufgerufen: /lobby/flip7")

    return render_template('flip7Lobby.html')

