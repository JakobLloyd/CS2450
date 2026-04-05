import os


# All eight possible winning combinations (rows, columns, diagonals)
WINNING_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6],             # diagonals
]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_board(board):
    """Print the current state of the board with dividers between rows."""
    for row in range(3):
        print(f" {board[row * 3]} | {board[row * 3 + 1]} | {board[row * 3 + 2]} ")
        if row < 2:
            print("---+---+---")


def check_winner(board):
    """Return 'X' or 'O' if that player has won, otherwise return None."""
    for combo in WINNING_COMBOS:
        marker = board[combo[0]]
        if marker in ('X', 'O') and all(board[i] == marker for i in combo):
            return marker
    return None


def play():
    # Initialize board with position numbers so players know which index to pick
    board = [str(i) for i in range(9)]
    current_player = "X"

    while any(cell.isdigit() for cell in board):
        clear_screen()
        print("Tic-Tac-Toe\n")
        display_board(board)
        print(f"\n{current_player}'s turn!")

        # Get and validate the player's move
        try:
            move = int(input("Pick a spot (0-8): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if 0 <= move < 9 and board[move].isdigit():
            board[move] = current_player

            winner = check_winner(board)
            if winner:
                clear_screen()
                print("Tic-Tac-Toe\n")
                display_board(board)
                print(f"\n{winner} wins!")
                return

            # Alternate turns between X and O
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Spot is taken or out of range. Try again.")

    # No empty cells remain and no winner — it's a draw
    clear_screen()
    print("Tic-Tac-Toe\n")
    display_board(board)
    print("\nIt's a draw!")


play()
