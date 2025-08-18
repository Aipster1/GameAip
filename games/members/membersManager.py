from dataclasses import dataclass, field
from secrets import token_hex
from typing import Dict, List
from games.gameFlip7.flip7 import Card


@dataclass
class Player:
    uid: str
    sid: str
    ip: str
    


@dataclass
class Flip7Player(Player):
    hand: list
    status: str
    roundScore: int
    totalScore: int


class PlayerStore:
    def __init__(self):
        self._players: Dict[str, Player] = {}

    def create_flip7_player(self, uid: str, sid: str, ip:str, hand: list, status: str, roundScore: int, totalScore: int) -> Player:
            
            player = Flip7Player(uid=uid, sid=sid, ip=ip, hand=hand, status=status, roundScore=roundScore, totalScore=totalScore)
            self._players[uid] = player
            return player
    
    def get(self, uid: str) -> Flip7Player | None:
        return self._players.get(uid)
    
    def add_card_to_hand(card:Card, player:Player):
         player.hand.append(card)

    def freeze_player(player:Player):
        player.status = "freeze"
    
    




playerStorage = PlayerStore()