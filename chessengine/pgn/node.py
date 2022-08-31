from ..bitboard import Board


class Game:
    """
    A class representing a game, keeping track of the moves made
    throughout the game and the GameNodes reached as a result.
    Used to record a game and replay it.
    """

    def __init__(self, root_node) -> None:
        self.headers: dict[str:str] = {}
        self.root_node: GameNode = root_node
        self.result = ""
        self.move_text = ''

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

    def __init__(self, turn: str) -> None:
        self.turn: str = turn
        self.children: dict[str:GameNode] = {}  # Maps SAN move strings to GameNode

    def __repr__(self):
        children = ''
        for c in self.children:
            children += ' ' + c
        return f'<chessengine.GameNode: {self.turn[0]} - {{{children.strip()}}}>'

    def add_child(self, move: str):
        if move not in self.children:
            turn = "white" if self.turn == "black" else "black"
            new_node = GameNode(turn)
            self.children[move] = new_node

        return self.children[move]

    def get_child(self, move: str):
        if move not in self.children:
            raise ValueError(f"{move} is not a child of the current Game Node.")
        return self.children[move]
