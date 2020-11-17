from Board import *

# # #CREATE BOARD

board =  createBoard(BOARD_ROW,BOARD_COLUMN)

print('WELCOME TO DISK-BATTLE!')
printBoard(board)

#PLAY GAME
noWinner = False
turn = 0
while not noWinner:
    if turn % 2 == 0:
        col = int(input('Player1 (enter any number from 0-6): '))
        if isAvailable(board, col):
            row = checkEmptySlot(board,col)
            dropPiece(board,row,col,'X')
    else:
        col = int(input('Player2 (enter any number from 0-6): '))
        if isAvailable(board, col):
            row = checkEmptySlot(board,col)
            dropPiece(board,row,col,'Y')
    turn += 1

    printBoard(board)