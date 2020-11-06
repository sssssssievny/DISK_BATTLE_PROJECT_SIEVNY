theBoard = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
def showBoard(board):
    for i in theBoard:
        for j in i:
            print(j,' ',end="")
        print()

showBoard(theBoard)

