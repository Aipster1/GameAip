from dataclasses import dataclass, field
from secrets import token_hex
from typing import Dict, List


@dataclass
class Game:
    id: str
    lobbyId: str
    gameType: str
    members: dict = field(default_factory=dict)
    isRunning: bool = True


class GameStore:
    def __init__(self):
        self._games: Dict[str, Game] = {}


    def create(self, lobbyId: str, gameType: str, members: dict) -> Game:
            
            gameId = f"{gameType}_{token_hex(4)}"

            game = Game(id=gameId, lobbyId=lobbyId, gameType=gameType, members=members)
            self._games[gameId] = game
            return game
    

    def get(self, gameId: str) -> Game | None:
        return self._games.get(gameId)

    def reconnect(self, player):
        pass


    # def join(self, lobbyId: str, userId: str):
    #     lob = self._lobbies[lobbyId]
    #     if userId not in lob.members:
    #         lob.members.append(userId)
            

    # def leave(self, lobbyId: str, userId: str):
    #     lob = self._lobbies[lobbyId]
    #     if userId in lob.members:
    #         lob.members.remove(userId)
    #         if not lob.members:
    #             self._lobbies.pop(lobbyId, None)
    #         elif lob.hostId == userId:  
    #             lob.hostId = lob.members[0]
        # emit(updateLobby)


    def listRunningGames(self) -> List[Game]:
        return [l for l in self._games.values() if l.isRunning]
    

    def delete():
        # lobby löschen wenn letzter Spieler raus ist und kein host weitergegeben werden kann
        # rufe UpdateLobyList event auf damit es aktualisiert
        pass
    

gameStorage = GameStore()