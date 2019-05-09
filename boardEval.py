#This function determines if the game of tic tac toe is over
#
# Input:
#   gameBoard:  the game of TTT to be evaluated
#   move:       the col/row of the last move made
#   nr2Win:
# Output:
#   gameState:  a string corresponding to several game states
#       False:  if no victor
#       True:   if there is a winner

def gameState (gameBoard, move, nr2Win):
    downRight   = [1, 1]
    upRight     = [1, -1]
    downLeft    = [-1, 1]
    upLeft      = [-1, -1]
    down        = [0, 1]
    up          = [0, -1]
    right       = [1, 0]
    left        = [-1, 0]

    print("move: ", move)

    #check column
    if check4Victory(gameBoard, move, down, up, nr2Win):
        return True
    #check row
    if check4Victory(gameBoard, move, left, right, nr2Win):
        return True
    #check diagonal 1
    if check4Victory(gameBoard, move, upLeft, downRight, nr2Win):
        return True
    #check diagonal 2
    if check4Victory(gameBoard, move, upRight, downLeft, nr2Win):
        return True
    return False

def check4Victory (gameBoard, move, direction, reverse, nr2Win):
    # get a list of indexes in the row col and diagonals
    # board.iterline() returns a list starting at the specified pos and traveling
    # to the edge of the board. To get the complete list use the last index
    # returned and reverse direction

    cordList = list(gameBoard.iterline((move[0], move[1]), (direction[0], direction[1])))
    cordList = list(gameBoard.iterline((cordList[-1]), (reverse[0], reverse[1])))
    pos = cordList.index((move[0], move[1]))
    #slice the list so that it only has indexes that can be part of a winning pos
    #cordList = cordList [pos - nr2Win : pos + nr2Win]

    if (len(cordList) >= nr2Win):
        #print("checking cordList for Victory")
        for i, index in cordList:
            numChecked = 0
            #print(numChecked)
            for j in range(nr2Win):
                #print(gameBoard[ cordList[i] ], gameBoard[cordList[j]])
                if (gameBoard[ cordList[i] ] != gameBoard[cordList[j]]) or gameBoard[ cordList[i] ] == False:
                    break
                else:
                    numChecked = numChecked + 1

            if numChecked == nr2Win:
                #print("Victory")
                #print(cordList)
                return True

    return False
