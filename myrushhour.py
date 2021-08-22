from movement import *
from aStar import *


def rushhour(heuristic, path):
    astar = AStarSolution(heuristic, path)
    if (astar != []):
        totalStatesExplored = astar.pop()
        astar.reverse()
        for i in range(len(path)):
            printBoard(astar[i])
            print("\n")
        print("Total Moves: ", len(astar) - 1) 
        print("Total States Explored: ", totalStatesExplored )
    else:
        print("Can't solve try again :)")
