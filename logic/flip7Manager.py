from dataclasses import dataclass
import random

# flip 7 logic
# lobby
# aktueller spieler highlighted
# liste mit zahlen 
# spieler hat button hit or stand wie bei black jack
# bei freeze und take 3 kann er einen Spieler wählen der noch nicht freeze oder bust ist


@dataclass
class Card:
    type: str    # "number", "modifier", "action"
    value: any   # int for numbers, str for others


def build_deck():
    deck = []

    for n in range(0, 13):
        deck.extend([Card("number", n)] * (1 if n == 0 else n))

    modifiers = [2,4,6,8,10]

    for m in modifiers:
        deck.append([Card("modifier",f"+{m}")])

    deck.append([Card("modifier",f"x2")])

    for action in ["freeze", "flip_three", "second_chance"]:
        deck.extend([Card("action", action)] * 3)

    return deck


def draw_card(num_cards, deck):
    drawn_cards = deck[0:num_cards]

    for card in drawn_cards:
        remove_card_from_deck(card, deck)

    return drawn_cards


def remove_card_from_deck(card, deck):
    deck.remove(card)
    print("removed card:", card)


def player_bust(player):

    
    #add hand cards to discard_pile
    pass


# initialize

discard_pile = []

deck = build_deck()

random.shuffle(deck)


# game logic

hand = draw_card(1, deck)









