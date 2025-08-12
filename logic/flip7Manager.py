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


def draw_card(card_count):
    #draw card
    pass


def player_bust(player):
    #add hand cards to discard_pile
    pass



discard_pile = []


deck = build_deck()


random.shuffle(deck)

print(deck)








