#swap two elements in a list
def swap(curr, pos1, pos2):
    curr = list(curr)
    curr[pos1], curr[pos2] = curr[pos2], curr[pos1]
    return ''.join(curr)


# returns slide one step to the right with the X and Y position of rightmost element
def slideRight(posX, posY, board):
    currBoard = board.copy()
    if (posX == 5):
        return None
    rowToChange = currBoard[posY] 
    charLabel = rowToChange[posX]
    if(rowToChange[posX + 1] == '-'):
        for i in range(len(rowToChange) - 2, -1, -1): # decrementing loop
            if (rowToChange[i] == charLabel):
                rowToChange = swap(rowToChange, i, i + 1)
        currBoard[posY] = rowToChange
    else:
        return None
    return currBoard

# returns slide one step to the left with the X and Y position of leftmost element
def slideLeft(posX, posY, board):
    currBoard = board.copy()
    if (posX == 0):
        return None
    rowToChange = currBoard[posY] 
    charLabel = rowToChange[posX]
    if(rowToChange[posX - 1] == '-'):
        for i in range(len(rowToChange)):
            if (rowToChange[i] == charLabel):
                rowToChange = swap(rowToChange, i - 1, i)
        currBoard[posY] = rowToChange
    else:
        return None
    return currBoard


# returns slide up one step with the X and Y position of uppermost element
def slideUp(posX, posY, board):
    currBoard = board.copy()
    if (posY == 0):
        return
    rowFirstEle = currBoard[posY] 
    charLabel = rowFirstEle[posX]
    #error handling
    if (currBoard[posY - 1][posX] == '-'):
        for i in range(6):
            searchString = list(currBoard[i])
            if (searchString[posX] == charLabel):
                swapUp = list(currBoard[i - 1])
                searchString[posX] = swapUp[posX]
                swapUp[posX] = charLabel
                #revert to string to place in currBoard
                swapUpStr = ''.join(swapUp)
                searchStringtoStr = ''.join(searchString)
                currBoard[i - 1] = swapUpStr
                currBoard[i] = searchStringtoStr
    else:
        return None
    return currBoard

# returns slide down one step with the X and Y position of lowermost element
def slideDown(posX, posY, board):
    currBoard = board.copy()
    if (posY == 5):
        return
    rowFirstEle = currBoard[posY] 
    charLabel = rowFirstEle[posX]
    #error handling
    if (currBoard[posY + 1][posX] == '-'):
        for i in range(5, -1, -1): # changed second value to -1
            searchString = list(currBoard[i])
            if (searchString[posX] == charLabel):
                swapDown = list(currBoard[i + 1])
                searchString[posX] = swapDown[posX]
                swapDown[posX] = charLabel
                #revert to strings to place in currBoard
                swapDownStr = ''.join(swapDown)
                searchStringtoStr = ''.join(searchString)
                currBoard[i + 1] = swapDownStr
                currBoard[i] = searchStringtoStr
    else:
        return None
    return currBoard
