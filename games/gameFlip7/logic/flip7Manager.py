from dataclasses import dataclass
import random


# aktueller spieler highlighted
# liste mit zahlen 
# spieler hat button hit or stand wie bei black jack
# bei freeze und take 3 kann er einen Spieler wählen der noch nicht freeze oder bust ist



# class Card:
#     def __init__(self, type: str, value: any, filename: str):

#         self.type = type
#         self.value = value
#         self.filename = filename
  


@dataclass
class Card:
    type: str    # "number", "modifier", "action"
    value: any   # int for numbers, str for others
    filename: str
    

### Deck functions ###
def build_deck():
    """Function to build the deck."""

    # init empty deck
    deck = []

    # add all number cards to deck
    for n in range(0, 13):
        deck.extend([Card("number", n, str(n)+ ".png")] * (1 if n == 0 else n))

    # add modifier cards to deck
    for m in [2,4,6,8,10]:
        deck.extend([Card("modifier",f"+{m}",f"+{m}.png")])

    # add x2 modifier card to deck
    deck.extend([Card("modifier",f"x2", f"x2.png")])

    # add action cards to deck
    for action in ["freeze", "flipThree", "secondChance"]:
        deck.extend([Card("action", action, action + ".png")] * 3)

    return deck


def remove_card_from_deck(card, deck):
    """Function to remove a card from a deck."""
    #todo: check if enough cards are in the deck
    # else shuffle discard pile and add to deck

    deck.remove(card)
    print("removed card:", card)


def shuffle_deck(deck):
    """Function to shuffle a deck."""
    random.shuffle(deck)

### player functions ###

def draw_card(num_cards, deck):
    """Function to draw cards."""

    drawn_cards = deck[0:num_cards]

    for card in drawn_cards:
        remove_card_from_deck(card, deck)

    return drawn_cards


def get_player_hand(player):
    """Function to get all cards of a player."""
    hand = game_data["players"][f"{player}"]["cards"]
    return hand


def clear_player_hand(player):
    """Function to clear all cards of a player."""
    game_data["players"][f"{player}"]["cards"] = []


def player_bust(player):
    """Function to bust a player. Removes all cards from hand and puts them on the discard pile."""
    player_hand = get_player_hand(player)

    discard_pile.append(player_hand)
    
    clear_player_hand(player)


def get_deck_card_count(deck):

    result = len(deck)

    return result


# initialize
game_data = {
    "round_count":0,
    "players": {
        "tim":{
            "cards": [],
            "points": 0,
        },
        "olaf":{
            "cards": [],
            "points": 0,
        }
    },
    "current_player": "tim",
}


discard_pile = []

deck = build_deck()

shuffle_deck(deck)


# game logic

hand = draw_card(3, deck)

game_data["players"]["tim"]["cards"] = hand

print("game_data: ", game_data)

player_bust("tim")

print(discard_pile)

print("tims hand: ", game_data["players"]["tim"]["cards"])

