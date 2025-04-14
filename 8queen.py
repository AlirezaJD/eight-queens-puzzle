def is_safe(board, row, col):
    # Check if the queen can be placed in the current position

    # Check the current row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < 8 and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_queens(board, col):
    # Base case: If all queens are placed, return True
    if col >= 8:
        return True

    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place the queen

            # Recursive call to place queens in the next column
            if solve_queens(board, col + 1):
                return True

            # If placing the queen in the current position doesn't lead to a solution,
            # backtrack and remove the queen from the current position
            board[i][col] = 0

    return False


def print_solution(board):
    # Print the board configuration
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=" ")
        print()


def solve_8queens(blocked_houses):
    board = [[0] * 8 for _ in range(8)]

    # Mark blocked houses on the board
    for i in range(8):
        for j in blocked_houses[i]:
            board[i][j] = -1

    if solve_queens(board, 0):
        # Convert board to queen positions array
        queens = []
        for i in range(8):
            for j in range(8):
                if board[i][j] == 1:
                    queens.append(j)
        return queens
    else:
        return None


# Take input for blocked houses
blocked_houses = []
print("Enter the blocked houses (one house number per line, separated by spaces):")
for _ in range(8):
    line = input().strip().split()
    blocked_houses.append([int(house) for house in line])

# Solve the 8-queen problem
queens = solve_8queens(blocked_houses)

# Print the result
if queens:
    print("Queen Positions:")
    print(queens)
else:
    print("No solution found.")