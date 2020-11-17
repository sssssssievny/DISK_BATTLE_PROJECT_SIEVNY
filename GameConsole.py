from Board import *

#CREATE BOARD

board =  createBoard(BOARD_ROW,BOARD_COLUMN)


#PLAY GAME
noWinner = False
turn = 0
while not noWinner:
    if turn % 2 == 0:
        col = int(input('Player1: '))
        if isAvailable(board, col):
            available = isAvailable(board,col)
            dropPiece(board,available,col,'X')
    else:
        col = int(input('Player2: '))
        if isAvailable(board, col):
            available = isAvailable(board,col)
            dropPiece(board,available,col,'Y')
    turn += 1
    print(board)