from secrets import token_hex
from flask import session


def currentUserId():
    if 'uid' not in session:
        session['uid'] = f"user_{token_hex(4)}"
        # session.permanent = True
    return session['uid']

def createGameId(gameType):

    gameId = f"{gameType}_{token_hex(4)}"
    print("Die gameId lautet: ",gameId)
    return gameId

def createMembersDict(membersList):
    players = {}

    for member in membersList:
        players[member] = { "status" : "",
                            "score" : 0 }
                            
    return players
    