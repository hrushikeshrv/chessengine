Search.setIndex({"docnames": ["api", "chessboard", "index", "playing", "ref/chessengine.bitboard", "ref/chessengine.lookup_tables", "ref/chessengine.moves", "ref/chessengine.pgn.node", "ref/chessengine.pgn.parser", "ref/chessengine.utils", "usage"], "filenames": ["api.rst", "chessboard.rst", "index.rst", "playing.rst", "ref\\chessengine.bitboard.rst", "ref\\chessengine.lookup_tables.rst", "ref\\chessengine.moves.rst", "ref\\chessengine.pgn.node.rst", "ref\\chessengine.pgn.parser.rst", "ref\\chessengine.utils.rst", "usage.rst"], "titles": ["API Reference", "Internal Board Representation", "Welcome to chessengine\u2019s documentation!", "Playing A Game", "chessengine.bitboard", "chessengine.lookup_tables", "chessengine.moves", "chessengine.pgn.node", "chessengine.pgn.parser", "chessengine.utils", "Usage &amp; Installation"], "terms": {"A": [1, 2, 4, 7, 8], "chess": [1, 2, 4], "engin": 2, "written": 2, "python": 2, "depend": 2, "thi": [2, 4], "project": 2, "i": [1, 2, 4, 8, 9], "under": 2, "activ": 2, "develop": 2, "index": 2, "modul": 2, "search": [2, 4], "page": 2, "us": [1, 2, 4, 7], "pip": 2, "code": [], "block": [], "consol": [], "venv": [], "intern": [2, 4], "bitboard": [0, 1, 2, 5, 9], "represent": [2, 4], "alpha": [2, 4], "beta": [2, 4], "prune": [2, 4], "move": [0, 2, 4, 7], "gener": 2, "api": 2, "open": [2, 7], "book": [2, 7], "pgn": [0, 2], "pars": [2, 7, 8], "start": [2, 4, 6], "game": [2, 4, 7], "m": 2, "plai": [2, 4], "class": [1, 4, 7, 8], "lookup": 5, "tabl": 5, "ar": [4, 5], "allow": 5, "u": 5, "mask": 5, "clear": [5, 9], "specif": 5, "rank": [5, 9], "file": [5, 8, 9], "posit": [1, 4, 5, 6, 9], "chessboard": [4, 5], "function": 4, "lookup_t": [0, 2], "util": [0, 2], "node": [0, 2], "parser": [0, 2], "complet": 4, "all": [1, 4, 8, 9], "method": 4, "need": 4, "support": [], "piec": [1, 4], "scenario": [], "defin": [1, 4], "gamenod": [7, 8], "creat": 4, "The": [1, 4], "common": [], "oper": [], "chessengin": [0, 1], "repres": [1, 4, 7], "board": [2, 4, 6, 9], "refer": [2, 4], "side": [1, 4, 6], "str": [4, 6, 7, 8], "implement": 4, "particular": 4, "can": [4, 6], "access": 4, "via": 4, "get_bitboard": 4, "an": 4, "attribut": [1, 4], "name": [1, 4], "_": [1, 4], "": [1, 4], "For": [2, 4], "exampl": 4, "white_pawn": 4, "white_queen": 4, "black_k": 4, "black_rook": 4, "alpha_beta_search": 4, "depth": 4, "int": [4, 6, 9], "4": 4, "1000": [4, 9], "maximizing_play": 4, "bool": [4, 6, 9], "true": [4, 9], "execut": 4, "you": [2, 4], "probabl": 4, "won": 4, "t": 4, "call": 4, "yourself": 4, "search_forward": 4, "instead": 4, "argument": 4, "number": 4, "pli": 4, "forward": 4, "default": 4, "minimum": 4, "score": 4, "maxim": 4, "player": 4, "guarante": 4, "specifi": 4, "maximum": 4, "minim": 4, "white": [4, 6], "fals": [4, 6, 9], "black": [4, 6], "return": [4, 6, 9], "valu": 4, "best": 4, "found": 4, "copi": 4, "self": [4, 8], "pass": 4, "king": [4, 6], "so": 4, "rais": 4, "attributeerror": 4, "invalid": 4, "request": 4, "see": [2, 4], "abov": 4, "convent": [1, 4], "get_mov": 4, "option": [4, 8], "none": [4, 8], "list": [4, 6, 8, 9], "tupl": [4, 6], "get": 4, "end": [4, 6], "reach": [4, 6, 7], "from": 4, "alwai": 4, "requir": 4, "If": 4, "e": [4, 9], "valid": 4, "rook": [4, 6], "where": 4, "get_self_piece_bitboard": 4, "correspond": [1, 4], "consid": 4, "own": 4, "etc": 4, "one": [1, 4], "queen": [4, 6], "bishop": [4, 6], "knight": [4, 6], "pawn": [4, 6], "get_side_bitboard": 4, "contain": 4, "given": [4, 8], "identify_piece_at": 4, "identifi": 4, "ani": 4, "power": [4, 9], "2": [4, 9], "3": 4, "format": 4, "g": 4, "type": [4, 6, 9], "black_bishop": 4, "present": [1, 4], "make_mov": 4, "track": [4, 7], "doesn": 4, "check": 4, "anyth": 4, "just": [1, 4], "make": 4, "unless": 4, "both": 4, "store": [1, 4], "undo": 4, "later": 4, "move_san": 4, "standard": 4, "algebra": 4, "notat": 4, "san": 4, "search_depth": 4, "loop": [2, 4], "first": 4, "find": 4, "optim": 4, "current": 4, "state": 4, "1": [1, 4, 9], "set_bitboard": 4, "set": [4, 9], "undo_mov": 4, "last": 4, "update_board_st": 4, "updat": 4, "when": 4, "made": [4, 7], "chang": 4, "wai": 4, "should": 4, "manual": 4, "otherwis": [4, 8], "automat": 4, "paramet": [4, 6, 7, 8, 9], "__eq__": 4, "other": 4, "__hash__": 4, "hash": 4, "fen": 4, "becaus": 4, "faster": 4, "easier": 4, "maintain": 4, "than": 4, "__init__": 4, "__repr__": 4, "repr": 4, "__str__": 4, "__weakref__": 4, "weak": 4, "object": [4, 8], "check_valid_posit": [], "auto_add": [], "indic": [], "whether": [], "second": [], "direct": [], "try": [], "explor": [], "next": [], "being": [], "add": [], "get_rook_mov": 6, "get_white_rook_mov": 6, "get_black_rook_mov": 6, "get_bishop_mov": 6, "get_white_bishop_mov": 6, "get_black_bishop_mov": 6, "get_knight_mov": 6, "get_white_knight_mov": 6, "get_black_knight_mov": 6, "get_king_mov": 6, "get_white_king_mov": 6, "get_black_king_mov": 6, "get_white_queen_mov": 6, "get_black_queen_mov": 6, "get_white_pawn_mov": 6, "allow_en_pass": 6, "get_black_pawn_mov": 6, "summari": 2, "get_bit_posit": 9, "which": [1, 9], "have": 9, "1001100": 9, "100": 9, "1000000": 9, "get_fil": 9, "log": 9, "either": 9, "ha": [1, 9], "rang": 9, "8": 9, "get_rank": 9, "lsb_po": 9, "rightmost": 9, "bit": [1, 9], "0000100": 9, "1010100": 9, "root_nod": 7, "keep": 7, "throughout": 7, "result": 7, "record": 7, "replai": 7, "turn": 7, "build": 7, "tree": [7, 8], "pgnparser": 8, "pgn_file": 8, "construct": 8, "param": [], "path": 8, "string": 8, "like": 8, "read": 4, "know": 4, "how": 4, "avail": 4, "It": [1, 4], "also": [1, 4], "detail": [2, 4], "differ": 4, "them": 4, "ref": [], "64": 1, "integ": 1, "each": 1, "squar": 1, "sinc": 1, "certain": 1, "mean": 1, "0": 1, "mai": 2, "run": 2, "bug": 2, "especi": 2, "instruct": 2, "local": 2}, "objects": {"chessengine": [[4, 0, 0, "-", "bitboard"], [5, 0, 0, "-", "lookup_tables"]], "chessengine.bitboard": [[4, 1, 1, "", "Board"]], "chessengine.bitboard.Board": [[4, 2, 1, "", "__eq__"], [4, 2, 1, "", "__hash__"], [4, 2, 1, "", "__init__"], [4, 2, 1, "", "__repr__"], [4, 2, 1, "", "__str__"], [4, 3, 1, "", "__weakref__"], [4, 2, 1, "", "alpha_beta_search"], [4, 2, 1, "", "copy"], [4, 2, 1, "", "get_bitboard"], [4, 2, 1, "", "get_moves"], [4, 2, 1, "", "get_self_piece_bitboard"], [4, 2, 1, "", "get_side_bitboard"], [4, 2, 1, "", "identify_piece_at"], [4, 2, 1, "", "make_moves"], [4, 2, 1, "", "move"], [4, 2, 1, "", "move_san"], [4, 2, 1, "", "play"], [4, 2, 1, "", "search_forward"], [4, 2, 1, "", "set_bitboard"], [4, 2, 1, "", "undo_move"], [4, 2, 1, "", "update_board_state"]], "chessengine.moves": [[6, 4, 1, "", "get_bishop_moves"], [6, 4, 1, "", "get_black_bishop_moves"], [6, 4, 1, "", "get_black_king_moves"], [6, 4, 1, "", "get_black_knight_moves"], [6, 4, 1, "", "get_black_pawn_moves"], [6, 4, 1, "", "get_black_queen_moves"], [6, 4, 1, "", "get_black_rook_moves"], [6, 4, 1, "", "get_king_moves"], [6, 4, 1, "", "get_knight_moves"], [6, 4, 1, "", "get_rook_moves"], [6, 4, 1, "", "get_white_bishop_moves"], [6, 4, 1, "", "get_white_king_moves"], [6, 4, 1, "", "get_white_knight_moves"], [6, 4, 1, "", "get_white_pawn_moves"], [6, 4, 1, "", "get_white_queen_moves"], [6, 4, 1, "", "get_white_rook_moves"]], "chessengine.pgn.node": [[7, 1, 1, "", "Game"], [7, 1, 1, "", "GameNode"]], "chessengine.pgn.parser": [[8, 1, 1, "", "PGNParser"]], "chessengine.pgn.parser.PGNParser": [[8, 2, 1, "", "parse"]], "chessengine.utils": [[9, 4, 1, "", "get_bit_positions"], [9, 4, 1, "", "get_file"], [9, 4, 1, "", "get_rank"], [9, 4, 1, "", "lsb_pos"]]}, "objtypes": {"0": "py:module", "1": "py:class", "2": "py:method", "3": "py:attribute", "4": "py:function"}, "objnames": {"0": ["py", "module", "Python module"], "1": ["py", "class", "Python class"], "2": ["py", "method", "Python method"], "3": ["py", "attribute", "Python attribute"], "4": ["py", "function", "Python function"]}, "titleterms": {"welcom": 2, "chessengin": [2, 4, 5, 6, 7, 8, 9], "": 2, "document": 2, "indic": 2, "tabl": 2, "usag": [2, 10], "instal": [2, 10], "featur": 2, "api": 0, "content": 2, "bitboard": 4, "lookup_t": 5, "move": 6, "util": 9, "pgn": [7, 8], "node": 7, "parser": 8, "intern": 1, "chess": [], "board": 1, "represent": 1, "refer": 0, "summari": 0, "Of": 2, "plai": 3, "A": 3, "game": 3, "local": 10, "For": 10, "develop": 10}, "envversion": {"sphinx.domains.c": 2, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 6, "sphinx.domains.index": 1, "sphinx.domains.javascript": 2, "sphinx.domains.math": 2, "sphinx.domains.python": 3, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx": 56}})