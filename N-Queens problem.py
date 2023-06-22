def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col]

    # Check the left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, N):
    # Base case: If all queens are placed, return True
    if col >= N:
        return True

    # Recursive case: Try placing a queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            # Recursively check if the remaining queens can be placed
            if solve_n_queens_util(board, col + 1, N):
                return True

            # If placing queen at board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If no queen can be placed in this column, return False
    return False


def solve_n_queens(N):
    # Create an empty N x N chessboard
    board = [[0] * N for _ in range(N)]

    if not solve_n_queens_util(board, 0, N):
        print("No solution exists.")
        return

    # Print the solution
    for row in board:
        print(' '.join(str(cell) for cell in row))


# Test the function with N = 4
solve_n_queens(4)
