from ..bitboard import Board
from .node import GameNode


class PGNParser:
    """
    A parser for parsing PGN files and constructing a tree of GameNodes
    """
    def __init__(self, pgn_file: str = None) -> None:
        self.pgn_file = pgn_file    # Path to the pgn_file to parse OR file object
        self.headers: dict[str: str] = {}
        self.move_text = ''
        self.moves: list[str] = []
        self.nodes: dict[str: GameNode] = {}
        self.root_node = GameNode('white', Board('white'))
        self.current_node = self.root_node
    
    def parse(self):
        try:
            self._parse(self.pgn_file)
        except (TypeError, AttributeError):
            with open(self.pgn_file, mode='r') as pgn_file:
                self._parse(pgn_file)
    
    def _parse(self, pgn_file):
        """
        Parses a PGN file and builds a tree of GameNodes
        """
        lines = pgn_file.readlines()
        new_game = False
        for line in lines:
            if not line:
                continue
            if line.startswith('['):
                new_game = True
                # New game starts here. Reset current node.
                self.current_node = self.root_node
                self._parse_header(line)
            elif line[0].isnumeric():
                new_game = False
                
    def _parse_header(self, header_string):
        pass
