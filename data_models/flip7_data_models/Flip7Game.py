from dataclasses import dataclass, field

from data_models.Game import Game
from data_models.flip7_data_models.Flip7DiscardPile import Flip7DiscardPile
from data_models.flip7_data_models.Flip7DrawPile import Flip7DrawPile

@dataclass
class Flip7Game(Game):
    draw_pile: Flip7DrawPile = field(default_factory=Flip7DrawPile)
    discard_pile: Flip7DiscardPile = field(default_factory=Flip7DiscardPile)
