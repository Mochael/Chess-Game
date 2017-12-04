import copy
from BackEndChess import *
from ChessBoard import *
import random
import NeuralNet
import ast

with open("/Users/michaelkronovet/Desktop/15-112/FinalProject/TrainedWeightsText.txt", "r") as myfile:
    weightsF = myfile.read().replace('\n', '')

weightsL = ast.literal_eval(weightsF)
print(weightsL)

myNet = NeuralNet.Net([64, 44, 18, 1])
for layer in range(len(myNet.layers)-1):
    for neuron in range(len(myNet.layers[layer])):
        myNet.layers[layer][neuron].outputWeights = weightsL[layer][neuron]
        

def translateBoard(board):
    tBoard = []
    for row in range(7, -1, -1):
        for col in range(8):
            if board[row][col] != None:
                if isinstance(board[row][col], Pawn):
                    if board[row][col].color == "White":
                        tBoard.append(1)
                    else:
                        tBoard.append(-1)
                elif isinstance(board[row][col], Knight):
                    if board[row][col].color == "White":
                        tBoard.append(2)
                    else:
                        tBoard.append(-2)
                if isinstance(board[row][col], Bishop):
                    if board[row][col].color == "White":
                        tBoard.append(3)
                    else:
                        tBoard.append(-3)
                if isinstance(board[row][col], Rook):
                    if board[row][col].color == "White":
                        tBoard.append(4)
                    else:
                        tBoard.append(-4)
                if isinstance(board[row][col], Queen):
                    if board[row][col].color == "White":
                        tBoard.append(5)
                    else:
                        tBoard.append(-5)
                if isinstance(board[row][col], King):
                    if board[row][col].color == "White":
                        tBoard.append(6)
                    else:
                        tBoard.append(-6)
            else:
                tBoard.append(0)
    return tBoard

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
        tBoard = translateBoard(gameBoard)
        return myNet.feedForward(tBoard)
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
        tBoard = translateBoard(gameBoard)
        return myNet.feedForward(tBoard)
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