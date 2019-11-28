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
        self.white_captured = []
        self.black_captured = []

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
        print(" ")
        print(f"9: ")
        print(f"Captured: {self.black_captured}")
        print("============Black==========")

    def check_piece(self, move_from_row, move_from_col):
        piece_selected = self._board[move_from_row][move_from_col]
        if piece_selected is " ":
            raise Exception("There is no piece on this position")
        elif piece_selected.color is not turn:
            raise Exception("Please choose a piece of your color")
        return piece_selected

    def check_available_moves(self, piece_to_move, move_to_row, move_to_col,
                              move_from_row, move_from_col):
        icon = piece_to_move.icon
        result = False
        if icon == "P":
            result = piece_to_move.available_positions(piece.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        elif icon == "K":
            result = piece_to_move.available_positions(piece.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        elif icon == "N":
            result = piece_to_move.available_positions(piece.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        elif icon == "G":
            result = piece_to_move.available_positions(piece.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        elif icon == "S":
            result = piece_to_move.available_positions(piece.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        elif icon == "L":
            if piece_to_move.color == "w":
                for i in range(move_from_row+1, move_to_row+1):
                    print(self._board[i][move_to_col])
                    if self._board[i][move_to_col] is not " ":
                        return result
            else:
                for i in range(move_to_row, move_from_row-1):
                    print(self._board[i][move_to_col])
                    if self._board[i][move_to_col] == " ":
                        return result

            result = piece_to_move.available_positions(piece.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        elif icon == "R":
            if move_to_col is move_from_col:
                if move_to_row > move_from_row:
                    for i in range(move_from_row+1, move_to_row+1):
                        if self._board[i][move_to_col] is not " ":
                            if self._board[i][move_to_col].color is piece_to_move.color:
                                return result
                else:
                    for i in range(move_from_row-1, move_to_row-1, -1):
                        print(self._board[i][move_to_col])
                        if self._board[i][move_to_col] is not " ":
                            if self._board[i][move_to_col].color is piece_to_move.color:
                                return result
            elif move_to_row is move_from_row:
                if move_to_col > move_from_col:
                    for i in range(move_from_col+1, move_to_col+1):
                        if self._board[move_to_row][i] is not " ":
                            if self._board[move_to_row][i].color is piece_to_move.color:
                                return result
                else:
                    for i in range(move_from_col-1, move_to_col-1):
                        if self._board[move_to_row][i] is not " ":
                            if self._board[move_to_row][i].color is piece_to_move.color:
                                return result

            result = piece_to_move.available_positions(piece.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        elif icon == "B":
            if to_row < from_row and to_col > from_col:
                for i in range(move_from_col+1, move_to_col+1):
                    for j in range(move_from_row+1, move_to_row+1):
                        if self._board[j][i] is not " ":
                            if self._board[j][i].color is piece_to_move.color:
                                return result
            elif to_row > from_row and to_col > from_col:
                for i in range(move_from_col+1, move_to_col+1):
                    for j in range(move_from_row-1, move_to_row-1, -1):
                        if self._board[j][i] is not " ":
                            if self._board[j][i].color is piece_to_move.color:
                                return result
            elif to_row > from_row and to_col < from_col:
                for i in range(move_from_col-1, move_to_col-1, -1):
                    for j in range(move_from_row+1, move_to_row+1):
                        if self._board[j][i] is not " ":
                            if self._board[j][i].color is piece_to_move.color:
                                return result
            elif to_row < from_row and to_col < from_col:
                for i in range(move_from_col-1, move_to_col-1, -1):
                    for j in range(move_from_row-1, move_to_row-1, -1):
                        if self._board[j][i] is not " ":
                            if self._board[j][i].color is piece_to_move.color:
                                return result

            result = piece_to_move.available_positions(piece.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        return result

    def capture_piece(self, piece_to_move, move_to_row, move_to_col):
        if piece_to_move.color == "w":
            self.white_captured.append(self._board[move_to_row][move_to_col])
        else:
            self.black_captured.append(self._board[move_to_row][move_to_col])

    def move_piece(self, piece_to_move, move_to_row, move_to_col, move_from_row, move_from_col):
        new_pos = self._board[move_to_row][move_to_col]
        able_to_move = self.check_available_moves(piece_to_move, move_to_row, move_to_col, move_from_row, move_from_col)
        if new_pos is " ":
            if able_to_move:
                self._board[move_to_row][move_to_col] = piece_to_move
                self._board[move_from_row][move_from_col] = " "
            else:
                raise Exception("This movement can not be done.")
        elif new_pos != " " and new_pos.color is not piece_to_move.color:
            if able_to_move:
                self.capture_piece(piece_to_move, move_to_row, move_to_col)
                self._board[move_to_row][move_to_col] = piece_to_move
                self._board[move_from_row][move_from_col] = " "
            else:
                raise Exception("This movement can not be done.")
        else:
            raise Exception("This position already has a piece of your color in")


b = Board()
b.print_board()

turn_count = 0
turn = "w"


while True:
    b.print_board()
    print(f"Turn: #{turn_count} {turn}\n")
    print(f"Which piece do you wish to move (row col): ")
    from_row = input()
    from_col = input()
    try:
        piece = b.check_piece(int(from_row), int(from_col))
        print(f"Where do you want to move your piece (row col): ")
        to_row = input()
        to_col = input()

        b.move_piece(piece, int(to_row), int(to_col), int(from_row), int(from_col))
        turn = "w" if turn == "b" else "b"
        turn_count += 1
    except Exception as e:
        print(f"\033[91m{e}\033[00m")
        print(f"Click enter to choose again.")
        input()
        continue
