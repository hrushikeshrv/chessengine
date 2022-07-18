def get_bit_positions(bitboard: int) -> list[int]:
    """
    Returns a list of positions in the bitboard which have a 1.
    1001100 returns [100, 1000, 1000000]
    """
    positions = []
    mask = 1
    for i in range(64):
        if bitboard & mask:
            positions.append(mask)
        mask = mask << 1
        
    return positions
