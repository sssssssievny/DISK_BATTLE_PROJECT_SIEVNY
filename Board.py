
#GLOBAL VALUES FOR ROW AND COLUMN (CONSTANTS)

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

def winCheck(board, sign):
    #HORIZONTAL CHECK
    for i in range(BOARD_COLUMN - 3):
        for j in range(BOARD_ROW):
            if (board[-j][i] == sign and board[-j][i+1] == sign) and (board[-j][i+2] == sign and board[-j][i+3] == sign):
                return True
    #VERTICAL CHECK
    for i in range(BOARD_COLUMN):
        for j in range(BOARD_ROW-3):
            if board[j][i] == sign and board[j+1][i] == sign and board[j+2][i] == sign and board[j+3][i] == sign:
                return True

    #DIAGONAL1 CHECK
    col = 0
    for i in range(BOARD_ROW-1):
        for j in range(BOARD_COLUMN):
            if board[i][col] == sign and board[i+1][col+1] == sign and board[i+2][col+2] == sign and board[i+3][col+3] == sign:
                return True

    #DIAGONAL2 CHECK
    col = 1
    for i in range(BOARD_ROW-2):
        for j in range(BOARD_COLUMN):
            if board[i][col] == sign and board[i+1][col+1] == sign and board[i+2][col+2] == sign and board[i+3][col+3] == sign:
                return True
    #DIAGONAL3 CHECK
    col = 2
    for i in range(BOARD_ROW-3):
        for j in range(BOARD_COLUMN):
            if board[i][col] == sign and board[i+1][col+1] == sign and board[i+2][col+2] == sign and board[i+3][col+3] == sign:
                return True
    #DIAGONAL4 CHECK
    col = 3
    for i in range(BOARD_ROW-3):
        for j in range(BOARD_COLUMN):
            if board[i][col] == sign and board[i+1][col+1] == sign and board[i+2][col+2] == sign and board[i+3][col+3] == sign:
                return True
    #DIAGONAL5 CHECK
    col = -1
    for i in range(BOARD_ROW-3):
        for j in range(BOARD_COLUMN):
            if board[i][col] == sign and board[i+1][col-1] == sign and board[i+2][col-2] == sign and board[i+3][col-3] == sign:
                return True

    #DIAGONAL6 CHECK
    col = -2
    for i in range(BOARD_ROW-3):
        for j in range(BOARD_COLUMN):
            if board[i][col] == sign and board[i+1][col-1] == sign and board[i+2][col-2] == sign and board[i+3][col-3] == sign:
                return True
    col = -3
    for i in range(BOARD_ROW-3):
        for j in range(BOARD_COLUMN):
            if board[i][col] == sign and board[i+1][col-1] == sign and board[i+2][col-2] == sign and board[i+3][col-3] == sign:
                return True

