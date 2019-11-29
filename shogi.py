import inquirer as inquirer
from Board import Board


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
                piece = b.check_piece(from_row, from_col, turn)
                print(f"Where do you want to move your piece: ")
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
                    piece = b.check_piece(from_row, from_col, turn)
                    print(f"Where do you want to move your piece: ")
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
                    inquirer.List("piece", "What piece do you want to use?",
                                  options)]
                selected_piece = inquirer.prompt(question)["piece"]
                if selected_piece is not 'Cancel':
                    print(f"Where do you want to move your piece: ")
                    to_row = int(input("Row: "))
                    to_col = int(input("Column: "))
                    selected_piece.change_color()
                    try:
                        drop = b.check_drop_place(selected_piece, to_row,
                                                  to_col)
                        if drop:
                            selected_piece.change_color()
                            b.white_captured.remove(selected_piece)
                            selected_piece.change_color()
                            b.drop_piece(selected_piece, to_row, to_col)
                            turn = "w" if turn == "b" else "b"
                            turn_count += 1
                    except Exception as e:
                        print(f"\033[91m{e}\033[00m")
                        print(f"\033[91mClick enter to choose again.\033[00m")
                        input()
                        continue
    else:
        if not b.black_captured:
            print(f"Which piece do you wish to move: ")
            from_row = int(input("Row: "))
            from_col = int(input("Column: "))
            try:
                piece = b.check_piece(from_row, from_col, turn)
                print(f"Where do you want to move your piece: ")
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
                    piece = b.check_piece(from_row, from_col, turn)
                    print(f"Where do you want to move your piece: ")
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
                    inquirer.List("piece", "What piece do you want to use?",
                                  options)]
                selected_piece = inquirer.prompt(question)["piece"]
                if selected_piece is not 'Cancel':
                    print(f"Where do you want to move your piece: ")
                    to_row = int(input("Row: "))
                    to_col = int(input("Column: "))
                    selected_piece.change_color()
                    try:
                        drop = b.check_drop_place(selected_piece, to_row, to_col)
                        if drop:
                            b.drop_piece(selected_piece, to_row, to_col)
                            selected_piece.change_color()
                            b.black_captured.remove(selected_piece)
                            selected_piece.change_color()
                            turn = "w" if turn == "b" else "b"
                            turn_count += 1
                    except Exception as e:
                        print(f"\033[91m{e}\033[00m")
                        print(f"\033[91mClick enter to choose again.\033[00m")
                        input()
                        continue
                else:
                    continue
