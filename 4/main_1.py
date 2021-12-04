import pandas as pd
import numpy as np
bingoInput = []
boards = []
def createBoard(board):
    boardMatriz = []
    for row in board:
        rowList=[]
        row = row.strip().split()
        for num in row:
            rowList.append(int(num))
        boardMatriz.append(rowList)
    return boardMatriz

with open('bingoInput.txt','r') as f:
    line = f.readline().strip()
    bingoInput = line.split(',')
    bingoInput = [int(num) for num in bingoInput]

with open('input.txt','r') as f:
    lines = f.readlines()
    boardsUnsorted = [line.strip() for line in lines]
    boardsUnsorted = list(filter(lambda x:(x!=""),boardsUnsorted))
    for i  in range(0,len(boardsUnsorted),5):
        board = boardsUnsorted[i:i+5]
        board = createBoard(board)
        boards.append(board)


class Board():
    def __init__(self,matrix=None):
        self.board = matrix
        self._bingo = None
        self._lastNum = None
    @property
    def bingo(self):
        return self._bingo
    @bingo.setter
    def bingo(self,bingo):
        self._bingo = bingo
    @property
    def lastNum(self):
        return self._lastNum 
    @lastNum.setter
    def lastNum(self,lastNum):
        self._lastNum = lastNum
  
    def finalScore(self,bingoList):
        boardEmpty = []
        indexOflastNum = bingoList.index(lastNum) 
        bingoList = bingo[:indexOflastNum+1]
        for row in self.board:
            newRow = list(filter(lambda x:not(x in bingoList), row))
            boardEmpty.append(newRow)
        totalSum = [sum(row) for row in boardEmpty]
        totalSum = sum(totalSum)
        return  totalSum*data[1]

def checkBoards(num,_boards):
    boardsWithNum = []
    for board in _boards:
        boardNp = np.array(board)
        df = pd.DataFrame(boardNp)
        if num in df.values:
            boardsWithNum.append(board)
    return boardsWithNum

def getFirstFull(board,nums):
    cols = [0]*5
    rows = [0]*5
    numXY = {}
    bingo = []
    lastNum = 0
    #Create board coordinates dict
    for row in range(len(board.board)):
        for col in range(row):
            num = board.board[row][col]
            numXY[num] = [row,col]
    #check list winner
    for lastNum  in nums:
        coordinates = numXY[lastNum]
        col = coordinates[1]
        row = coordinates[0]
        cols[col]+=1
        rows[row]+=1
        if rows[row] == 5:
            board.bingo = board.board[row]
            break
        elif cols[col]==5:
            for rows in board.board:
                for cols in range(len(rows)):
                    if cols == col:
                        bingo.append(rows[cols])
            board.bingo = bingo
            break
    board.lastNum = lastNum
    return board

def getWinner(fulls,bingoList):
    winnerIndex = 100**10
    winner = 0
    for full in range(len(fulls)):
        indexOfLastNum = bingoList.index(fulls[full].lastNum)
        if indexOfLastNum < winnerIndex :
            winnerIndex = indexOfLastNum
            winner = full
    return fulls[winner]


def bingo(data):
    bingoNumber = {}
    boardsMap = {}
    bingoFulls = []
    #filter board by concurrency in each bingo number
    for num in data:
       bingoNumber[num] = checkBoards(num,boards)
    #Get order of bingo number by board
    for board in range(len(boards)):
         boardsMap[board]=[]
         for key,value in bingoNumber.items():
             for row in value:
                if boards[board] == row:
                     boardsMap[board].append(key)
                     break
    for key,value in boardsMap.items():
        newBoard = Board(boards[key])
        fulls = getFirstFull(newBoard,value)
        bingoFulls.append(fulls)
    winner = getWinner(bingoFulls,data)
    print(f"Winner:")
    print(pd.DataFrame(winner.board))
    print(f"With the full:{winner.bingo}")
    return winner
    


if __name__ == "__main__":
    winner = bingo(bingoInput)
    score = winner.finalScore(bingoInput) 
    print(f"Score:{score}")
