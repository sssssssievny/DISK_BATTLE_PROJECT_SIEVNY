BOARD_ROW = 6
BOARD_COLUMN = 7
boardList = []
def createBoard(row,col):
    for i in range(row):
        boardList.append(['0']*col)
    return boardList

def printBoard(board): 
    for i in range(BOARD_COLUMN):
        print(i, end=' ')
    print()
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end=' ')
        print()

def dropPiece(board, row, col, sign):
    board[row][col] = sign

def isAvailable(board,col):
    return board[0][col] == '0'

def checkEmptySlot(board,col):
    for i in range(BOARD_ROW):
        if board[-(i+1)][col] == '0':
            return -(i+1)





