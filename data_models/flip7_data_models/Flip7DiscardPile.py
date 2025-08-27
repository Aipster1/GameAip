from dataclasses import dataclass, field
from data_models.flip7_data_models.Flip7Card import Flip7Card


@dataclass
class Flip7DiscardPile:
    cards: list[Flip7Card] = field(default_factory=list)   
    
    def clear(self) -> None:
        self.cards.clear()

    def extend(self, cards: list[Flip7Card]) -> None:
        self.cards.extend(cards)
