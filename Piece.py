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

    def __repr__(self):
        return f"{self._icon}{self._color}"


class Pawn(Piece):
    def __init__(self, color):
        super().__init__("P", color)

    def available_positions(self, color, from_row, to_row):
        if color == "b":
            if to_row == (from_row+1):
                return True


class King(Piece):
    def __init__(self, color):
        super().__init__("K", color)


class Knight(Piece):
    def __init__(self, color):
        super().__init__("N", color)


class Rook(Piece):
    def __init__(self, color):
        super().__init__("R", color)


class GoldGeneral(Piece):
    def __init__(self, color):
        super().__init__("G", color)


class SilverGeneral(Piece):
    def __init__(self, color):
        super().__init__("S", color)


class Lance(Piece):
    def __init__(self, color):
        super().__init__("L", color)


class Bishop(Piece):
    def __init__(self, color):
        super().__init__("B", color)
