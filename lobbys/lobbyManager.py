from typing import Dict, List
import uuid
from dataclasses import dataclass, field


@dataclass
class Lobby:
    id: str
    name: str
    lobby_type: str
    host_id: str
    members: List[str] = field(default_factory=list)
    is_open: bool = True


class LobbyStore:
    def __init__(self):
        self._lobbies: Dict[str, Lobby] = {}


    def create(self, name: str, lobby_type: str, host_id: str) -> Lobby:
            lobby_id = uuid.uuid4().hex[:6].upper()
            lobby = Lobby(id=lobby_id, name=name, lobby_type=lobby_type, host_id=host_id, members=[host_id])
            self._lobbies[lobby_id] = lobby
            return lobby
    

    def get(self, lobby_id: str) -> Lobby | None:
        return self._lobbies.get(lobby_id)


    def join(self, lobby_id: str, user_id: str):
        lob = self._lobbies[lobby_id]
        if user_id not in lob.members:
            lob.members.append(user_id)
            

    def leave(self, lobby_id: str, user_id: str):
        lob = self._lobbies[lobby_id]
        if user_id in lob.members:
            lob.members.remove(user_id)
            if not lob.members:
                self._lobbies.pop(lobby_id, None)
            elif lob.host_id == user_id:  
                lob.host_id = lob.members[0]
        # emit(updateLobby)


    def list_open(self) -> List[Lobby]:
        return [l for l in self._lobbies.values() if l.is_open]
    

    def delete():
        # lobby löschen wenn letzter Spieler raus ist und kein host weitergegeben werden kann
        # rufe UpdateLobyList event auf damit es aktualisiert
        pass
    

lobbyStorage = LobbyStore()