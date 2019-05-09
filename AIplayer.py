#This is a recursive function that returns the optimal move in a game of tic tac toe
#This is done by finding all the available moves on the board and evaluating the new board state.
#If the new state results in a victory or loss then the moves score is returned, other wise the function is called again up to depth times
#this is an alpha beta search algo so each time the function is called the player changes and the function will care about the other extreme

def AIplayer (gameBoard, depth ):
    currBoard = gameBoard
    moves = availabeMoves(gameBoard)
    

def availabeMoves (gameBoard):
    moves = []
    moves = list(gameBoard.__iter__())
    #print(moves)
    for i, item in moves:
        if (gameBoard[i]):
            del moves[i]
    #print("Available: ", moves)
    return moves

def alphaBeta ()
