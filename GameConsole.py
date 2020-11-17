from Board import *

# CREATE BOARD

board =  createBoard(BOARD_ROW,BOARD_COLUMN)

#PRINT BOARD BEFORE STARTING GAME

print('WELCOME TO DISK-BATTLE!')
printBoard(board)

#PLAY GAME, ALWAYS PLAY WHEN THERE ARE SPACE LEFT TO PLAY AND NO ONE WINS YET
noWinner = False
turn = 0
while not noWinner:
    #WHEN TURN IS EVEN, PLAYER1 TURN TO PLAY!
    if turn % 2 == 0:
        col = int(input('Player1 (enter any number from 0-6): '))
        if isAvailable(board, col):
            row = checkEmptySlot(board,col)
            dropPiece(board,row,col,'X')
    #WHEN TURN IS ODD, PLAYER2 TURN TO PLAY!
    else:
        col = int(input('Player2 (enter any number from 0-6): '))
        if isAvailable(board, col):
            row = checkEmptySlot(board,col)
            dropPiece(board,row,col,'Y')
    turn += 1

    #PRINT BOARD EACH TIME, AFTER EACH PLAYER INPUT()

    printBoard(board)