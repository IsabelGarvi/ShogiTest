from abc import abstractmethod


class Piece:
    def __init__(self, icon, color):
        self._icon = icon
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def icon(self):
        return self._icon

    @abstractmethod
    def available_positions(self, color, from_row=None, to_row=None, from_col=None, to_col=None):
        """Check if a piece can make that move.
        Args:
            color: color of the piece
            from_row: row from where the piece wants to move
            to_row: row to where the piece wants to move
            from_col: column from where the piece wants to move
            to_col: column to where the piece wants to move

        Returns:
            Whether the piece can make the move.
        """
        ...

    def __repr__(self):
        return f"{self._icon}{self._color}"


class Pawn(Piece):
    def __init__(self, color):
        super().__init__("P", color)

    def available_positions(self, color, from_row=None, to_row=None, from_col=None, to_col=None) -> bool:
        if color == "b":
            if to_row == (from_row-1) and to_col == from_col:
                return True
            return False
        else:
            if to_row == (from_row+1) and to_col == from_col:
                return True
            return False


class King(Piece):
    def __init__(self, color):
        super().__init__("K", color)

    def available_positions(self, color, from_row=None, to_row=None,
                            from_col=None, to_col=None) -> bool:
        if (to_row  == from_row+1 or to_row == from_row-1) and (to_col == from_col+1 or to_col == from_col-1):
            return True
        elif to_row == from_row+1 or to_row == from_row-1 or to_col == from_col+1 or to_col == from_col-1:
            return True
        elif to_row == (from_row-1):
            return True
        else:
            return False


class Knight(Piece):
    def __init__(self, color):
        super().__init__("N", color)

    def available_positions(self, color, from_row=None, to_row=None,
                            from_col=None, to_col=None) -> bool:
        if color == "b":
            if to_row == (from_row-2) and (to_col == from_col+1 or to_col == from_col-1):
                return True
            return False
        else:
            if to_row == (from_row+2) and (to_col == from_col+1 or to_col == from_col-1):
                return True
            return False


class Rook(Piece):
    def __init__(self, color):
        super().__init__("R", color)

    def available_positions(self, color, from_row=None, to_row=None,
                            from_col=None, to_col=None) -> bool:
        if (to_row > from_row or to_row < from_row) and to_col == from_col:
            return True
        elif (to_col > from_col or to_col < from_col) and to_row == from_row:
            return True
        else:
            return False


class GoldGeneral(Piece):
    def __init__(self, color):
        super().__init__("G", color)

    def available_positions(self, color, from_row=None, to_row=None,
                            from_col=None, to_col=None) -> bool:
        if color == "b":
            if to_row == (from_row-1) and (to_col == from_col+1 or to_col == from_col-1):
                return True
            elif to_row == from_row-1 or to_row == from_row+1 or to_col == from_col+1 or to_col == from_col-1:
                return True
            else:
                return False
        else:
            if to_row == (from_row+1) and (to_col == from_col+1 or to_col == from_col-1):
                return True
            elif to_row == from_row-1 or to_row == from_row+1 or to_col == from_col+1 or to_col == from_col-1:
                return True
            else:
                return False


class SilverGeneral(Piece):
    def __init__(self, color):
        super().__init__("S", color)

    def available_positions(self, color, from_row=None, to_row=None,
                            from_col=None, to_col=None) -> bool:
        if color == "b":
            if (to_row == from_row-1 or to_row == from_row+1) and (to_col == from_col+1 or to_col == from_col-1):
                return True
            elif to_row == from_row-1:
                return True
            else:
                return False
        else:
            if (to_row == from_row - 1 or to_row == from_row + 1) and (
                    to_col == from_col + 1 or to_col == from_col - 1):
                return True
            elif to_row == from_row+1:
                return True
            else:
                return False


class Lance(Piece):
    def __init__(self, color):
        super().__init__("L", color)

    def available_positions(self, color, from_row=None, to_row=None,
                            from_col=None, to_col=None) -> bool:
        if color == "b":
            if to_col == from_col and to_row < from_row:
                return True
            return False
        else:
            if to_col == from_col and to_row > from_row:
                return True
            return False


class Bishop(Piece):
    def __init__(self, color):
        super().__init__("B", color)

    def available_positions(self, color, from_row=None, to_row=None,
                            from_col=None, to_col=None) -> bool:
        if to_row > from_row and to_col > from_col:
            return True
        elif to_row < from_row and to_col > from_col:
            return True
        elif to_row < from_row and to_col < from_col:
            return True
        elif to_row > from_row and to_col < from_col:
            return True
        else:
            return False
