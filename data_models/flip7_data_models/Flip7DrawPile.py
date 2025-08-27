from dataclasses import dataclass, field
import random
from data_models.flip7_data_models.Flip7Card import Flip7Card

@dataclass
class Flip7DrawPile:
    cards: list[Flip7Card] = field(default_factory=list)   
    
    def extend(self, cards: list[Flip7Card]) -> None:
        self.cards.extend(cards)

    def clear(self) -> None:
        self.cards.clear()

    def draw(self, n: int) -> list[Flip7Card]:
        drawn = self.cards[:n]
        del self.cards[:n]
        return drawn
    
    def shuffle(self) -> None:
        random.shuffle(self.cards)
