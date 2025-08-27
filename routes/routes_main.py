from flask import flash, redirect, render_template, session, url_for, Blueprint
from flask import render_template, request

from manager.PlayerManager import currentPlayers

main = Blueprint('main', __name__,
                       template_folder='../templates/main',
                       static_folder='/static')

@main.route('/')
def index():
    session.clear()
    print("[ROUTE] Aufgerufen: / (index)")

    return render_template('index.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    print("[ROUTE] Aufgerufen: / (register)")
    

    if request.method == 'POST':
        username = (request.form.get('name') or '').strip()

        if any(u.lower() == username.lower() for u in currentPlayers):
            flash('Username already taken. Please choose another.', 'error')
            # Either re-render the form:
            return render_template('register.html', username=username), 409
        
        # todo: check if user is already registered so you can not register 2 times with different usernames

        session["user_Id"] = username

        lowerCaseName = username.lower()
        ipAddress = request.remote_addr

        if lowerCaseName in currentPlayers and currentPlayers[lowerCaseName]["status"] == "disconnected":
            currentPlayers[lowerCaseName]["status"] = "connected"
            print(f"Spieler RECONNECTED: {username} (IP: {ipAddress})")
            return

        playerData = {
            'username': username,
            'sid': "",
            'ip': ipAddress,
            'status': "connected"
        }

        currentPlayers[lowerCaseName] = playerData

        print(currentPlayers)

        return redirect(url_for('lobby.main_lobby',))
    
    return render_template('register.html')