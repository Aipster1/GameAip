from secrets import token_hex
from flask import render_template, session, Blueprint
from lobbys.lobbyManager import lobbyStorage

mainLobbyBp = Blueprint('mainLobbyBp', __name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='/mainLobby')
                       

def current_user_id():
    if 'uid' not in session:
        session['uid'] = f"user_{token_hex(4)}"
    return session['uid']


@mainLobbyBp.route('/lobby')
def lobby():
    print("[ROUTE] Aufgerufen: / (lobby)")
   

    return render_template('lobby.html')
