from dataclasses import dataclass, field

from data_models.Player import Player


@dataclass
class Game:
    id: str
    gameType: str
    lobby_Id: str
    players: list[Player] = field(default_factory=list[Player])
    current_player: Player = None
    winner: Player = None
    is_running: bool = True
