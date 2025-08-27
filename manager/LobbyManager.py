from secrets import token_hex
from typing import Dict, List

from data_models.Lobby import Lobby

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

            lobby = Lobby(id=lobbyId, name=name, lobby_type=lobbyType, host_Id=hostId, members=[hostId], max_member_count=maxMember)
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
            elif lob.host_Id == userId:  
                lob.host_Id = lob.members[0]
        # emit(updateLobby)


    def listOpen(self) -> List[Lobby]:
        return [l for l in self._lobbies.values() if l.is_open]
    

    def delete():
        # lobby löschen wenn letzter Spieler raus ist und kein host weitergegeben werden kann
        # rufe UpdateLobyList event auf damit es aktualisiert
        pass
    

lobbyStorage = LobbyStore()