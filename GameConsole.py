import Board
from termcolor import colored, cprint


#PRINT BOARD BEFORE STARTING GAME
def printBoard(): 
    for i in range(Board.BOARD_COLUMN):
        print(i, end=' ')
    print()
    for i in range(len(Board.board)):
        for j in range(len(Board.board[i])):
            print(Board.board[i][j],end=' ')
        print()


print('WELCOME TO DISK-BATTLE!')
printBoard()

#START GAME
#PLAYER1 REPRESENTS BY X, PLAYER2 REPRESENT BY Y
over = False
while not over:
    #GET SIGN
    if Board.currentPlayer == Board.PLAYER_ONE:
        sign = 'X'
    else:
        sign = 'O'

    #ASK FOR USER INPUT
    askCol = 'Player ' + str(Board.currentPlayer) + ' turn (Enter column 1-6): '
    col = input(askCol)
    if col != '':
        col = int(col)
        if Board.isValidInput(col):
            if Board.canPlay(Board.board, col):
                row = Board.getEmptyRow(Board.board,col)
                Board.dropPiece(Board.board,row,col, sign)
                if Board.winCheck(Board.board, sign):
                    cprint('PLAYER1 WON!','blue', attrs=['bold'])
                    over = True
                Board.switchPlay()
                printBoard()
        else:
            cprint('You input is invalid!', 'red', attrs=['bold'])
    else:
        cprint('Your input is empty!', 'red', attrs=['bold'])



