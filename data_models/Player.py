from dataclasses import dataclass, field

from data_models.flip7_data_models.Flip7Card import Flip7Card


@dataclass
class Player:
    user_Id: str
    username: str
    sid: str
    ip_address: str


@dataclass
class Flip7Player(Player):
    hand: list[Flip7Card] = field(default_factory=list[Flip7Card]) 
    status: str  = "" # frozen, bust, in, out, (for display purpose)
    active: bool = True # true: can draw cards (status in)  false: is out and can not draw cards (out)
    wants_to_draw: bool = True
    hand_score: int = 0
    total_score: int = 0