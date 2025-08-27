
from typing import Dict
from data_models.flip7_data_models.Flip7Card import Flip7Card
from data_models.Player import Flip7Player

currentPlayers = {}

class PlayerStore:
    def __init__(self):
        self._players: Dict[str, Flip7Player] = {}

    def create_flip7_player(self, user_Id: str, sid: str, ip_address:str) -> Flip7Player:
            
            player = Flip7Player(user_Id=user_Id, username=user_Id, sid=sid, ip_address=ip_address)
            self._players[user_Id] = player
            return player
    
    def get(self, user_Id: str) -> Flip7Player | None:
        return self._players.get(user_Id)
    
    def add_card_to_hand(card:Flip7Card, player:Flip7Player):
         player.hand.append(card)

    def freeze_player(player:Flip7Player):
        player.status = "freeze"
    
    
playerStorage = PlayerStore()