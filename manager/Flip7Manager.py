from dataclasses import dataclass
import random

from data_models.flip7_data_models.Flip7Game import Flip7Game
from data_models.flip7_data_models.Flip7Card import Flip7Card
from data_models.Player import Flip7Player

# --- Flip7 Manager that holds all methods that can be executed in the game ---
@dataclass
class Flip7Manager:

    # --- deck construction ---
    
    def build_deck(self, game: Flip7Game) -> None:
        '''Builds and shuffles the deck'''

        deck: list[Flip7Card] = []
        for n in range(0, 13):
            count = 1 if n == 0 else n
            for _ in range(count):
                deck.append(Flip7Card("number", n, f"{n}.png"))

        for m in [2, 4, 6, 8, 10]:
            deck.append(Flip7Card("modifier", f"+{m}", f"+{m}.png"))
        deck.append(Flip7Card("modifier", "x2", "x2.png"))

        for action in ["freeze", "flipThree", "secondChance"]:
            for _ in range(3):
                deck.append(Flip7Card("action", action, f"{action}.png"))

        random.shuffle(deck)
        game.draw_pile.cards = deck
        
    # --- shuffle draw pile ---
    def shuffle_draw_pile(self, game: Flip7Game) -> None:
        """Function to shuffle a deck."""
        random.shuffle(game.draw_pile.cards)
        
    # --- shuffle discard pile ---
    def shuffle_discard_pile(self, game: Flip7Game) -> None:
        """Function to shuffle a deck."""
        random.shuffle(game.discard_pile.cards)

    # --- deal a card to a player ---
    def deal_to(self, player: Flip7Player, game: Flip7Game) -> Flip7Card:
        if not game.draw_pile.cards and not game.discard_pile.cards:
            return print("Can not deal. No cards on the draw and discard pile.")
        
        elif not game.draw_pile.cards and game.discard_pile.cards:
            self._reshuffle_discard_into_draw()
            
            self._deal_card(game, player)
        else:

            self._deal_card(game, player)

        #todo: emit update
            
    

    # --- internal classes ---
    def _player_bust(self, player: Flip7Player, game : Flip7Game):
        '''Adds the player hand to discard pile and sets status to bust, does NOT clear the hand'''
        game.discard_pile.extend(player.hand)

        player.status = "bust"
        

    # --- remove card from draw pile ---
    def _remove_card_from_deck(self, game: Flip7Game, card: Flip7Card):
        game.draw_pile.cards.remove(card)
        print("card removed")

    # --- reshuffle the discard pile to get cards for the draw pile ---
    def _reshuffle_discard_into_draw(self, game: Flip7Game) -> None:
        if not game.draw_pile.cards and game.discard_pile.cards:
            game.draw_pile.cards = game.discard_pile.cards[:]
            game.discard_pile.cards.clear()
            random.shuffle(game.draw_pile.cards)

    # --- get card from draw pile, remove it and add it to player hand --- 
    def _deal_card(self, game : Flip7Game, player: Flip7Player):
        '''Deals a card to a player, removes it from the drawpile and adds to player hand'''
        card: Flip7Card

        if not player.status == "active":
            return
         
        card = game.draw_pile.cards[0]
        
        self._remove_card_from_deck(game=game, card=card)

        if card.type == "number" and card in player.hand:
            if self._player_has_second_chance(player):
                self._remove_second_chance(player, game)
                game.discard_pile.extend([card])
                return

            player.hand.append(card)
            self._player_bust(player, game)  
            return
        
        player.hand.append(card)
    

    def _player_has_second_chance(self, player: Flip7Player):
        for card in player.hand:
            if card.type == "action" and card.value == "secondChance":
                return True
            
    def _remove_second_chance(self, player: Flip7Player, game: Flip7Game):
        for card in player.hand:
            if card.type == "action" and card.value == "secondChance":
                player.hand.remove(card)
                game.discard_pile.extend([card])


flip7_manager = Flip7Manager()