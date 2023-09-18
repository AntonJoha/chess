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

    # Board representation
    bitBoard: List[List[int]] = []

    def __init__(self):
        self.bitBoard = [[0 for x in range(6)] for y in range(2)]

    def Setup_Board(self):
        self.bitBoard[Color.WHITE.value][Piece.KING.value] = 0x0000000000000010
        self.bitBoard[Color.WHITE.value][Piece.QUEEN.value] = 0x0000000000000008
        self.bitBoard[Color.WHITE.value][Piece.ROOK.value] = 0x0000000000000081
        self.bitBoard[Color.WHITE.value][Piece.BISHOP.value] = 0x0000000000000024
        self.bitBoard[Color.WHITE.value][Piece.KNIGHT.value] = 0x0000000000000042
        self.bitBoard[Color.WHITE.value][Piece.PAWN.value] = 0x000000000000FF00

        self.bitBoard[Color.BLACK.value][Piece.KING.value] = 0x1000000000000000
        self.bitBoard[Color.BLACK.value][Piece.QUEEN.value] = 0x0800000000000000
        self.bitBoard[Color.BLACK.value][Piece.ROOK.value] = 0x8100000000000000
        self.bitBoard[Color.BLACK.value][Piece.BISHOP.value] = 0x2400000000000000
        self.bitBoard[Color.BLACK.value][Piece.KNIGHT.value] = 0x4200000000000000
        self.bitBoard[Color.BLACK.value][Piece.PAWN.value] = 0x00FF000000000000
