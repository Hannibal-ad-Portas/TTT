#This is a recursive function that returns the optimal move in a game of tic tac toe
#This is done by finding all the available moves on the board and evaluating the new board state.
#If the new state results in a victory or loss then the moves score is returned,
#other wise the function is called again up to depth times
#this is an alpha beta search algo so each time the function is called the player changes and the function will care about the other extreme

from  boardEval import *

def AIplayer (gameBoard, depth, maxSym, minSym, nr2Win) :
    player = True
    currBoard = gameBoard.copy()
    moves = availabeMoves(gameBoard)
    bestmove = None
    moveValue = -10
    player = True
    while len(moves) > 0:
        move = moves.pop()
        currMoveVal = alphaBeta(currBoard, move, moves, depth, player, maxSym, minSym, nr2Win)
        if currMoveVal > moveValue:
            moveValue = currMoveVal
            bestmove = move

    gameBoard[move] = maxSym
    return gameBoard, move

def alphaBeta (board, move, moves, depth, player, maxSym, minSym, nr2Win):
    #Base Cases
    #if there are no available move return 0
    if len(moves) == 0:
        return 0
    #if depth = 0 end recursion and return 0
    if depth == 0:
        return 0

    if player:
        playerToken = maxSym
    else:
        playerToken = minSym
    board[ move ] = playerToken;
    if gameState(board, move, nr2Win):
        if (player):
            return 10
        else:
            return -10

    else:
        move = moves.pop()
        return alphaBeta (board, move, moves, depth-1, (not player), maxSym, minSym, nr2Win)

def availabeMoves (gameBoard):
    moves = list(gameBoard.__iter__())
    movesOut = []
    for item in moves:
        if (gameBoard[item[0], item[1]]):
            continue
        else:
            movesOut.append(item)
    return movesOut


