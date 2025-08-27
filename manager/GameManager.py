from secrets import token_hex
from typing import Dict, List, Type

from data_models.Game import Game
from data_models.flip7_data_models.Flip7Game import Flip7Game as Flip7GameCls

# --- Factory to ensure correct subclass ---
GAME_CLASSES: Dict[str, Type[Game]] = {
    "flip7": Flip7GameCls,
    # other games ...
}

class GameStore:
    def __init__(self):
        self._games: Dict[str, Game] = {}


    def create(self, lobbyId: str, gameType: str, players: list) -> Game:
            
        cls = GAME_CLASSES.get(gameType)
        if cls is None:
            raise ValueError(f"Unknown gameType: {gameType}")
        gameId = f"{gameType}_{token_hex(4)}"
        game = cls(id=gameId,gameType=gameType, lobby_Id=lobbyId, players=players)  # <-- Flip7Game instance
        self._games[gameId] = game
        return game


        # gameId = f"{gameType}_{token_hex(4)}"

        # match gameType:
        #     case "flip7":

        # game = Game(id=gameId, lobby_Id=lobbyId, gameType=gameType, players=players)
        # self._games[gameId] = game
        # return game
    

    def get(self, gameId: str) -> Game | None:
        return self._games.get(gameId)

    def reconnect(self, player):
        pass

    def listRunningGames(self) -> List[Game]:
        return [l for l in self._games.values() if l.is_running]
    

    def delete():
        # lobby löschen wenn letzter Spieler raus ist und kein host weitergegeben werden kann
        # rufe UpdateLobyList event auf damit es aktualisiert
        pass
    

gameStorage = GameStore()