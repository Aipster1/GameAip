from dataclasses import dataclass


@dataclass(frozen=True)
class Flip7Card:
    type: str    # "number", "modifier", "action"
    value: any   # int for numbers, str for others
    filename: str
