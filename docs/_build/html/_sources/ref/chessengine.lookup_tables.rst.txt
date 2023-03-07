.. _lookup_tables:

chessengine.lookup\_tables
==========================

.. automodule:: chessengine.lookup_tables

.. py:data:: pos_to_coords

    :type: dict[int, str]

    A dictionary mapping position *indices* on the board to their square names. 0 is mapped to "A1", 1
    is mapped to "B1", 8 is mapped to "A2", 9 is mapped to "B2", and so on.


.. py:data:: coords_to_pos

    :type: dict[str, int]

    A dictionary mapping squares on the board to their position *indices*. Basically the reverse mapping
    of ``pos_to_coords``. "A1" is mapped to 0, "B1" is mapped to 1, "A2" is mapped to 8, "B2" is mapped
    to 9, and so on.


.. py:data:: clear_rank

    :type: dict[int, int]

    A dictionary mapping ranks to a bitboard having 0s only on that rank. For example,
    ``clear_rank[1]`` is a bitboard having only 0s on positions on the first rank,
    and 1s on all other positions.


.. py:data:: mask_rank

    :type: dict[int, int]

    A dictionary mapping ranks to a bitboard having 1s only on that rank, and 0s on all
    other ranks. For example, ``mask_rank[1]`` is a bitboard having only 1s on positions
    on the first rank, and 0s on all other position.


.. py:data:: clear_file

    :type: dict[int, int]

    A dictionary mapping files to a bitboard having 0s only on that file, and 1s on all
    other ranks. For example, ``clear_file[1]`` is a bitboard having only 0s on positions
    on the first file, and 1s on all other positions.


.. py:data:: mask_file

    :type: dict[int, int]

    A dictionary mapping files to a bitboard having 1s only on that file, and 0s on all
    other ranks. For example, ``mask_file[1]`` is a bitboard having only 1s on positions
    on the first file, and 0s on all other positions.


.. py:data:: clear_position

    :type: dict[int, int]

    A dictionary mapping *positions* to bitboards with a 0 at that position and 1 at all
    other positions.