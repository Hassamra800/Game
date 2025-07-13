import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print("\n")
    for i in range(3):
        row = " | ".join(board[i])
        print(f" {row} ")
        if i < 2:
            print("---+---+---")
    print("\n")

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column, e.g. 1 3): ")
            row, col = map(int, move.strip().split())
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Invalid input. Row and column must be between 1 and 3.")
                continue
            if board[row - 1][col - 1] != ' ':
                print("That cell is already taken. Try again.")
                continue
            return row - 1, col - 1
        except ValueError:
            print("Invalid input format. Please enter two numbers separated by a space.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        clear_screen()
        print_board(board)
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        if check_win(board, current_player):
            clear_screen()
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break
        if check_draw(board):
            clear_screen()
            print_board(board)
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
