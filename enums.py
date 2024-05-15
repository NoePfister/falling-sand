from enum import Enum
class Types(Enum):
    CELL = 1
    EMPTY_CELL = 2


class Colors(Enum):
    RED= (255,51,51)
    ORANGE= (255,153,51)
    YELLOW= (255,255,51)
    GREEN= (51,255,51)
    BLUE= (51,51,255)
    PINK= (255,51,255)
    DEFAULT= (160,160,160)
    BLACK= (0,0,0)
