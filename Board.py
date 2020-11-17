BOARD_ROW = 6
BOARD_COLUMN = 7
boardList = []
def createBoard(row,col):
    for i in range(row):
        boardList.append(['0']*col)
    return boardList

def dropPiece(board, row, col, sign):
    board[row][col] = sign

def isAvailable(board,col):
    return board[BOARD_ROW-1][col] == '0'

def checkEmptySlot(board,col):
    for i in range(BOARD_ROW):
        if board[i][col] == '0':
            return i





