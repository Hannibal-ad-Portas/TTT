# This function handles the logic for the three player types
# Human:    get user input
# Random:   place player token in an unoccupied position
# AI:       use alpha beta pruning to crush the weak opponents
#
# Inputs:
#   board:  this is a board.Board object
#   nr2Win: the number of adjacent tokens needed to win
#   player: the player type
#   plySym:  the symbol representing the player
#   depth:  the max depth the AB algo is allowed to calculate
#
# Outputs:
#   gameBoard:  the state of the board after the player made their move
#   move:       the most recent move, used to check for victory
import board
import random
from AIplayer import *

def playGame(gameBoard, nr2Win, player, maxSym, minSym, depth):
    if (player == "human"):
        gameBoard, move = humanInput(gameBoard, maxSym)
    elif (player == "random"):
        gameBoard, move = randomPlayer (gameBoard, minSym)
    elif (player == "AI"):
        print("Placing token inteligently")
        gameBoard, move = AIplayer(gameBoard, depth, maxSym, minSym, nr2Win)

    return gameBoard, move

def randomPlayer (gameBoard, plySym):
    print("Random Move")
    moveMade = False
    while not moveMade:
        x = random.randint(0,gameBoard.lendata())
        y = random.randint(0,gameBoard.lendata())
        if [x,y] in gameBoard:
            if gameBoard[x,y] is board.Empty:
                gameBoard[x,y] = plySym
                moveMade = True
                move = [x,y]

    return gameBoard, move


def humanInput (gameBoard, plySym):
    print("Calling Human Player")
    moveMade = False
    move = []
    while not moveMade:
        x = int(input("Col: "))
        y = int(input("Row: "))
        if [x,y] in gameBoard:
            if gameBoard[x,y] is board.Empty:
                gameBoard[x,y] = plySym
                moveMade = True
                move = [x,y]
            else:
                print("That space is already occupied please try again")
        else:
            print("That position is OOB\nPlease try again\nIndexes Start at 0")

    return gameBoard, move

