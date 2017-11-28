import copy
from BackEndChess import *
from ChessBoard import *
# Minimax

# Makes dictionary of all moves where each object has its own list of moves.
def getAllMoves(board, AIcolor):
    allMoves = dict()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != None and board[row][col].color == AIcolor:
                if board[row][col] in allMoves:
                    allMoves[board[row][col]].extend(board[row][col].moves)
                else:
                    board[row][col].getMoves(board)
                    allMoves[board[row][col]] = board[row][col].moves
    return allMoves

def minimaxSearch(board, AIcolor):
    allMoves = getAllMoves(board, AIcolor)
    bestScore = float("-inf")
    for key in allMoves:
        for move in allMoves[key]:
            objCopy = copy.deepcopy(key)
            tempB = copy.deepcopy(board)
            tempB[move[0]][move[1]] = objCopy
            tempB[objCopy.posRow][objCopy.posCol] = None
            objCopy.posRow = move[0]
            objCopy.posCol = move[1]
            # Evaulate would be the neural network evaluation function
            if AIcolor == "White":
                score = minPart(tempB, 0, "Black")
            else:
                score = minPart(tempB, 0, "White")
            if score > bestScore:
                bestMove = [key, move]
                bestScore = score
    return bestMove


def minPart(gameBoard, level, color):
    if level == 2:
        return evaluate(gameBoard)
    bestScore = float("inf")
    newMoves = getAllMoves(gameBoard, color)
    for key in newMoves:
        for move in newMoves[key]:
            objCopy = copy.deepcopy(key)
            tempB = copy.deepcopy(gameBoard)
            tempB[move[0]][move[1]] = objCopy
            tempB[objCopy.posRow][objCopy.posCol] = None
            objCopy.posRow = move[0]
            objCopy.posCol = move[1]
            if color == "White":
                score = maxPart(tempB, 0, "Black")
            else:
                score = maxPart(tempB, 0, "White")
            if score < bestScore:
                bestMove = move
                bestScore = score
    return bestScore

def maxPart(gameBoard, level, color):
    if level == 2:
        return evaluate(gameBoard)
    bestScore = float("-inf")
    newMoves = getAllMoves(gameBoard, color)
    for key in newMoves:
        for move in newMoves[key]:
            objCopy = copy.deepcopy(key)
            tempB = copy.deepcopy(gameBoard)
            tempB[move[0]][move[1]] = objCopy
            tempB[objCopy.posRow][objCopy.posCol] = None
            objCopy.posRow = move[0]
            objCopy.posCol = move[1]
            if color == "White":
                score = minPart(tempB, 0, "Black")
            else:
                score = minPart(tempB, 0, "White")
            if score > bestScore:
                bestMove = move
                bestScore = score
    return bestScore