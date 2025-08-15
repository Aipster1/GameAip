from secrets import token_hex
from flask import session


def current_user_id():
    session["name"] = "testname"
    if 'uid' not in session:
        session['uid'] = f"user_{token_hex(4)}"
        session.permanent = True
    return session['uid']