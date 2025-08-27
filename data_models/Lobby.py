from dataclasses import dataclass, field


@dataclass
class Lobby:
    id: str
    name: str
    lobby_type: str
    host_Id: str
    members: list[str] = field(default_factory=list)
    max_member_count: int = 7
    is_open: bool = True