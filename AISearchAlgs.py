import copy
from BackEndChess import *
from ChessBoard import *
import random
import NeuralNet
import ast

with open("/Users/michaelkronovet/Desktop/15-112/FinalProject/TrainedWeightsAttempt1.txt", "r") as myfile:
    weightsF=myfile.read().replace('\n', '')

#weightsL = ast.literal_eval(weightsF)

myNet = NeuralNet.Net([64, 44, 18, 1])
for layer in range(len(myNet.layers)):
    for neuron in range(len(myNet.layers[layer])):
        myNet.layers[layer][neuron]
        

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
            newT = copy.deepcopy(tempB)
            if isCheck(newT, "Black"):
                continue
            # Evaulate would be the neural network evaluation function
            score = minPart(tempB, 0, "White")
            if score > bestScore:
                bestMove = [key, move]
                bestScore = score
    board[bestMove[1][0]][bestMove[1][1]] = bestMove[0]
    board[bestMove[0].posRow][bestMove[0].posCol] = None
    board[bestMove[1][0]][bestMove[1][1]].posRow = bestMove[1][0]
    board[bestMove[1][0]][bestMove[1][1]].posCol = bestMove[1][1]
    return board

def evaluate(board):
    return random.uniform(0,1)

def minPart(gameBoard, level, color):
    if level == 1:
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
            newT = copy.deepcopy(tempB)
            if isCheck(newT, "White"):
                continue
            score = maxPart(tempB, level+1, "Black")
            if score < bestScore:
                bestMove = move
                bestScore = score
    return bestScore

def maxPart(gameBoard, level, color):
    if level == 1:
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
            newT = copy.deepcopy(tempB)
            if isCheck(newT, "Black"):
                continue
            score = minPart(tempB, level+1, "White")
            if score > bestScore:
                bestMove = move
                bestScore = score
    return bestScore