# ShogiTest
Shogi is a Japanese Chess. 

Implemented functionality:
- Pieces movement.
- Pawn and Lance are automatically promoted when reaching last rank of the 
furthest side.
- Knight is automatically promoted when reaching last two ranks of the 
furthest side.
- Other pieces (that can be promoted) are automatically promoted when 
reaching last three ranks of the furthest side.
- Promoted pieces movement.
- Select if player wants to use a captured piece (if it has any)
- Check if a piece can be dropped.
    - If a player wants to drop a pawn, checks if there is a pawn of the 
    same color on the same column where the player wants to drop it. 
    Also, that the row is not the last on the board so it prevents the 
    pawn from moving forward.

It has been implemented in Python.

