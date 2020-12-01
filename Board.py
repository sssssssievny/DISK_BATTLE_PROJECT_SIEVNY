
#GLOBAL VALUES FOR ROW AND COLUMN (CONSTANTS)

BOARD_ROW = 6
BOARD_COLUMN = 7
boardList = []

PLAYER_ONE = 1
PLAYER_TWO = 2


NO_WINNER = 'ON_PROGRESS'
RED_WINNER = 'RED_WON'
YELLOW_WINNER = 'YELLOW_WON'
BOARD_FULL = 'BOARD_FULL'

currentPlayer = PLAYER_ONE  # At game start

def switchPlay():
    global currentPlayer
    if currentPlayer == PLAYER_ONE:
        currentPlayer = PLAYER_TWO
    else:
        currentPlayer = PLAYER_ONE

    return currentPlayer

def createBoard(row,col):
    for i in range(row):
        boardList.append(['.']*col)
    return boardList

#CREATE BOARD
board =  createBoard(BOARD_ROW,BOARD_COLUMN)


#CLEAR BOARD
def clearBoard():
    board = createBoard(BOARD_ROW,BOARD_COLUMN)


def isValidInput(column_no):
    if column_no >=0 and column_no <=7:
        return True
    else:
        return False
#UPDATE THE SIGN TO BOARD
def dropPiece(row, col, sign):
    board[row][col] = sign

#CHECK IF COLUMN IS NOT FULL
def canPlay(col):
    return board[0][col] == '.'

#GET EMPTY ROW 
def getEmptyRow(col):
    for i in range(BOARD_ROW):
        if board[-(i+1)][col] == '.':
            return -(i+1)



#PLAY RED OR YELLOW
def play(sign, col):
        if canPlay(col):
            row = getEmptyRow(col)
            dropPiece(row,col,sign)






#CHECK POSSIBLE WINNING SHAPE
def winCheck(sign):
    #HORIZONTAL CHECK
    for i in range(BOARD_COLUMN - 3):
        for j in range(BOARD_ROW):
            if (board[-j][i] == sign and board[-j][i+1] == sign) and (board[-j][i+2] == sign and board[-j][i+3] == sign):
                if sign == 'R':
                    return RED_WINNER
                else:
                    return YELLOW_WINNER
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


