"""Global exceptions for the engine"""


class PositionError(Exception):
    """An invalid position was passed"""

    pass


class MoveError(Exception):
    """An invalid move was passed"""

    pass


class PGNParsingError(Exception):
    """An error occurred while parsing a PGN file/move"""

    pass


class GameNodeError(Exception):
    """A GameNode was not found in the game tree"""

    pass
