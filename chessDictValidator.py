#! python3
# A function that validates the possible number chess pieces

chess_board = {'1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wqueen', '1e': 'wking', '1f': 'wbishop',
               '1g': 'wknight', '1h': 'wrook', '2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn',
               '2e': 'wpawn',
               '2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn', '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '',
               '3g': '', '3h': '', '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
               '5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
               '6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
               '7a': 'bpawn', '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn',
               '7h': 'bpawn',
               '8a': 'brook', '8b': 'bknight', '8c': 'bbishop', '8d': 'bqueen', '8e': 'bking', '8f': 'bbishop',
               '8g': 'bknight', '8h': 'brook'}


def isValidChessBoard(board):
    # Define board and pieces from start of game
    w_pawn = 0
    b_piece = 0
    w_piece = 0
    b_pawn = 0
    colour = ['w', 'b']

    # Check that the correct colours are present
    for i in board.values():
        if i:
            if i[0] == colour[0]:
                w_piece += 1
    print(str(w_piece) + ' white pieces are there')

    for i in board.values():
        if i:
            if i[0] == colour[1]:
                b_piece += 1
    print(str(b_piece) + ' black pieces are there')

    # one black king and one white king
    if 'bking' not in board.values():
        print('KingError')
        return False
    else:
        print('black king is present')
    if 'wking' not in board.values():
        print('KingError')
        return False
    else:
        print('white king is present')

    # check whether there is the right amount of pawns
    for pawn in board.values():
        if pawn == 'wpawn':
            w_pawn += 1
        else:
            pass

        if pawn == 'bpawn':
            b_pawn += 1
        else:
            pass

    # Check that there aren't too many pawns
    if w_pawn == 8:
        print(str(w_pawn) + ' white pawns are present')
    elif w_pawn > 8:
        print('Too many white pawns: ', w_pawn)
        print()
        return False

    if b_pawn == 8:
        print(str(b_pawn) + ' black pawns are present')
        print()

    elif b_pawn > 8:
        print('Too many black pawns')
        print()
        return False

    # check that there are no more than 16 Pieces for white player
    if w_piece > 16:
        print('too many white pieces')
        return False

    # check that there are no more than 16 Pieces for black player
    if b_piece > 16:
        print('too many black pieces')
        return False


isValidChessBoard(chess_board)
