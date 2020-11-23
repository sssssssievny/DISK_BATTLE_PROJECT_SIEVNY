
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

def resetBoard(board):
    for i in range(BOARD_ROW):
        for j in range(BOARD_COLUMN):
            board[i][j] = '0'

def dropPiece(board, row, col, sign):
    board[row][col] = sign


def canPlay(board,col):
    return board[0][col] == '0'


def checkEmptySlot(board,col):
    for i in range(BOARD_ROW):
        if board[-(i+1)][col] == '0':
            return -(i+1)


#CHECK POSSIBLE WINNING SHAPE
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
    for i in range(BOARD_COLUMN - 3):
        for j in range(BOARD_ROW - 3):
            if board[j][i] == sign and board[j+1][i+1] == sign and board[j+2][i+2] == sign and board[j+3][i+3] == sign:
                return True

    #DIAGONAL2 CHECK

    for i in range(BOARD_COLUMN-3):
        for j in range(BOARD_ROW-2):
            if board[-(j+1)][i] == sign and board[-(j+2)][i+1] == sign and board[-(j+3)][i+2] == sign and board[-(j+4)][i+3] == sign:
                return True
