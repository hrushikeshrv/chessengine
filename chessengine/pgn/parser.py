from ..bitboard import Board
from .node import GameNode, Game


class PGNParser:
    """
    A parser for parsing PGN files and constructing a tree of GameNodes
    """

    def __init__(self, pgn_files: list[str] = None) -> None:
        self.pgn_files = pgn_files  # Path to the pgn_file to parse OR file object
        self.root_node = GameNode("white")
        self.current_node = self.root_node
        self.current_game = None
        self.games: list[Game] = []

    def parse(self, pgn_file=None):
        if pgn_file is not None:
            try:
                self._parse(pgn_file)
            except (TypeError, AttributeError):
                with open(pgn_file, mode="r") as pgn_file:
                    self._parse(pgn_file)
        else:
            for file in self.pgn_files:
                try:
                    self._parse(file)
                except (TypeError, AttributeError):
                    with open(file, mode='r') as pgn_file:
                        self._parse(pgn_file)

    def _parse(self, pgn_file):
        """
        Parses a PGN file and builds a tree of GameNodes
        """
        lines = pgn_file.readlines()
        new_game = True
        move_text = ""
        for line in lines:
            if not line:
                continue
            if line.startswith("["):
                if move_text:
                    # Completely parses the move text of a game. Ends that game.
                    self._parse_move_text(move_text)
                    new_game = True
                if new_game:
                    # New game starts here. Reset current node.
                    self.current_game = Game(self.root_node)
                    self.games.append(self.current_game)

                    self.current_node = self.root_node
                    move_text = ""
                    new_game = False
                self._parse_header(line)
            else:
                # This is the move text
                new_game = False
                move_text += " " + line.strip()
        self._parse_move_text(move_text)

    def _parse_header(self, header_string: str):
        """
        Parses a header string in a PGN file and sets the
        header on the current game
        """
        header_string = header_string.strip()[1:][:-1]
        _ = header_string.split()
        key = _[0]
        value = " ".join(_[1:])
        if value.startswith('"') and value.endswith('"'):
            value = value[1:][:-1]
        self.current_game.add_header(key, value)

    def _parse_move_text(self, move_text: str):
        self.current_game.move_text = move_text
        move_list = move_text.strip().split(".")
        last_move = move_list.pop()
        for m in move_list[1:]:
            move = m.split()
            self.current_node = self.current_node.add_child(move[0])
            self.current_node = self.current_node.add_child(move[1])

        # Make the last move separately
        self.current_node = self.current_node.add_child(last_move[0])
        if last_move[1] not in {"1-0", "0-1", "1/2-1/2"}:
            self.current_node = self.current_node.add_child(last_move[1])
        self.current_game.result = last_move[-1]
