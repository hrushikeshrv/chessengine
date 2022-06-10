"""
Lookup tables are bitboards that allow us to mask or clear specific ranks or files of the chessboard
"""
clear_rank = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

mask_rank = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

clear_file = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

mask_file = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

# Maps a board position with a binary number only having a 1 at that position
# Used to check if a particular position on a bitboard is 1 or 0
mask_position = {}

# Maps a board position with a binary number only having a 0 at that position.
# Used to set a particular position on a bitboard to 0
clear_position = {}

# Maps a board position with a binary number only having a 1 at that position.
# Used to set a particular position on a bitboard to 1
set_position = {}
