#!/usr/bin/python3
"""scrpit to solve the nqueen problem"""

from sys import argv


def check_mate(board, x, y):
    "check if the can put in correct place or not"
    m = len(board)
    for i in range(m):
        mate = 0
        if x + i < m:
            mate += board[x + i][y]
        if x - i >= 0:
            mate += board[x - i][y]
        if y + i <= m - 1:
            mate += board[x][y + i]
        if y - i >= 0:
            mate += board[x][y - i]

        if x - i >= 0 and y - i >= 0:
            mate += board[x - i][y - i]
        if x + i < m and y + i < m:
            mate += board[x + i][y + i]

        if x - i >= 0 and y + i < m:
            mate += board[x - i][y + i]
        if x + i < m and y - i >= 0:
            mate += board[x + i][y - i]

        if mate > 0:
            return 1
    return 0


def extract_sol(board):
    """extract the solution from board to be in format"""
    answer = set()
    m = len(board)
    for i in range(m):
        for j in range(m):
            if board[i][j] == 1:
                answer.add(tuple([i, j]))
    return tuple(answer)


def nqueen(N, board, queens, answers):
    """N queen function"""
    if queens == N:
        answers.add(extract_sol(board))
        return

    for i in range(N):
        for j in range(N):
            if not check_mate(board, i, j):
                board[i][j] = 1
                nqueen(N, board, queens + 1, answers)
                board[i][j] = 0
    return answers


def create_board(n):
    """create a board"""
    board = [[0] * n for _ in range(n)]
    return board


def main():
    "main funciton"
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        N = int(argv[1])
    except Exception:
        print('N must be a number')
        exit(1)
    if N < 4:
        print('N must be at least 4')
        exit(1)
    board = create_board(N)
    answers = nqueen(N, board, 0, set())
    for answer in answers:
        arr = []
        for s in answer:
            arr.append(list(s))
        print(arr)


if __name__ == "__main__":
    main()
