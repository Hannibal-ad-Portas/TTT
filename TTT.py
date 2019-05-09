#! /usr/bin/python3
# Usage TTT nrRows nrCols nr2Win player1 player2 depth

import sys
import board
from playerLogic import *
from boardEval import *

def usage (argv):
    print("Usage: ", sys.argv[0], " nrRows nrCols nr2Win player1 player2 depth")
    print("The options for player1 and 2 are:")
    print("\thuman\n\trandom\n\tAI")

def main (argv):
    expArg = 7
    if ((len(sys.argv)) != expArg):
        print("Wrong number of args")
        print("Expected args: ", expArg)
        print("You Provided: ", len(sys.argv))
        usage(argv)
        return


    nrRows  = int(sys.argv[1])
    nrCols  = int(sys.argv[2])
    nr2Win  = int(sys.argv[3])
    player1 = str(sys.argv[4])
    player2 = str(sys.argv[5])
    depth   = int(sys.argv[6])

    ply1Sym = 'X'
    ply2Sym = 'O'

    gameBoard = board.Board((nrRows,nrCols))
    #populate the board with a simgle ' ' just to display the board
    gameBoard.populate(" ")
    gameBoard.draw()
    #remove the values in the board so that pos 0,0 can be set by a player
    gameBoard.clear();

    turns = 1
    while turns <= nrRows * nrCols:
        print("Turn: ", turns)
        if turns > 1:
            gameBoard.draw()

        if not(turns % 2 == 0):
            gameBoard, move = playGame(gameBoard, nr2Win, player1, ply1Sym, depth)
            gameBoard.draw()
            if (turns >= nr2Win):
                if gameState(gameBoard, move, nr2Win):
                    print("Player 1 victory")
                    return
        else:
            gameBoard, move = playGame(gameBoard, nr2Win, player2, ply2Sym, depth)
            gameBoard.draw()
            if (turns >= nr2Win):
                if gameState(gameBoard, move, nr2Win):
                    print("Player 2 victory")
                    return
        turns = turns + 1

    print("Tie")


main(1)
