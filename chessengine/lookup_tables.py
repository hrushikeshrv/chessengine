"""
The lookup tables module provides mappings between different position representation
formats, as well as utility bitboards that let you mask or clear individual ranks, files,
or positions on the chess board.
"""

pos_to_coords = {
    0: "A1",
    1: "B1",
    2: "C1",
    3: "D1",
    4: "E1",
    5: "F1",
    6: "G1",
    7: "H1",
    8: "A2",
    9: "B2",
    10: "C2",
    11: "D2",
    12: "E2",
    13: "F2",
    14: "G2",
    15: "H2",
    16: "A3",
    17: "B3",
    18: "C3",
    19: "D3",
    20: "E3",
    21: "F3",
    22: "G3",
    23: "H3",
    24: "A4",
    25: "B4",
    26: "C4",
    27: "D4",
    28: "E4",
    29: "F4",
    30: "G4",
    31: "H4",
    32: "A5",
    33: "B5",
    34: "C5",
    35: "D5",
    36: "E5",
    37: "F5",
    38: "G5",
    39: "H5",
    40: "A6",
    41: "B6",
    42: "C6",
    43: "D6",
    44: "E6",
    45: "F6",
    46: "G6",
    47: "H6",
    48: "A7",
    49: "B7",
    50: "C7",
    51: "D7",
    52: "E7",
    53: "F7",
    54: "G7",
    55: "H7",
    56: "A8",
    57: "B8",
    58: "C8",
    59: "D8",
    60: "E8",
    61: "F8",
    62: "G8",
    63: "H8",
}

coords_to_pos = {
    "A1": 0,
    "B1": 1,
    "C1": 2,
    "D1": 3,
    "E1": 4,
    "F1": 5,
    "G1": 6,
    "H1": 7,
    "A2": 8,
    "B2": 9,
    "C2": 10,
    "D2": 11,
    "E2": 12,
    "F2": 13,
    "G2": 14,
    "H2": 15,
    "A3": 16,
    "B3": 17,
    "C3": 18,
    "D3": 19,
    "E3": 20,
    "F3": 21,
    "G3": 22,
    "H3": 23,
    "A4": 24,
    "B4": 25,
    "C4": 26,
    "D4": 27,
    "E4": 28,
    "F4": 29,
    "G4": 30,
    "H4": 31,
    "A5": 32,
    "B5": 33,
    "C5": 34,
    "D5": 35,
    "E5": 36,
    "F5": 37,
    "G5": 38,
    "H5": 39,
    "A6": 40,
    "B6": 41,
    "C6": 42,
    "D6": 43,
    "E6": 44,
    "F6": 45,
    "G6": 46,
    "H6": 47,
    "A7": 48,
    "B7": 49,
    "C7": 50,
    "D7": 51,
    "E7": 52,
    "F7": 53,
    "G7": 54,
    "H7": 55,
    "A8": 56,
    "B8": 57,
    "C8": 58,
    "D8": 59,
    "E8": 60,
    "F8": 61,
    "G8": 62,
    "H8": 63,
}

clear_rank = {
    1: 18446744073709551360,
    2: 18446744073709486335,
    3: 18446744073692839935,
    4: 18446744069431361535,
    5: 18446742978492891135,
    6: 18446463698244468735,
    7: 18374967954648334335,
    8: 72057594037927935,
}

mask_rank = {
    1: 255,
    2: 65280,
    3: 16711680,
    4: 4278190080,
    5: 1095216660480,
    6: 280375465082880,
    7: 71776119061217280,
    8: 18374686479671623680,
}

clear_file = {
    1: 9187201950435737471,
    2: 13816973012072644543,
    3: 16131858542891098079,
    4: 17289301308300324847,
    5: 17868022691004938231,
    6: 18157383382357244923,
    7: 18302063728033398269,
    8: 18374403900871474942,
}

mask_file = {
    8: 9259542123273814144,
    7: 4629771061636907072,
    6: 2314885530818453536,
    5: 1157442765409226768,
    4: 578721382704613384,
    3: 289360691352306692,
    2: 144680345676153346,
    1: 72340172838076673,
}

# Maps a board position with a binary number only having a 1 at that position
# Used to check if a particular position on a bitboard is 1 or 0
mask_position = {
    2**0: 1,
    2**1: 2,
    2**2: 4,
    2**3: 8,
    2**4: 16,
    2**5: 32,
    2**6: 64,
    2**7: 128,
    2**8: 256,
    2**9: 512,
    2**10: 1024,
    2**11: 2048,
    2**12: 4096,
    2**13: 8192,
    2**14: 16384,
    2**15: 32768,
    2**16: 65536,
    2**17: 131072,
    2**18: 262144,
    2**19: 524288,
    2**20: 1048576,
    2**21: 2097152,
    2**22: 4194304,
    2**23: 8388608,
    2**24: 16777216,
    2**25: 33554432,
    2**26: 67108864,
    2**27: 134217728,
    2**28: 268435456,
    2**29: 536870912,
    2**30: 1073741824,
    2**31: 2147483648,
    2**32: 4294967296,
    2**33: 8589934592,
    2**34: 17179869184,
    2**35: 34359738368,
    2**36: 68719476736,
    2**37: 137438953472,
    2**38: 274877906944,
    2**39: 549755813888,
    2**40: 1099511627776,
    2**41: 2199023255552,
    2**42: 4398046511104,
    2**43: 8796093022208,
    2**44: 17592186044416,
    2**45: 35184372088832,
    2**46: 70368744177664,
    2**47: 140737488355328,
    2**48: 281474976710656,
    2**49: 562949953421312,
    2**50: 1125899906842624,
    2**51: 2251799813685248,
    2**52: 4503599627370496,
    2**53: 9007199254740992,
    2**54: 18014398509481984,
    2**55: 36028797018963968,
    2**56: 72057594037927936,
    2**57: 144115188075855872,
    2**58: 288230376151711744,
    2**59: 576460752303423488,
    2**60: 1152921504606846976,
    2**61: 2305843009213693952,
    2**62: 4611686018427387904,
    2**63: 9223372036854775808,
}

# Maps a board position with a binary number only having a 0 at that position.
# Used to set a particular position on a bitboard to 0
clear_position = {
    2**0: 36893488147419103230,
    2**1: 36893488147419103229,
    2**2: 36893488147419103227,
    2**3: 36893488147419103223,
    2**4: 36893488147419103215,
    2**5: 36893488147419103199,
    2**6: 36893488147419103167,
    2**7: 36893488147419103103,
    2**8: 36893488147419102975,
    2**9: 36893488147419102719,
    2**10: 36893488147419102207,
    2**11: 36893488147419101183,
    2**12: 36893488147419099135,
    2**13: 36893488147419095039,
    2**14: 36893488147419086847,
    2**15: 36893488147419070463,
    2**16: 36893488147419037695,
    2**17: 36893488147418972159,
    2**18: 36893488147418841087,
    2**19: 36893488147418578943,
    2**20: 36893488147418054655,
    2**21: 36893488147417006079,
    2**22: 36893488147414908927,
    2**23: 36893488147410714623,
    2**24: 36893488147402326015,
    2**25: 36893488147385548799,
    2**26: 36893488147351994367,
    2**27: 36893488147284885503,
    2**28: 36893488147150667775,
    2**29: 36893488146882232319,
    2**30: 36893488146345361407,
    2**31: 36893488145271619583,
    2**32: 36893488143124135935,
    2**33: 36893488138829168639,
    2**34: 36893488130239234047,
    2**35: 36893488113059364863,
    2**36: 36893488078699626495,
    2**37: 36893488009980149759,
    2**38: 36893487872541196287,
    2**39: 36893487597663289343,
    2**40: 36893487047907475455,
    2**41: 36893485948395847679,
    2**42: 36893483749372592127,
    2**43: 36893479351326081023,
    2**44: 36893470555233058815,
    2**45: 36893452963047014399,
    2**46: 36893417778674925567,
    2**47: 36893347409930747903,
    2**48: 36893206672442392575,
    2**49: 36892925197465681919,
    2**50: 36892362247512260607,
    2**51: 36891236347605417983,
    2**52: 36888984547791732735,
    2**53: 36884480948164362239,
    2**54: 36875473748909621247,
    2**55: 36857459350400139263,
    2**56: 36821430553381175295,
    2**57: 36749372959343247359,
    2**58: 36605257771267391487,
    2**59: 36317027395115679743,
    2**60: 35740566642812256255,
    2**61: 34587645138205409279,
    2**62: 32281802128991715327,
    2**63: 27670116110564327423,
}

san_piece_map = {
    "P": "pawns",
    "K": "kings",
    "Q": "queens",
    "B": "bishops",
    "N": "knights",
    "R": "rooks",
    "\u2654": "kings",
    "\u2655": "queens",
    "\u2656": "rooks",
    "\u2657": "bishops",
    "\u2658": "knights",
    "\u2659": "pawns",
    "\u265A": "kings",
    "\u265B": "queens",
    "\u265C": "rooks",
    "\u265D": "bishops",
    "\u265E": "knights",
    "\u265F": "pawns",
}

# fmt: off

piece_square_table = {
    ('white', 'kings'): [
        20, 30, 10, 0, 0, 10, 30, 20,
        20, 20, 0, 0, 0, 0, 20, 20,
        -10, -20, -20, -20, -20, -20, -20, -10,
        20, -30, -30, -40, -40, -30, -30, -20,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30
    ],

    ('white', 'queens'): [
        -20, -10, -10, -5, -5, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 0, 5, 5, 5, 5, 0, -10,
        -5, 0, 5, 5, 5, 5, 0, -5,
        0, 0, 5, 5, 5, 5, 0, -5,
        -10, 5, 5, 5, 5, 5, 0, -10,
        -10, 0, 5, 0, 0, 0, 0, -10,
        -20, -10, -10, -5, -5, -10, -10, -20
    ],

    ('white', 'rooks'): [
        0, 0, 0, 5, 5, 0, 0, 0,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        5, 10, 10, 10, 10, 10, 10, 5,
        0, 0, 0, 0, 0, 0, 0, 0
    ],

    ('white', 'bishops'): [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10, 5, 0, 0, 0, 0, 5, -10,
        -10, 10, 10, 10, 10, 10, 10, -10,
        -10, 0, 10, 10, 10, 10, 0, -10,
        -10, 5, 5, 10, 10, 5, 5, -10,
        -10, 0, 5, 10, 10, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -10, -10, -10, -10, -20
    ],

    ('white', 'knights'): [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20, 0, 0, 0, 0, -20, -40,
        -30, 0, 10, 15, 15, 10, 0, -30,
        -30, 5, 15, 20, 20, 15, 5, -30,
        -30, 0, 15, 20, 20, 15, 0, -30,
        -30, 5, 10, 15, 15, 10, 5, -30,
        -40, -20, 0, 5, 5, 0, -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50
    ],

    ('white', 'pawns'): [
        0, 0, 0, 0, 0, 0, 0, 0,
        5, 10, 10, -20, -20, 10, 10, 5,
        5, -5, -10, 0, 0, -10, -5, 5,
        0, 0, 0, 20, 20, 0, 0, 0,
        5, 5, 10, 25, 25, 10, 5, 5,
        10, 10, 20, 30, 30, 20, 10, 10,
        50, 50, 50, 50, 50, 50, 50, 50,
        0, 0, 0, 0, 0, 0, 0, 0
    ],

    ('black', 'kings'): [
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        20, -30, -30, -40, -40, -30, -30, -20,
        -10, -20, -20, -20, -20, -20, -20, -10,
        20, 20, 0, 0, 0, 0, 20, 20,
        20, 30, 10, 0, 0, 10, 30, 20,
    ],

    ('black', 'queens'): [
        -20, -10, -10, -5, -5, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 0, 5, 5, 5, 5, 0, -10,
        -5, 0, 5, 5, 5, 5, 0, -5,
        0, 0, 5, 5, 5, 5, 0, -5,
        -10, 5, 5, 5, 5, 5, 0, -10,
        -10, 0, 5, 0, 0, 0, 0, -10,
        -20, -10, -10, -5, -5, -10, -10, -20
    ],

    ('black', 'rooks'): [
        0, 0, 0, 0, 0, 0, 0, 0,
        5, 10, 10, 10, 10, 10, 10, 5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        0, 0, 0, 5, 5, 0, 0, 0,
    ],

    ('black', 'bishops'): [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 0, 5, 10, 10, 5, 0, -10,
        -10, 5, 5, 10, 10, 5, 5, -10,
        -10, 0, 10, 10, 10, 10, 0, -10,
        -10, 10, 10, 10, 10, 10, 10, -10,
        -10, 5, 0, 0, 0, 0, 5, -10,
        -20, -10, -10, -10, -10, -10, -10, -20,
    ],

    ('black', 'knights'): [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20, 0, 0, 0, 0, -20, -40,
        -30, 0, 10, 15, 15, 10, 0, -30,
        -30, 5, 15, 20, 20, 15, 5, -30,
        -30, 0, 15, 20, 20, 15, 0, -30,
        -30, 5, 10, 15, 15, 10, 5, -30,
        -40, -20, 0, 5, 5, 0, -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50
    ],

    ('black', 'pawns'): [
        0, 0, 0, 0, 0, 0, 0, 0,
        50, 50, 50, 50, 50, 50, 50, 50,
        10, 10, 20, 30, 30, 20, 10, 10,
        5, 5, 10, 25, 25, 10, 5, 5,
        0, 0, 0, 20, 20, 0, 0, 0,
        5, -5, -10, 0, 0, -10, -5, 5,
        5, 10, 10, -20, -20, 10, 10, 5,
        0, 0, 0, 0, 0, 0, 0, 0,
    ],
}


knight_attacks = {
    1: [131072, 1024],
    2: [65536, 262144, 2048],
    4: [131072, 524288, 256, 4096],
    8: [262144, 1048576, 512, 8192],
    16: [524288, 2097152, 1024, 16384],
    32: [1048576, 4194304, 2048, 32768],
    64: [2097152, 8388608, 4096],
    128: [4194304, 8192],
    256: [4, 33554432, 262144],
    512: [8, 16777216, 67108864, 524288],
    1024: [1, 16, 33554432, 134217728, 65536, 1048576],
    2048: [2, 32, 67108864, 268435456, 131072, 2097152],
    4096: [4, 64, 134217728, 536870912, 262144, 4194304],
    8192: [8, 128, 268435456, 1073741824, 524288, 8388608],
    16384: [16, 536870912, 2147483648, 1048576],
    32768: [32, 1073741824, 2097152],
    65536: [2, 1024, 8589934592, 67108864],
    131072: [1, 4, 2048, 4294967296, 17179869184, 134217728],
    262144: [2, 8, 256, 4096, 8589934592, 34359738368, 16777216, 268435456],
    524288: [4, 16, 512, 8192, 17179869184, 68719476736, 33554432, 536870912],
    1048576: [8, 32, 1024, 16384, 34359738368, 137438953472, 67108864, 1073741824],
    2097152: [16, 64, 2048, 32768, 68719476736, 274877906944, 134217728, 2147483648],
    4194304: [32, 128, 4096, 137438953472, 549755813888, 268435456],
    8388608: [64, 8192, 274877906944, 536870912],
    16777216: [512, 262144, 2199023255552, 17179869184],
    33554432: [256, 1024, 524288, 1099511627776, 4398046511104, 34359738368],
    67108864: [512, 2048, 65536, 1048576, 2199023255552, 8796093022208, 4294967296, 68719476736],
    134217728: [1024, 4096, 131072, 2097152, 4398046511104, 17592186044416, 8589934592, 137438953472],
    268435456: [2048, 8192, 262144, 4194304, 8796093022208, 35184372088832, 17179869184, 274877906944],
    536870912: [4096, 16384, 524288, 8388608, 17592186044416, 70368744177664, 34359738368, 549755813888],
    1073741824: [8192, 32768, 1048576, 35184372088832, 140737488355328, 68719476736],
    2147483648: [16384, 2097152, 70368744177664, 137438953472],
    4294967296: [131072, 67108864, 562949953421312, 4398046511104],
    8589934592: [65536, 262144, 134217728, 281474976710656, 1125899906842624, 8796093022208],
    17179869184: [131072, 524288, 16777216, 268435456, 562949953421312, 2251799813685248, 1099511627776, 17592186044416],
    34359738368: [262144, 1048576, 33554432, 536870912, 1125899906842624, 4503599627370496, 2199023255552, 35184372088832],
    68719476736: [524288, 2097152, 67108864, 1073741824, 2251799813685248, 9007199254740992, 4398046511104, 70368744177664],
    137438953472: [1048576, 4194304, 134217728, 2147483648, 4503599627370496, 18014398509481984, 8796093022208, 140737488355328],
    274877906944: [2097152, 8388608, 268435456, 9007199254740992, 36028797018963968, 17592186044416],
    549755813888: [4194304, 536870912, 18014398509481984, 35184372088832],
    1099511627776: [33554432, 17179869184, 144115188075855872, 1125899906842624],
    2199023255552: [16777216, 67108864, 34359738368, 72057594037927936, 288230376151711744, 2251799813685248],
    4398046511104: [33554432, 134217728, 4294967296, 68719476736, 144115188075855872, 576460752303423488, 281474976710656, 4503599627370496],
    8796093022208: [67108864, 268435456, 8589934592, 137438953472, 288230376151711744, 1152921504606846976, 562949953421312, 9007199254740992],
    17592186044416: [134217728, 536870912, 17179869184, 274877906944, 576460752303423488, 2305843009213693952, 1125899906842624, 18014398509481984],
    35184372088832: [268435456, 1073741824, 34359738368, 549755813888, 1152921504606846976, 4611686018427387904, 2251799813685248, 36028797018963968],
    70368744177664: [536870912, 2147483648, 68719476736, 2305843009213693952, 9223372036854775808, 4503599627370496],
    140737488355328: [1073741824, 137438953472, 4611686018427387904, 9007199254740992],
    281474976710656: [8589934592, 4398046511104, 288230376151711744],
    562949953421312: [4294967296, 17179869184, 8796093022208, 576460752303423488],
    1125899906842624: [8589934592, 34359738368, 1099511627776, 17592186044416, 72057594037927936, 1152921504606846976],
    2251799813685248: [17179869184, 68719476736, 2199023255552, 35184372088832, 144115188075855872, 2305843009213693952],
    4503599627370496: [34359738368, 137438953472, 4398046511104, 70368744177664, 288230376151711744, 4611686018427387904],
    9007199254740992: [68719476736, 274877906944, 8796093022208, 140737488355328, 576460752303423488, 9223372036854775808],
    18014398509481984: [137438953472, 549755813888, 17592186044416, 1152921504606846976],
    36028797018963968: [274877906944, 35184372088832, 2305843009213693952],
    72057594037927936: [2199023255552, 1125899906842624],
    144115188075855872: [1099511627776, 4398046511104, 2251799813685248],
    288230376151711744: [2199023255552, 8796093022208, 281474976710656, 4503599627370496],
    576460752303423488: [4398046511104, 17592186044416, 562949953421312, 9007199254740992],
    1152921504606846976: [8796093022208, 35184372088832, 1125899906842624, 18014398509481984],
    2305843009213693952: [17592186044416, 70368744177664, 2251799813685248, 36028797018963968],
    4611686018427387904: [35184372088832, 140737488355328, 4503599627370496],
    9223372036854775808: [70368744177664, 9007199254740992],
}

# fmt: on

rook_attack_masks = {
    1: 72340172838076926,
    2: 144680345676153597,
    4: 289360691352306939,
    8: 578721382704613623,
    16: 1157442765409226991,
    32: 2314885530818453727,
    64: 4629771061636907199,
    128: 9259542123273814143,
    256: 72340172838141441,
    512: 144680345676217602,
    1024: 289360691352369924,
    2048: 578721382704674568,
    4096: 1157442765409283856,
    8192: 2314885530818502432,
    16384: 4629771061636939584,
    32768: 9259542123273813888,
    65536: 72340172854657281,
    131072: 144680345692602882,
    262144: 289360691368494084,
    524288: 578721382720276488,
    1048576: 1157442765423841296,
    2097152: 2314885530830970912,
    4194304: 4629771061645230144,
    8388608: 9259542123273748608,
    16777216: 72340177082712321,
    33554432: 144680349887234562,
    67108864: 289360695496279044,
    134217728: 578721386714368008,
    268435456: 1157442769150545936,
    536870912: 2314885534022901792,
    1073741824: 4629771063767613504,
    2147483648: 9259542123257036928,
    4294967296: 72341259464802561,
    8589934592: 144681423712944642,
    17179869184: 289361752209228804,
    34359738368: 578722409201797128,
    68719476736: 1157443723186933776,
    137438953472: 2314886351157207072,
    274877906944: 4629771607097753664,
    549755813888: 9259542118978846848,
    1099511627776: 72618349279904001,
    2199023255552: 144956323094725122,
    4398046511104: 289632270724367364,
    8796093022208: 578984165983651848,
    17592186044416: 1157687956502220816,
    35184372088832: 2315095537539358752,
    70368744177664: 4629910699613634624,
    140737488355328: 9259541023762186368,
    281474976710656: 143553341945872641,
    562949953421312: 215330564830528002,
    1125899906842624: 358885010599838724,
    2251799813685248: 645993902138460168,
    4503599627370496: 1220211685215703056,
    9007199254740992: 2368647251370188832,
    18014398509481984: 4665518383679160384,
    36028797018963968: 9259260648297103488,
    72057594037927936: 18302911464433844481,
    144115188075855872: 18231136449196065282,
    288230376151711744: 18087586418720506884,
    576460752303423488: 17800486357769390088,
    1152921504606846976: 17226286235867156496,
    2305843009213693952: 16077885992062689312,
    4611686018427387904: 13781085504453754944,
    9223372036854775808: 9187484529235886208,
}

bishop_attack_masks = {
    1: 18049651735527936,
    2: 70506452091904,
    4: 275415828992,
    8: 1075975168,
    16: 38021120,
    32: 8657588224,
    64: 2216338399232,
    128: 567382630219776,
    256: 9024825867763712,
    512: 18049651735527424,
    1024: 70506452221952,
    2048: 275449643008,
    4096: 9733406720,
    8192: 2216342585344,
    16384: 567382630203392,
    32768: 1134765260406784,
    65536: 4512412933816832,
    131072: 9024825867633664,
    262144: 18049651768822272,
    524288: 70515108615168,
    1048576: 2491752130560,
    2097152: 567383701868544,
    4194304: 1134765256220672,
    8388608: 2269530512441344,
    16777216: 2256206450263040,
    33554432: 4512412900526080,
    67108864: 9024834391117824,
    134217728: 18051867805491712,
    268435456: 637888545440768,
    536870912: 1135039602493440,
    1073741824: 2269529440784384,
    2147483648: 4539058881568768,
    4294967296: 1128098963916800,
    8589934592: 2256197927833600,
    17179869184: 4514594912477184,
    34359738368: 9592139778506752,
    68719476736: 19184279556981248,
    137438953472: 2339762086609920,
    274877906944: 4538784537380864,
    549755813888: 9077569074761728,
    1099511627776: 562958610993152,
    2199023255552: 1125917221986304,
    4398046511104: 2814792987328512,
    8796093022208: 5629586008178688,
    17592186044416: 11259172008099840,
    35184372088832: 22518341868716544,
    70368744177664: 9007336962655232,
    140737488355328: 18014673925310464,
    281474976710656: 2216338399232,
    562949953421312: 4432676798464,
    1125899906842624: 11064376819712,
    2251799813685248: 22137335185408,
    4503599627370496: 44272556441600,
    9007199254740992: 87995357200384,
    18014398509481984: 35253226045952,
    36028797018963968: 70506452091904,
    72057594037927936: 567382630219776,
    144115188075855872: 1134765260406784,
    288230376151711744: 2832480465846272,
    576460752303423488: 5667157807464448,
    1152921504606846976: 11333774449049600,
    2305843009213693952: 22526811443298304,
    4611686018427387904: 9024825867763712,
    9223372036854775808: 18049651735527936,
}

# fmt: off
rook_magic_numbers = [
    0xa8002c000108020, 0x6c00049b0002001, 0x100200010090040, 0x2480041000800801,
    0x280028004000800, 0x900410008040022, 0x280020001001080, 0x2880002041000080,
    0xa000800080400034, 0x4808020004000, 0x2290802004801000, 0x411000d00100020,
    0x402800800040080, 0xb000401004208, 0x2409000100040200, 0x1002100004082,
    0x22878001e24000, 0x1090810021004010, 0x801030040200012, 0x500808008001000,
    0xa08018014000880, 0x8000808004000200, 0x201008080010200, 0x801020000441091,
    0x800080204005, 0x1040200040100048, 0x120200402082, 0xd14880480100080,
    0x12040280080080, 0x100040080020080, 0x9020010080800200, 0x813241200148449,
    0x491604001800080, 0x100401000402001, 0x4820010021001040, 0x400402202000812,
    0x209009005000802, 0x810800601800400, 0x4301083214000150, 0x204026458e001401,
    0x40204000808000, 0x8001008040010020, 0x8410820820420010, 0x1003001000090020,
    0x804040008008080, 0x12000810020004, 0x1000100200040208, 0x430000a044020001,
    0x280009023410300, 0xe0100040002240, 0x200100401700, 0x2244100408008080,
    0x8000400801980, 0x2000810040200, 0x8010100228810400, 0x2000009044210200,
    0x4080008040102101, 0x40002080411d01, 0x2005524060000901, 0x502001008400422,
    0x489a000810200402, 0x1004400080a13, 0x4000011008020084, 0x26002114058042
]

bishop_magic_numbers = [
    0x40040844404084, 0x2004208a004208, 0x10190041080202, 0x108060845042010,
    0x581104180800210, 0x2112080446200010, 0x1080820820060210, 0x3c0808410220200,
    0x4050404440404, 0x21001420088, 0x24d0080801082102, 0x1020a0a020400,
    0x40308200402, 0x4011002100800, 0x401484104104005, 0x801010402020200,
    0x400210c3880100, 0x404022024108200, 0x810018200204102, 0x4002801a02003,
    0x85040820080400, 0x810102c808880400, 0xe900410884800, 0x8002020480840102,
    0x220200865090201, 0x2010100a02021202, 0x152048408022401, 0x20080002081110,
    0x4001001021004000, 0x800040400a011002, 0xe4004081011002, 0x1c004001012080,
    0x8004200962a00220, 0x8422100208500202, 0x2000402200300c08, 0x8646020080080080,
    0x80020a0200100808, 0x2010004880111000, 0x623000a080011400, 0x42008c0340209202,
    0x209188240001000, 0x400408a884001800, 0x110400a6080400, 0x1840060a44020800,
    0x90080104000041, 0x201011000808101, 0x1a2208080504f080, 0x8012020600211212,
    0x500861011240000, 0x180806108200800, 0x4000020e01040044, 0x300000261044000a,
    0x802241102020002, 0x20906061210001, 0x5a84841004010310, 0x4010801011c04,
    0xa010109502200, 0x4a02012000, 0x500201010098b028, 0x8040002811040900,
    0x28000010020204, 0x6000020202d0240, 0x8918844842082200, 0x401001102902002
]

rook_index_bits = [
    12, 11, 11, 11, 11, 11, 11, 12,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    12, 11, 11, 11, 11, 11, 11, 12
]

bishop_index_bits = [
    6, 5, 5, 5, 5, 5, 5, 6,
    5, 5, 5, 5, 5, 5, 5, 5,
    5, 5, 7, 7, 7, 7, 5, 5,
    5, 5, 7, 9, 9, 7, 5, 5,
    5, 5, 7, 9, 9, 7, 5, 5,
    5, 5, 7, 7, 7, 7, 5, 5,
    5, 5, 5, 5, 5, 5, 5, 5,
    6, 5, 5, 5, 5, 5, 5, 6
]
# fmt: on
