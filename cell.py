from enums import Types, Colors
from dataclasses import dataclass

@dataclass
class Cell:
    color: Colors = Colors.BLACK
    type: Types = Types.EMPTY_CELL
