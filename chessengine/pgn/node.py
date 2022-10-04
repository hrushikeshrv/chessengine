"""
Defines the Game and GameNode class, used to parse PGN files and
create the opening book.
"""


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
        self.move_text = ""

    def add_header(self, key: str, value: str) -> None:
        """
        Add a header to Game.headers
        
        :param key: The header to be added (usually sourced from the PGN file)
        :param value: The value of the header
        
        :raises ValueError: If the key has already been added to the Game
        """
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
    
    Provides a ``children`` dictionary that maps a move (str) made from
    this GameNode to the GameNode representing the new Board state.
    
    :param turn: The side to move on this GameNode.
    """

    def __init__(self, turn: str) -> None:
        self.turn: str = turn
        self.children: dict[str:GameNode] = {}  # Maps SAN move strings to GameNode

    def __repr__(self):
        children = ""
        for c in self.children:
            children += " " + c
        return f"<chessengine.GameNode: {self.turn[0]} - {{{children.strip()}}}>"

    def __contains__(self, move: str) -> bool:
        return move in self.children

    def add_child(self, move: str):
        """
        Create a new GameNode and add it as a child to the current node in
        the ``children`` dictionary.
        
        :param move: The move made to reach the new game node
        :return GameNode: Return the newly created GameNode.
        """
        if move not in self.children:
            turn = "white" if self.turn == "black" else "black"
            new_node = GameNode(turn)
            self.children[move] = new_node

        return self.children[move]

    def get_child(self, move: str):
        """
        Check if ``move`` is a child of this GameNode. If it is,
        return the corresponding GameNode, else raise ValueError.
        
        :param move: The move to check for
        :return GameNode: Return the GameNode if found
        :raises ValueError: If the move passed is not a child of the GameNode
        """
        if move not in self.children:
            raise ValueError(f"{move} is not a child of the current Game Node.")
        return self.children[move]
