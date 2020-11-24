import copy
import random
import time
import plotly.express as px


def get_board(n):
    #Returns an n by n board
    board = ["x"]*n
    for i in range(n):
        board[i] = ["x"]*n
    return board

def solve(board, col, n):
    # Using backtracking to find all solutions
    if col >= n:
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = "Q"
            if col == n-1:
                add_solution(board)
                board[i][col] = "x"
                return
            solve(board, col+1, n)
            board[i][col] = "x"
    
            
def is_safe(board, row, col, n):
    # Checking if it's safe to place a queen at board[x][y]
    # Checking row on left side
    for j in range(col):
        if board[row][j] == "Q":
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i=i-1
        j=j-1
    x, y = row,col
    while x < n and y >= 0:
        if board[x][y] == "Q":
            return False
        x=x+1
        y=y-1
    return True

def add_solution(board):
    #Saves the board state to the global variable: solutions
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)


if __name__ == "__main__":

    timer = []
    for i in range(4,14):
        print("For n = ", i)
        #Returns a square board of nxn dimension
        board = get_board(i)

        #Empty list of all possible solutions
        solutions = []

        #Solving using backtracking
        start_time = time.time()
        solve(board, 0, i)
        timer.append(time.time() - start_time)
        print("Time Taken: ", time.time() - start_time)
        print("Total number of solutions=", len(solutions))

        print()

    fig = px.line(x=list(range(4,14)), 
                  y=timer,
                  labels={"x": "N Queen",
                          "y": "Time(s)"},
                  title="Time Graph")

    fig.show()
