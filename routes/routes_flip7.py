from flask import Blueprint, render_template, session

from manager.GameManager import gameStorage

flip7 = Blueprint('flip7', __name__,
                       template_folder='../templates/flip7',
                        static_folder='static')


@flip7.route('/game/flip7/<string:id>')
def flip7Game(id):
    print("[ROUTE] Aufgerufen: /game/flip7/<string:id>")

    flip7Game = gameStorage.get(id)

    if not flip7Game:
        print("no game found")
    else:
        print("wir sind im game", flip7Game)
        
    return render_template('index_flip7.html', flip7Game=flip7Game, flip7GameId=id, session=session)
