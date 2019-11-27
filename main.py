from Piece import Pawn, King, GoldGeneral, SilverGeneral, Knight, Lance, Rook, \
    Bishop, Piece


class Board:
    def __init__(self):
        self._size = 9
        self._board = [self._king("w"),
                       self._rook_bishop("w"),
                       self._pawns("w"),
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", ],
                       self._pawns("b"),
                       self._rook_bishop("b"),
                       self._king("b")]
        self.white_captured = 0
        self.black_captured = 0

    @staticmethod
    def _pawns(color):
        return [Pawn(color) for _ in range(0, 9)]

    @staticmethod
    def _king(color):
        return [Lance(color), Knight(color), SilverGeneral(color), GoldGeneral(color), King(color), GoldGeneral(color), SilverGeneral(color), Knight(color), Lance(color)]

    @staticmethod
    def _rook_bishop(color):
        return [" ", Rook(color), " ", " ", " ", " ", " ", Bishop(color), " "]

    def print_board(self):
        print("============White==========")
        print(f"Captured: {self.white_captured}")
        print(f"9: ")
        print(" ")
        print(f"   | 0  1  2  3  4  5  6  7  8")
        print(f"--+-----------------------------")

        for i, row in enumerate(self._board):
            print(f"{i} |", end=" ")
            for item in row:
                if isinstance(item, Piece):
                    print(item, end=" ")
                else:
                    print("  ", end=" ")
            print("")
        print(f"9: ")
        print(f"Captured: {self.black_captured}")
        print("============Black==========")

    def check_piece(self, row, col):
        piece = self._board[row][col]
        if not piece:
            print("There is no piece on this position")
            exit()
        return piece

    def check_available_moves(self, piece, to_row, to_col, from_row, from_col):
        icon = piece.icon()
        if(icon == "P"):
        pass

    def check_position(self, piece, row, col, from_row, from_col):
        new_pos = self._board[row][col]
        if new_pos is " ":
            if self.check_available_moves(piece, row, col, from_row, from_col):
                self._board[row][col] = piece
                self._board[from_row][from_col] = " "
        else:
            print("This position already has a piece in")




b = Board()
b.print_board()

turn_count = 0
turn = "White"


while True:
    b.print_board()
    print(f"Turn: #{turn_count} {turn}\n")
    print(f"From which position do you wish to move (row col): ")
    from_row = input()
    from_col = input()
    piece = b.check_piece(int(from_row), int(from_col))
    print(f"Which position do you want to move your piece (row col): ")
    to_row = input()
    to_col = input()
    b.check_position(piece, int(to_row), int(to_col), int(from_row), int(from_col))
    turn = "White" if turn == "Black" else "Black"
    turn_count += 1
    input()
