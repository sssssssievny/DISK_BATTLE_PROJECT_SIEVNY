
#GLOBAL VALUES FOR ROW AND COLUMN (CONSTANTS)

BOARD_ROW = 6
BOARD_COLUMN = 7
boardList = []


def createBoard(row,col):
    for i in range(row):
        boardList.append(['0']*col)
    return boardList

# CREATE BOARD

board =  createBoard(BOARD_ROW,BOARD_COLUMN)

def printBoard(board): 
    for i in range(BOARD_COLUMN):
        print(i, end=' ')
    print()
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end=' ')
        print()


def playGame():
    over = False
    turn = 0
    while not over:
        #WHEN TURN IS EVEN, PLAYER1 TURN TO PLAY!
        if turn % 2 == 0:
            col = int(input('Player1 (enter any number from 0-6): '))
            if isAvailable(board, col):
                row = checkEmptySlot(board,col)
                dropPiece(board,row,col,'X')
                if winCheck(board,'X'):
                    print('PLAYER1 WON!')
                    over = True
        #WHEN TURN IS ODD, PLAYER2 TURN TO PLAY!
        else:
            col = int(input('Player2 (enter any number from 0-6): '))
            if isAvailable(board, col):
                row = checkEmptySlot(board,col)
                dropPiece(board,row,col,'Y')
                if winCheck(board,'Y'):
                    print('PLAYER2 WON!')
                    over = True
        turn += 1

            #PRINT BOARD EACH TIME, AFTER EACH PLAYER INPUT()

        printBoard(board)


def startGame():
    validInput = True
    while validInput:
        startGame = input('TYPE <S> TO START GAME: ')
        if startGame == 'S':
            validInput = False
    printBoard(board)
    playGame()

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
    for i in range(BOARD_COLUMN - 3):
        for j in range(BOARD_ROW - 3):
            if board[j][i] == sign and board[j+1][i+1] == sign and board[j+2][i+2] == sign and board[j+3][i+3] == sign:
                return True

    #DIAGONAL2 CHECK

    for i in range(BOARD_COLUMN-3):
        for j in range(BOARD_ROW-2):
            if board[-(j+1)][i] == sign and board[-(j+2)][i+1] == sign and board[-(j+3)][i+2] == sign and board[-(j+4)][i+3] == sign:
                return True
