from ..bitboard import Board


class Game:
    """
    A class representing a game, keeping track of the moves made
    throughout the game and the GameNodes reached as a result.
    Used to record a game and replay it.
    """

    def __init__(self, root_node) -> None:
        self.moves: list[str] = []
        self.nodes: dict[
            str:GameNode
        ] = {}  # A dictionary mapping board hashes to the board objects
        self.headers: dict[str:str] = {}
        self.root_node: GameNode = root_node
        self.result = ""

    def add_header(self, key, value):
        if key in self.headers:
            raise ValueError(
                f"{key} header has already been set on this game - {self.headers[key]}."
            )
        self.headers[key] = value


class GameNode:
    """
    A class representing a node in a game. Useful for
    parsing a PGN game and building a tree of moves
    for the opening book.
    """

    def __init__(self, turn: str, board: Board) -> None:
        self.turn: str = turn
        self.board: Board = board
        self.children: dict[str:GameNode] = {}  # Maps SAN move strings to GameNode

    def add_child(self, move: str):
        if move not in self.children:
            new_board = self.board.copy()
            new_board.move_san(move)

            turn = "white" if self.turn == "black" else "black"
            new_node = GameNode(turn, new_board)
            self.children[move] = new_node

        return self.children[move]

    def get_child(self, move: str):
        if move not in self.children:
            raise ValueError(f"{move} is not a child of the current Game Node.")
        return self.children[move]
