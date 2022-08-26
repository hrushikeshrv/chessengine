from ..bitboard import Board


class Game:
    """
    A class representing a game, keeping track of the moves made
    throughout the game and the GameNodes reached as a result.
    Used to record a game and replay it.
    """

    def __init__(self, board: Board) -> None:
        self.board: Board = board
        self.moves: list[str] = []
        self.nodes: dict[
            str:GameNode
        ] = {}  # A dictionary mapping board hashes to the board objects
        self.headers: dict[str:str] = {}


class GameNode:
    """
    A class representing a node in a game. Useful for
    parsing a PGN game and building a tree of moves
    for the opening book.
    """

    def __init__(self, turn: str, board: Board) -> None:
        self.turn: str = turn
        self.board: Board = board
        self.children: dict[str:Board] = {}
