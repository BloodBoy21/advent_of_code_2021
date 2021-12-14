board = []
flashed = set()
flashes = 0

def processNeighbours(x, y):
    global board
    global flashed
    global flashes
    for row in range(x - 1, x + 2):
        for col in range(y - 1, y + 2):
            if x == row and y == col:
                continue
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and (row, col) not in flashed:
                board[row][col] += 1
                if board[row][col] > 9:
                    board[row][col] = 0
                    flashes += 1
                    flashed.add((row, col))
                    processNeighbours(row, col)


with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    board = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            board[i][j] = int(lines[i][j])

    for n in range(100):
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] += 1
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] > 9:
                    board[i][j] = 0
                    flashes += 1
                    flashed.add((i, j))
                    processNeighbours(i, j)
        flashed = set()

    print("1: " + str(flashes))

    for n in range(10000):
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] += 1
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] > 9:
                    board[i][j] = 0
                    flashes += 1
                    flashed.add((i, j))
                    processNeighbours(i, j)
                if len(flashed) == len(board) * len(board[0]):
                    print("2: " + str(n + 101))
                    exit(0)
        flashed = set()
