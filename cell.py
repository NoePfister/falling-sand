from enums import Types
from dataclasses import dataclass

@dataclass
class Cell:
    color: (int,int,int) = (0,0,0)
    type: Types = Types.EMPTY_CELL
