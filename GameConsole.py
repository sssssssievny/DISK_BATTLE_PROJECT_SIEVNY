from Board import *


#PRINT BOARD BEFORE STARTING GAME

print('WELCOME TO DISK-BATTLE!')
printBoard(board)

#START GAME FOR THE FIRST TIME
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
