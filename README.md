# python-game


Initialize the 3x3 game board with empty spaces

Display the empty board to the players

Repeat the following steps until the game is over:

    - Player 1's turn:
        - Prompt Player 1 to enter row and column for their move
        - Check if the chosen position is valid (within the board and not already occupied)
        - If valid, place 'X' in the chosen position
        - Check if Player 1 has won (3 'X's in a row, column, or diagonal)
        - If yes, end the game and declare Player 1 as the winner
        - If no, continue to the next player's turn

    - Player 2's turn:
        - Prompt Player 2 to enter row and column for their move
        - Check if the chosen position is valid (within the board and not already occupied)
        - If valid, place 'O' in the chosen position
        - Check if Player 2 has won (3 'O's in a row, column, or diagonal)
        - If yes, end the game and declare Player 2 as the winner
        - If no, continue to the next player's turn

    - Check for a draw (all spaces are occupied with no winner)
    - If a draw, end the game and declare it a draw
    - End of the game loop
  Display the final game board
