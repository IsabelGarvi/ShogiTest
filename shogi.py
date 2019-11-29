from typing import Sequence

import inquirer as inquirer

from Piece import Pawn, King, GoldGeneral, SilverGeneral, Knight, Lance, Rook, \
    Bishop, Piece


class Board:
    def __init__(self):
        """Initializes the board with the pieces placed.
        """
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
    def _pawns(color) -> Sequence:
        return [Pawn(color) for _ in range(0, 9)]

    @staticmethod
    def _king(color) -> Sequence:
        return [Lance(color), Knight(color), SilverGeneral(color), GoldGeneral(color), King(color), GoldGeneral(color), SilverGeneral(color), Knight(color), Lance(color)]

    @staticmethod
    def _rook_bishop(color) -> Sequence:
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
        """Checks if there is the piece in the selected position has a piece
        and if there is one in it, check if it's the same color as the player.

        Args:
            move_from_row: row from where the player wants to move the piece.
            move_from_col: column from where the player wants to move the piece.

        Returns:
            The selected piece.
        """
        piece_selected = self._board[move_from_row][move_from_col]
        if piece_selected is " ":
            raise Exception("There is no piece on this position")
        elif piece_selected.color is not turn:
            raise Exception("Please choose a piece of your color")
        return piece_selected

    def check_available_moves(self, piece_to_move, move_to_row, move_to_col,
                              move_from_row, move_from_col):
        """Checks whether the selected piece can be moved to the desired
        position.

        Args:
            piece_to_move: piece the player wants to move.
            move_to_row: row where the player wants to move the piece to.
            move_to_col: column where the player wants to move the piece to.
            move_from_row: row from where the player wants to move the piece.
            move_from_col: column from where the player wants to move the piece.
        """
        icon = piece_to_move.icon
        result = False
        if icon == "P":
            self.check_promotion(piece_to_move, move_to_row)
            result = piece_to_move.available_positions(piece_to_move.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        elif icon == "K":
            result = piece_to_move.available_positions(piece_to_move.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        elif icon == "N":
            self.check_promotion(piece_to_move, move_to_row)
            result = piece_to_move.available_positions(piece_to_move.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        elif icon == "G":
            result = piece_to_move.available_positions(piece_to_move.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        elif icon == "S":
            self.check_promotion(piece_to_move, move_to_row)
            result = piece_to_move.available_positions(piece_to_move.color,
                                                       to_row=move_to_row,
                                                       from_row=move_from_row,
                                                       to_col=move_to_col,
                                                       from_col=move_from_col)
        elif icon == "L":
            self.check_promotion(piece_to_move, move_to_row)
            if to_col is not from_col:
                return False
            else:
                if piece_to_move.color == "w":
                    if move_to_row < move_from_row:
                        return False
                    for i in range(move_from_row+1, move_to_row+1):
                        if self._board[i][move_to_col] is not " ":
                            if self._board[i][move_to_col] is not piece_to_move.color:
                                move_to_row = i
                                return True, move_to_row, move_to_col
                            else:
                                raise Exception(f"There's a piece of your color in the way -> {self._board[i][move_to_col]}")
                else:
                    if move_to_row > move_from_row:
                        return False
                    for i in range(move_to_row, move_from_row-1):
                        if self._board[i][move_to_col] == " ":
                            if self._board[i][move_to_col] is not piece_to_move.color:
                                move_to_row = i
                                return True, move_to_row, move_to_col
                            else:
                                raise Exception(f"There's a piece of your color in the way -> {self._board[i][move_to_col]}")

        elif icon == "R":
            self.check_promotion(piece_to_move, move_to_row)
            if move_to_col is move_from_col:
                if move_to_row > move_from_row:
                    for i in range(move_from_row+1, move_to_row+1):
                        if self._board[i][move_to_col] is not " ":
                            if self._board[i][move_to_col].color is piece_to_move.color:
                                raise Exception(f"There's a piece of your color in the way -> {self._board[i][move_to_col]}")
                            else:
                                move_to_row = i
                                return True, move_to_row, move_to_col
                        else:
                            return True, move_to_row, move_to_col
                else:
                    for i in range(move_from_row-1, move_to_row-1, -1):
                        print(self._board[i][move_to_col])
                        if self._board[i][move_to_col] is not " ":
                            if self._board[i][move_to_col].color is piece_to_move.color:
                                raise Exception(f"There's a piece of your color in the way -> {self._board[i][move_to_col]}")
                            else:
                                move_to_row = i
                                return True, move_to_row, move_to_col
                        else:
                            return True, move_to_row, move_to_col
            elif move_to_row is move_from_row:
                if move_to_col > move_from_col:
                    for i in range(move_from_col+1, move_to_col+1):
                        if self._board[move_to_row][i] is not " ":
                            if self._board[move_to_row][i].color is piece_to_move.color:
                                raise Exception(f"There's a piece of your color in the way -> {self._board[move_to_row][i]}")
                            else:
                                move_to_col = i
                                return True, move_to_row, move_to_col
                        else:
                            return True, move_to_row, move_to_col
                else:
                    for i in range(move_from_col-1, move_to_col-1, -1):
                        if self._board[move_to_row][i] is not " ":
                            if self._board[move_to_row][i].color is piece_to_move.color:
                                raise Exception(f"There's a piece of your color in the way -> {self._board[move_to_row][i]}")
                            else:
                                move_to_col = i
                                return True, move_to_row, move_to_col
                        else:
                            return True, move_to_row, move_to_col
            else:
                return False
        elif icon == "B":
            self.check_promotion(piece_to_move, move_to_row)
            if to_row < from_row and to_col > from_col:
                for i, j in zip(range(move_from_col+1, move_to_col+1), range(move_from_row-1, move_to_row-1, -1)):
                    if self._board[j][i] is not " ":
                        if self._board[j][i].color is piece_to_move.color:
                            raise Exception(f"There's a piece of your color in the way -> {self._board[j][i]}")
                        else:
                            move_to_col = i
                            move_to_row = j
                            return True, move_to_row, move_to_col
                    else:
                        return True, move_to_row, move_to_col
            elif to_row > from_row and to_col > from_col:
                for i, j in zip(range(move_from_col+1, move_to_col+1), range(move_from_row+1, move_to_row+1)):
                    if self._board[j][i] is not " ":
                        if self._board[j][i].color is piece_to_move.color:
                            raise Exception(f"There's a piece of your color in the way -> {self._board[j][i]}")
                        else:
                            move_to_col = i
                            move_to_row = j
                            return True, move_to_row, move_to_col
                    else:
                        return True, move_to_row, move_to_col
            elif to_row > from_row and to_col < from_col:
                for i, j in zip(range(move_from_col-1, move_to_col-1, -1), range(move_from_row+1, move_to_row+1)):
                    print(f"Checking: {j} {i}")
                    if self._board[j][i] is not " ":
                        if self._board[j][i].color is piece_to_move.color:
                            raise Exception(
                                f"There's a piece of your color in the way -> {self._board[j][i]}")
                        else:
                            move_to_col = i
                            move_to_row = j
                            return True, move_to_row, move_to_col
                    else:
                        return True, move_to_row, move_to_col
            elif to_row < from_row and to_col < from_col:
                for i, j in zip(range(move_from_col-1, move_to_col-1, -1), range(move_from_row-1, move_to_row-1, -1)):
                    if self._board[j][i] is not " ":
                        if self._board[j][i].color is piece_to_move.color:
                            raise Exception(f"There's a piece of your color in the way -> {self._board[j][i]}")
                        else:
                            move_to_col = i
                            move_to_row = j
                            return True, move_to_row, move_to_col
                    else:
                        return True, move_to_row, move_to_col
            else:
                return False
        elif icon == "+B":
            if move_to_row == move_from_row+1 or move_to_row == move_from_row-1 or move_to_col == move_from_col+1 or move_to_col == move_from_col-1:
                return True, move_to_row, move_to_col
            elif to_row < from_row and to_col > from_col:
                for i, j in zip(range(move_from_col+1, move_to_col+1), range(move_from_row+1, move_to_row+1)):
                    if self._board[j][i] is not " ":
                        if self._board[j][i].color is piece_to_move.color:
                            raise Exception(f"There's a piece of your color in the way -> {self._board[j][i]}")
                        else:
                            move_to_col = i
                            move_to_row = j
                            return True, move_to_row, move_to_col
                    else:
                        return True, move_to_row, move_to_col
            elif to_row > from_row and to_col > from_col:
                for i, j in zip(range(move_from_col+1, move_to_col+1), range(move_from_row-1, move_to_row-1, -1)):
                    if self._board[j][i] is not " ":
                        if self._board[j][i].color is piece_to_move.color:
                            raise Exception(f"There's a piece of your color in the way -> {self._board[j][i]}")
                        else:
                            move_to_col = i
                            move_to_row = j
                            return True, move_to_row, move_to_col
                    else:
                        return True, move_to_row, move_to_col
            elif to_row > from_row and to_col < from_col:
                for i, j in zip(range(move_from_col-1, move_to_col-1, -1), range(move_from_row+1, move_to_row+1)):
                    print(f"Checking: {j} {i}")
                    if self._board[j][i] is not " ":
                        if self._board[j][i].color is piece_to_move.color:
                            raise Exception(
                                f"There's a piece of your color in the way -> {self._board[j][i]}")
                        else:
                            move_to_col = i
                            move_to_row = j
                            return True, move_to_row, move_to_col
                    else:
                        return True, move_to_row, move_to_col
            elif to_row < from_row and to_col < from_col:
                for i, j in zip(range(move_from_col-1, move_to_col-1, -1), range(move_from_row-1, move_to_row-1, -1)):
                    if self._board[j][i] is not " ":
                        if self._board[j][i].color is piece_to_move.color:
                            raise Exception(f"There's a piece of your color in the way -> {self._board[j][i]}")
                        else:
                            move_to_col = i
                            move_to_row = j
                            return True, move_to_row, move_to_col
                    else:
                        return True, move_to_row, move_to_col
            else:
                return False
        elif icon == "+R":
            if (move_to_row == move_from_row + 1 or move_to_row == move_from_row - 1) and (
                    move_to_col == move_from_col + 1 or move_to_col == move_from_col - 1):
                return True, move_to_row, move_to_col
            elif move_to_col is move_from_col:
                if move_to_row > move_from_row:
                    for i in range(move_from_row+1, move_to_row+1):
                        if self._board[i][move_to_col] is not " ":
                            if self._board[i][move_to_col].color is piece_to_move.color:
                                raise Exception(f"There's a piece of your color in the way -> {self._board[i][move_to_col]}")
                            else:
                                move_to_row = i
                                return True, move_to_row, move_to_col
                        else:
                            return True, move_to_row, move_to_col
                else:
                    for i in range(move_from_row-1, move_to_row-1, -1):
                        print(self._board[i][move_to_col])
                        if self._board[i][move_to_col] is not " ":
                            if self._board[i][move_to_col].color is piece_to_move.color:
                                raise Exception(f"There's a piece of your color in the way -> {self._board[i][move_to_col]}")
                            else:
                                move_to_row = i
                                return True, move_to_row, move_to_col
                        else:
                            return True, move_to_row, move_to_col
            elif move_to_row is move_from_row:
                if move_to_col > move_from_col:
                    for i in range(move_from_col+1, move_to_col+1):
                        if self._board[move_to_row][i] is not " ":
                            if self._board[move_to_row][i].color is piece_to_move.color:
                                raise Exception(f"There's a piece of your color in the way -> {self._board[move_to_row][i]}")
                            else:
                                move_to_col = i
                                return True, move_to_row, move_to_col
                        else:
                            return True
                else:
                    for i in range(move_from_col-1, move_to_col-1, -1):
                        if self._board[move_to_row][i] is not " ":
                            if self._board[move_to_row][i].color is piece_to_move.color:
                                raise Exception(f"There's a piece of your color in the way -> {self._board[move_to_row][i]}")
                            else:
                                move_to_col = i
                                return True, move_to_row, move_to_col
                        else:
                            return True, move_to_row, move_to_col
            else:
                return False
        elif icon == "+P" or icon == "+N" or icon == "+L" or icon == "+S":
            result = piece_to_move.promoted_movement(piece_to_move.color,
                                                     to_row=move_to_row,
                                                     from_row=move_from_row,
                                                     to_col=move_to_col,
                                                     from_col=move_from_col)

        return result, move_to_row, move_to_col

    @staticmethod
    def check_promotion(piece_to_move, move_to_row) -> None:
        """Checks if a piece can be promoted and if it can, it promotes it.

        Args:
            piece_to_move: piece up for promotion.
            move_to_row: row to check.
        """
        if piece_to_move.color == "w":
            if move_to_row > 6:
                piece_to_move.promote()
        else:
            if move_to_row < 3:
                piece_to_move.promote()

    def capture_piece(self, piece_to_move, move_to_row, move_to_col) -> None:
        """Adds the rival piece to the captured list of the turn in play.

        Args:
            piece_to_move: piece the player wants to move.
            move_to_row: row where the rival piece is.
            move_to_col: column where the rival piece is.
        """
        if piece_to_move.color == "w":
            self.white_captured.append(self._board[move_to_row][move_to_col])
        else:
            self.black_captured.append(self._board[move_to_row][move_to_col])

    def move_piece(self, piece_to_move, move_to_row, move_to_col, move_from_row, move_from_col) -> None:
        """Gets the new position on the boards, checks if the selected piece
        can be moved to it and if it can, it moves it.

        Args:
            piece_to_move: piece the player wants to move.
            move_to_row: row where the player wants to move the piece to.
            move_to_col: column where the player wants to move the piece to.
            move_from_row: row from where the player wants to move the piece.
            move_from_col: column from where the player wants to move the piece.
        """
        new_pos = self._board[move_to_row][move_to_col]
        able_to_move, move_to_row, move_to_col = self.check_available_moves(piece_to_move, move_to_row, move_to_col, move_from_row, move_from_col)
        if new_pos is " ":
            if able_to_move:
                self._board[move_to_row][move_to_col] = piece_to_move
                self._board[move_from_row][move_from_col] = " "
            else:
                raise Exception("This movement can not be done.")
        elif new_pos is not " " and new_pos.color is not piece_to_move.color:
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
    """Prints board and allows to play changing turn if no exception is thrown.
    """
    b.print_board()
    print(f"Turn: #{turn_count} {turn}\n")
    if turn == "w":
        if not b.white_captured:
            print(f"Which piece do you wish to move: ")
            from_row = int(input("Row: "))
            from_col = int(input("Column: "))
            try:
                piece = b.check_piece(from_row, from_col)
                print(f"Where do you want to move your piece (row col): ")
                to_row = int(input("Row: "))
                to_col = int(input("Column: "))

                b.move_piece(piece, to_row, to_col, from_row, from_col)
                turn = "w" if turn == "b" else "b"
                turn_count += 1
            except Exception as e:
                print(f"\033[91m{e}\033[00m")
                print(f"\033[91mClick enter to choose again.\033[00m")
                input()
                continue
        else:
            question = [inquirer.List("action", "What do you want to do?",
                                      ["Move a piece",
                                       "Drop a captured piece"])]
            answer = inquirer.prompt(question)["action"]

            if answer == "Move a piece":
                print(f"Which piece do you wish to move: ")
                from_row = int(input("Row: "))
                from_col = int(input("Column: "))
                try:
                    piece = b.check_piece(from_row, from_col)
                    print(f"Where do you want to move your piece (row col): ")
                    to_row = int(input("Row: "))
                    to_col = int(input("Column: "))

                    b.move_piece(piece, to_row, to_col, from_row, from_col)
                    turn = "w" if turn == "b" else "b"
                    turn_count += 1
                except Exception as e:
                    print(f"\033[91m{e}\033[00m")
                    print(f"\033[91mClick enter to choose again.\033[00m")
                    input()
                    continue
            else:
                options = b.white_captured.copy()
                options.append('Cancel')
                question = [
                    inquirer.List("place", "What piece do you want to use?",
                                  options)]
                answer = inquirer.prompt(question)["place"]
                if answer is not 'Cancel':
                    b.white_captured.remove(answer)
                pass
    else:
        if not b.black_captured:
            print(f"Which piece do you wish to move: ")
            from_row = int(input("Row: "))
            from_col = int(input("Column: "))
            try:
                piece = b.check_piece(from_row, from_col)
                print(f"Where do you want to move your piece (row col): ")
                to_row = int(input("Row: "))
                to_col = int(input("Column: "))

                b.move_piece(piece, to_row, to_col, from_row, from_col)
                turn = "w" if turn == "b" else "b"
                turn_count += 1
            except Exception as e:
                print(f"\033[91m{e}\033[00m")
                print(f"\033[91mClick enter to choose again.\033[00m")
                input()
                continue
        else:
            question = [inquirer.List("action", "What do you want to do?",
                                      ["Move a piece",
                                       "Drop a captured piece"])]
            answer = inquirer.prompt(question)["action"]

            if answer == "Move a piece":
                print(f"Which piece do you wish to move: ")
                from_row = int(input("Row: "))
                from_col = int(input("Column: "))
                try:
                    piece = b.check_piece(from_row, from_col)
                    print(f"Where do you want to move your piece (row col): ")
                    to_row = int(input("Row: "))
                    to_col = int(input("Column: "))

                    b.move_piece(piece, to_row, to_col, from_row, from_col)
                    turn = "w" if turn == "b" else "b"
                    turn_count += 1
                except Exception as e:
                    print(f"\033[91m{e}\033[00m")
                    print(f"\033[91mClick enter to choose again.\033[00m")
                    input()
                    continue
            else:
                options = b.black_captured.copy()
                options.append('Cancel')
                question = [
                    inquirer.List("place", "What piece do you want to use?",
                                  options)]
                answer = inquirer.prompt(question)["place"]
                if answer is not 'Cancel':
                    b.black_captured.remove(answer)
                else:
                    continue
