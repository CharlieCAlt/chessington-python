"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        square = board.find_piece(self)

        if self.player == Player.WHITE:
            change = 1
            start_row = 1
            row_limit = 7
        else:
            change = -1
            start_row = 6
            row_limit = 0

        if square.row == row_limit:
            return []
        else:
            pass

        move_once = Square.at(square.row + (1 * change), square.col)
        move_twice = Square.at(square.row +(2 * change), square.col)
        available = board.get_piece(move_once)
        available_two = board.get_piece(move_twice)
        print(available)

        if square.row == start_row and available == None and available_two == None:
          return [move_once, move_twice]
        elif square.row == start_row and available == None:
            return [move_once]
        elif available == None:
            return [move_once]
        else:
            return []

        # white_move_once = Square.at(square.row + 1, square.col)
        # white_move_twice = Square.at(square.row + 2, square.col)
        # black_move_once = Square.at(square.row -1, square.col)
        # black_move_twice = Square.at(square.row - 2, square.col)

        # if self.player == Player.WHITE:
        #     # if loop where pawn must be at start with nothing 1 or 2 squares infront
        #     if square.row == 1 and available_W == None:
        #         return [white_move_once, white_move_twice]
        #     elif available_W == None:
        #         return [white_move_once]
        #     else:
        #         return []
        # else:
        #     if square.row == 6 and available_B == None:
        #         return [black_move_once, black_move_twice]
        #     elif available_B == None:
        #         return [black_move_once]
        #     else:
        #         return []

    #board.get_piece() This will return none or piece when coordinates are input
    # available = board.get_piece(squareToMoveTo)
    # print(available)
    # if available != none, then there is a piece in the way and cannot move there.


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []