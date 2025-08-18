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
  
# discardPile = []

@dataclass
class Card:
    type: str    # "number", "modifier", "action"
    value: any   # int for numbers, str for others
    filename: str
    

### Deck functions ###
def buildDeck(deck):
    """Function to build the deck."""

    # init empty deck
    # deck = []

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


def removeCardFromDeck(card, deck):
    """Function to remove a card from a deck."""
    #todo: check if enough cards are in the deck
    # else shuffle discard pile and add to deck

    deck.remove(card)
    print("removed card:", card)


def shuffleDeck(deck):
    """Function to shuffle a deck."""
    random.shuffle(deck)

### player functions ###

def drawCard(numCards, deck):
    """Function to draw cards."""

    drawnCards = deck[0:numCards]

    for card in drawnCards:
        removeCardFromDeck(card, deck)

    return drawnCards


def getPlayerHand(player):
    """Function to get all cards of a player."""
    hand = gameData["players"][f"{player}"]["cards"]
    return hand


def clearPlayerHand(player):
    """Function to clear all cards of a player."""
    gameData["players"][f"{player}"]["cards"] = []


# def playerBust(player):
#     """Function to bust a player. Removes all cards from hand and puts them on the discard pile."""
#     playerHand = getPlayerHand(player)

#     discardPile.append(playerHand)
    
#     clearPlayerHand(player)


def getDeckCardCount(deck):

    result = len(deck)

    return result


# initialize
gameData = {
    "roundCount":0,
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
    "currentPlayer": "tim",
}




# deck = buildDeck()

# shuffleDeck(deck)


# # game logic

# hand = drawCard(3, deck)

# gameData["players"]["tim"]["cards"] = hand

# print("gameData: ", gameData)

# playerBust("tim")

# print(discardPile)

# print("tims hand: ", gameData["players"]["tim"]["cards"])

