"""
The PGN parser class
"""


import re
from chessengine.pgn.node import GameNode, Game

# groups()[0] = The piece moved, one of {K, Q, N, R, B}, None if a pawn was moved
# groups()[1] = The file the piece was moved from. Present to resolve ambiguity, if any
# groups()[2] = The rank the piece was moved from. Present to resolve ambiguity, if any
# groups()[3] = The square the piece was moved to. Always non-null
# groups()[4] = The piece a pawn was promoted to, if a pawn reached the last rank
SAN_MOVE_REGEX = re.compile(
    "([KQNRB\u2654\u2655\u2656\u2657\u2658\u2659\u265A\u265B\u265C\u265D\u265E\u265F])?([a-h])?([1-8])?x?([a-h][1-8])=?([QNRB])?"
)
MOVE_TEXT_COMMENT_REGEX = re.compile(
    r"\s*{.*?}\s*"
)  # TODO - add support for removing line comments
MOVE_TEXT_MOVE_REGEX = re.compile(
    r"(\d+)\.\s*([A-Za-z0-9\-+=]+)\s+([A-Za-z0-9\-+=]+)\s*(1-0|0-1|1/2-1/2)?\s*"
)


class PGNParser:
    """
    A parser for parsing PGN files and constructing a tree of GameNodes
    
    :param pgn_files: A list of PGN files passed as strings, path-like objects, or file-like objects
    :ivar root_node: The root node of the Game tree that the opening book will start from (always corresponds to a new chess board)
    :ivar games: A list of games parsed by the parser
    """

    def __init__(self, pgn_files: list[str] = None) -> None:
        self.pgn_files = pgn_files  # Path to the pgn_file to parse OR file object
        self.root_node: GameNode = GameNode("white")
        self.current_node = self.root_node
        self.current_game = None
        self.games: list[Game] = []

    def parse(self, pgn_file=None):
        """
        Parse the given pgn file if pgn_file is not None.
        Otherwise, parse all the pgn files in self.pgn_files.

        :param pgn_file: a path to a PGN file as a string, path-like object, or file-like object
        """
        files_to_parse = [pgn_file] if pgn_file is not None else self.pgn_files
        for file in files_to_parse:
            try:
                self._parse(file)
            except (TypeError, AttributeError):
                with open(file, mode="r", errors="replace") as opened_pgn_file:
                    self._parse(opened_pgn_file)

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
        if "{" in move_text:
            # Remove all comments from the move text
            move_text = MOVE_TEXT_COMMENT_REGEX.sub(" ", move_text).strip()
        self.current_game.move_text = move_text

        ply_number = 0
        move_list = MOVE_TEXT_MOVE_REGEX.findall(move_text.strip())
        last_move = move_list.pop()
        for _, white_move, black_move, _ in move_list:
            self.current_node = self.current_node.add_child(white_move)
            ply_number += 1
            self.current_node = self.current_node.add_child(black_move)
            ply_number += 1

        if last_move[2] in {"1-0", "0-1", "1/2-1/2"}:
            self.current_game.result = last_move[2]
        else:
            self.current_node = self.current_node.add_child(last_move[2])
        if last_move[3] in {"1-0", "0-1", "1/2-1/2"}:
            self.current_game.result = last_move[3]
