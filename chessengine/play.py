from .bitboard import Board


if __name__ == "__main__":
    player_side = input("Do you want to play white or black (w/b)? - ")
    while not player_side.lower().strip().startswith(('b', 'w')):
        print(f'You entered an invalid side - {player_side}. Enter b for black and w for white')
        player_side = input("Do you want to play white or black (w/b)? - ")
    if player_side.lower().strip().startswith('w'):
        b = Board("black")
    else:
        b = Board('white')
    b.play()
