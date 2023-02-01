"""
Utility functions for the engine to efficiently use the
parsed PGN files
"""
from chessengine.pgn import GameNode


def best_move_from_tree(board, tree: GameNode) -> tuple[str, int]:
    """
    Searches the passed tree depth-first only using the moves in the
    tree and returns the best move to make. Makes the assumption that
    the passed tree will have considerably fewer moves as compared to
    the entire move space, and will only contain "good" moves, and hence
    complete depth-first search will be possible.

    This is a reasonable assumption only when the passed tree is
    from the engine's opening book.

    :param board: A ``chessengine.bitboard.Board`` object
    :param tree: A ``chessengine.pgn.node.GameNode`` object
    """
    if not tree.children:
        return "", board.evaluate_score()
    moves = tree.children.keys()
    best_move = moves[0]
    best_score = -100000 if board.side == "white" else 100000
    for move in moves:
        new_node = tree.get_child(move)
        new_score = 0
        board.move_san(move, tree.turn)
        if new_node.children:
            _, new_score = best_move_from_tree(board, new_node)
        board.undo_move()
    return best_move, best_score
