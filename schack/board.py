from enum import Enum
from typing import List

class Color(Enum):
    BLACK: int = 0
    WHITE: int = 1

class Piece(Enum):
    KING: int = 0
    QUEEN: int = 1
    ROOK: int = 2
    BISHOP: int = 3
    KNIGHT: int = 4
    PAWN: int = 5


class Board:
    
    BitBoard: List[List[int]] = [[0 for x in range(6)] for y in range(2)]

    def __init__(self):
        print("Board created")


    
