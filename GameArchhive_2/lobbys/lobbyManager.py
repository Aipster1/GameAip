from secrets import token_hex
from typing import Dict, List
import uuid
from dataclasses import dataclass, field


@dataclass
class Lobby:
    id: str
    name: str
    lobbyType: str
    hostId: str
    members: List[str] = field(default_factory=list)
    maxMemberCount: int = 1
    isOpen: bool = True


class LobbyStore:
    def __init__(self):
        self._lobbies: Dict[str, Lobby] = {}


    def create(self, name: str, lobbyType: str, hostId: str) -> Lobby:
            match lobbyType:
                case "flip7":
                    maxMember = 7
                    lobbyId =  f"flip7Lobby_{token_hex(4)}"
                case _:
                    lobbyId =  f"genericLobby_{token_hex(4)}"
                
                # case "keywords":
                #     maxMember = 10
                #     lobbyId =  f"keywordsLobby_{token_hex(4)}"

            lobby = Lobby(id=lobbyId, name=name, lobbyType=lobbyType, hostId=hostId, members=[hostId], maxMemberCount=maxMember)
            self._lobbies[lobbyId] = lobby
            return lobby
    

    def get(self, lobbyId: str) -> Lobby | None:
        return self._lobbies.get(lobbyId)


    def join(self, lobbyId: str, userId: str):
        lob = self._lobbies[lobbyId]
        if userId not in lob.members:
            lob.members.append(userId)
            

    def leave(self, lobbyId: str, userId: str):
        lob = self._lobbies[lobbyId]
        if userId in lob.members:
            lob.members.remove(userId)
            if not lob.members:
                self._lobbies.pop(lobbyId, None)
            elif lob.hostId == userId:  
                lob.hostId = lob.members[0]
        # emit(updateLobby)


    def listOpen(self) -> List[Lobby]:
        return [l for l in self._lobbies.values() if l.isOpen]
    

    def delete():
        # lobby löschen wenn letzter Spieler raus ist und kein host weitergegeben werden kann
        # rufe UpdateLobyList event auf damit es aktualisiert
        pass
    

lobbyStorage = LobbyStore()