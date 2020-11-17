BOARD_ROW = 6
BOARD_COLUMN = 7
rowList = []
boardList = []
def createBoard(row,col):
    for i in range(col):
        rowList.append('0')
    for j in range(row):
        boardList.append(rowList)
    return boardList


def dropPiece(board, row, col, sign):
    board[row][col] = sign
def isAvailable(boardList,col):
    return boardList[BOARD_ROW-1][col] == '0'

def checkEmptySlot(board,col):
    for i in range(BOARD_ROW):
        if board[i][col] == '0':
            return i





