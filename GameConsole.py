from Board import *

#CREATE BOARD

board =  createBoard(BOARD_ROW,BOARD_COLUMN)
for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end='')
        print()

#PLAY GAME
noWinner = False
turn = 0
while not noWinner:
    if turn % 2 == 0:
        col = int(input('Player1: '))
        if isAvailable(board, col):
            row = checkEmptySlot(board,col)
            dropPiece(board,row,col,'X')
    else:
        col = int(input('Player2: '))
        if isAvailable(board, col):
            row = checkEmptySlot(board,col)
            dropPiece(board,row,col,'Y')
    turn += 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end='')
        print()
    