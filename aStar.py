from movement import *

#using nodes for A* algorithm
class Node(object):
    #base class for all boards
    def __init__(self, board, prev, f ,g):
        self.board = board #current game board
        self.prev = prev #index of last element in the path
        self.f = f 
        self.g = g

    def goal(self):
        row3 = list(self.board[2])
        if (row3[4] == row3[5]):
            if (row3[4] == 'X'):
                return True
        else:
            return False

# print the board output 
def printBoard(board):
        for i in board:
            print(i)
            
# uses the heuristic and g to find what f(n) is 
def solveFn(heuristic, currBoard, g):
    f = 0
    if (heuristic == 0):
        f = blockingHeuristic(currBoard) + g
    if (heuristic == 1):
        f = selfMadeHeuristic(currBoard) + g
    return f

#seeing if the path is open or closed for AstarSolution function
def createNode(state, heuristic, g, prev):
    f = solveFn(heuristic, state, g)
    returnNode = Node(state,prev,f,g)
    return returnNode

#sort with key for open paths on the board
def sortKey(board):
    return board.f

#Use AStarSearch Algorithm to solve rushhour game
def AStarSolution(heuristic, board):
    currentState = 0
    f = solveFn(heuristic, board, currentState)
    exploring = Node(board, None, f, currentState)
    openPath = [exploring]
    closedPath = []
    #counting the number of states explored
    explored = 0
    

    while(openPath != []):
        # each new node set up         
        exploring = openPath.pop(0)
        currentState = exploring.g + 1
        explored = explored + 1
        closedPath.append(exploring)
        
        #if the goal is found then return path and explored number
        if(exploring.goal()):
            path = []
            path.append(exploring.board)
            while(exploring.prev != None):
                exploring = exploring.prev
                path.append(exploring.board) 
            path.append(explored)
            return path
        #goal not found search through possible states
        else:
            newStates = generateStates(exploring, heuristic, currentState)
            length = len(newStates)
            for i in range(length):
                inClosed = False
                inOpen = False
                length1 = len(closedPath)
                for j in range(length1):
                    if (newStates[i].board == closedPath[j].board):
                        inClosed = True
                length2 = len(openPath)
                for k in range(length2):
                    if(newStates[i].board == openPath[k].board):
                        inOpen = True
                if (not inClosed and not inOpen):
                    openPath.append(newStates[i])
        #sort open by f(n)
        for i in range(len(openPath)):
            openPath.sort(key = sortKey)
    return [] 

# implementing blocking heuristic
def blockingHeuristic(board):
    xRow = list(board[2])
    blocksInRow = []
    blocks = 0
    x = 0

    for i in range(6):
        if (xRow[i] == 'X'):
            x = i
            break
    for j in range(i , 6):
        if (xRow[j] != 'X'):
            if (xRow[i] != '-'):
                if (xRow[j] not in blocksInRow):
                    blocksInRow.append(xRow[j])
                    blocks = blocks + 1
    if ('-' in blocksInRow):
        blocks = blocks - 1
    if (blocks == 0):
        return 0 
    else:
        return (blocks + 1)

# This heuristic counts the number of blocks in front of X and the number of steps X has to take to reach the end if we've reached goal state h(n) = 0
#else  h(n) = blockingObstacles + spacesUntilXReachesGoal + 1
# heuristic == 1
def selfMadeHeuristic(board):
    pass 
    """traverseXRow = list(board[2])
    blocksInRow = []
    blocksCounter = 0
    whereIsX = 0
    XToGoal = 0

    #blocking heuristic
    for j in range(6):
        if (traverseXRow[j] == 'X'):
            whereIsX = j + 1
            break
    for i in range(j , 6):
        if (traverseXRow[i] != 'X'):
            if (traverseXRow[i] != '-'):
                if (traverseXRow[i] not in blocksInRow):
                    blocksInRow.append(traverseXRow[i])
                    blocksCounter += 1
    if ('-' in blocksInRow):
        blocksCounter -= 1

    #define return value with added X movements
    XToGoal = (6 - j - 2) # 6-j is first X and there are 2 extra spots
    h = XToGoal + blocksCounter + 1 ## one plus the number of cars plus how many moves until exit
    if (blocksCounter == 0):
        return 0 ## h(n) = 0
    else:
        return h"""

#find vehicles on board with coordinates
def vehicles(board):
    #find '-' on board and add to list obstacles and visited
    obstacles = []
    visitedNode = []
    for i in range(6):
        currentRow = board[i]
        for j in range(6):
            if(currentRow[j] != '-'):
                if(currentRow[j] not in obstacles):
                    obstacles.append([currentRow[j],(j,i)])
                    if(currentRow[j] not in visitedNode):
                        visitedNode.append(currentRow[j])
    #now sort the 2 lists obstacles, visited
    obstacles.sort()
    visitedNode.sort()

    currentElement = []
    obstacleCoord = []
    length = len(visitedNode)
    length2 = len(obstacles)
    for i in range(length):
        currentElement = []
        currentElement.append(visitedNode[i])
        for j in range(length2):
            if(visitedNode[i] == obstacles[j][0]):
                currentElement.append(obstacles[j][1])
        obstacleCoord.append(currentElement)
    return obstacleCoord
    
#generate all states within game board
def generateStates(board,heurisitic, g):
    newStates = []
    vStates = []
    hStates = []
    
    obstacleCoord = vehicles(board.board)
    for i in range(len(obstacleCoord)):
        x = obstacleCoord[i][1][0] 
        y = obstacleCoord[i][2][0]
        #vertical
        if (x ==  y): 
            vStatesTemp = verticalState(board.board, obstacleCoord[i])
            for j in range(len(vStatesTemp)):
                vStates.append(vStatesTemp[j])
        #horizontal
        else: 
            hStatesTemp = horizontalState(board.board,obstacleCoord[i])
            for j in range(len(hStatesTemp)):
                hStates.append(hStatesTemp[j])
    
    # make each new state into correct format for A* search
    allStates = hStates + vStates
    for i in range(len(allStates)):
        newStates.append(createNode(allStates[i],heurisitic,g,board)) 
    return newStates



#generate horizontal states
def horizontalState(board, obstacle):
    newStates = []
    rightX = obstacle[-1][0]
    rightY = obstacle[-1][1] 
    if(slideRight(rightX,rightY,board) != None):
        newStates.append(slideRight(rightX,rightY,board))
    leftX = obstacle[1][0]
    leftY = obstacle[1][1]
    if(slideLeft(leftX,leftY,board) != None):
        newStates.append(slideLeft(leftX,leftY,board))
    return newStates

#generate vertical states
def verticalState(board, obstacle):
    newStates = []
    downX = obstacle[-1][0]
    downY = obstacle[-1][1] 
    if(slideDown(downX,downY,board) != None):
        newStates.append(slideDown(downX,downY,board))
    upX = obstacle[1][0]
    upY = obstacle[1][1]
    if(slideUp(upX,upY,board) != None):
        newStates.append(slideUp(upX,upY,board))
    return newStates



