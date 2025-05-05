
def solveNQueens(n):
    board = [-1] * n
    solutions = []

    def isSafe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solution = []
            for r in range(n):
                row_str = "".join("Q" if board[r] == c else "." for c in range(n))
                solution.append(row_str)
            solutions.append(solution)
            return
        
        for col in range(n):
            if isSafe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  

    backtrack(0)

    if not solutions:
        print("No solution exists.")
    else:
        for idx, sol in enumerate(solutions):
            print(f"Solution {idx + 1}:")
            for row in sol:
                print(row)
            print()

n = int(input("Enter value of N (e.g., 4 or 8): "))
solveNQueens(n)
