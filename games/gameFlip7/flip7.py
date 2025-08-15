from flask import Blueprint, render_template, request, session
from .logic.flip7Manager import *

gameFlip7Bp = Blueprint('gameFlip7Bp', __name__,
                       template_folder='templates',
                        static_folder='static',
                        static_url_path='/gameFlip7')


@gameFlip7Bp.route('/game/flip7')
def flip7Game():
    print("[ROUTE] Aufgerufen: /game/flip7")

    deck = build_deck()
    
    shuffle_deck(deck)

    hand = draw_card(6, deck)

    player_cards = hand

    print(get_deck_card_count(deck))

    return render_template('flip7Game.html', player_cards = player_cards)