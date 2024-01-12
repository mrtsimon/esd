import random

def create_empty_board():
    return [[0 for _ in range(9)] for _ in range(9)]

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_safe(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    empty_location = find_empty_location(board)
    if not empty_location:
        return True

    row, col = empty_location
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True

            board[row][col] = 0
    return False

def get_input():
    row = int(input("Entrez la ligne (1-9): ")) - 1
    col = int(input("Entrez la colonne (1-9): ")) - 1
    num = int(input("Entrez le chiffre (1-9): "))
    return row, col, num

def main():
    board = create_empty_board()
    while True:
        print_board(board)
        row, col, num = get_input()
        if num == 0:
            break
        if not is_safe(board, row, col, num):
            print("Le chiffre n'est pas sécurisé pour cet emplacement. Veuillez réessayer.")
            continue
        board[row][col] = num

    print("\nRésultat final:")
    print_board(board)

if __name__ == "__main__":
    main()