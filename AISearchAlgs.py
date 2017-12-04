# This file is where I include the minimax algorithm for my chess AI which 
# calls the neural network when it needs to evaluate a chess board.


import copy
from BackEndChess import *
from ChessBoard import *
import random
import NeuralNet
import ast

# Converts string of weights to actual list of weights.
with open("/Users/michaelkronovet/Desktop/15-112/FinalProject/RealWeights/RealWeights9.txt", "r") as myfile:
    weightsF = myfile.read().replace('\n', '')
weightsL = ast.literal_eval(weightsF)

# Sets neural network weights to the weights stored in the text file.
myNet = NeuralNet.Net([64, 44, 18, 1])
for layer in range(len(myNet.layers)-1):
    for neuron in range(len(myNet.layers[layer])):
        myNet.layers[layer][neuron].outputWeights = weightsL[layer][neuron]

# Translates the chess board that is in the game to a form which is readable by the neural network.
def translateBoard(board):
    tBoard = []
    for row in range(7, -1, -1):
        for col in range(8):
            if board[row][col] != None:
                if isinstance(board[row][col], Pawn):
                    if board[row][col].color == "White":
                        tBoard.append(.01)
                    else:
                        tBoard.append(-.01)
                elif isinstance(board[row][col], Knight):
                    if board[row][col].color == "White":
                        tBoard.append(.02)
                    else:
                        tBoard.append(-.02)
                if isinstance(board[row][col], Bishop):
                    if board[row][col].color == "White":
                        tBoard.append(.03)
                    else:
                        tBoard.append(-.03)
                if isinstance(board[row][col], Rook):
                    if board[row][col].color == "White":
                        tBoard.append(.04)
                    else:
                        tBoard.append(-.04)
                if isinstance(board[row][col], Queen):
                    if board[row][col].color == "White":
                        tBoard.append(.05)
                    else:
                        tBoard.append(-.05)
                if isinstance(board[row][col], King):
                    if board[row][col].color == "White":
                        tBoard.append(.06)
                    else:
                        tBoard.append(-.06)
            else:
                tBoard.append(0.0)
    return tBoard

# Makes dictionary of all moves where each piece object has its own list of moves.
def getAllMoves(board, AIcolor):
    allMoves = dict()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != None and board[row][col].color == AIcolor:
                board[row][col].getMoves(board)
                allMoves[board[row][col]] = board[row][col].moves
    return allMoves

# This is the minimax search algorithm.
def minimaxSearch(board, AIcolor, data):
    allMoves = getAllMoves(board, AIcolor)
    bestScore = float("-inf")
    curBoard = translateBoard(board)
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
            tBoard = translateBoard(tempB)
            score = minPart(tempB, 0, "White")
            if sum(tBoard) < sum(curBoard):
                newSum = (sum(tBoard)*-1 + sum(curBoard))*100
                if abs(score) <= abs(newSum):
#                    score = sum(tBoard)*-1
                    score = newSum
            if score > bestScore:
                bestMove = [key, move]
                bestScore = score
    return makeMove(bestMove, board)

# Given a move and a board, this function makes the move.
def makeMove(bestMove, board):
    board[bestMove[1][0]][bestMove[1][1]] = bestMove[0]
    board[bestMove[0].posRow][bestMove[0].posCol] = None
    board[bestMove[1][0]][bestMove[1][1]].posRow = bestMove[1][0]
    board[bestMove[1][0]][bestMove[1][1]].posCol = bestMove[1][1]
    return board

# Used to find which move is the best for the human player in response to the AI's move.
def minPart(gameBoard, level, color):
    if level == 1:
        tBoard = translateBoard(gameBoard)
        myNet.feedForward(tBoard)
        return myNet.getResults()
    bestScore = float("inf")
    newMoves = getAllMoves(gameBoard, color)
    curSum = sum(translateBoard(gameBoard))
    for key in newMoves:
        for move in newMoves[key]:
            objCopy = copy.deepcopy(key)
            tempB = copy.deepcopy(gameBoard)
            tempB[move[0]][move[1]] = objCopy
            tempB[objCopy.posRow][objCopy.posCol] = None
            objCopy.posRow = move[0]
            objCopy.posCol = move[1]
            tBoard = translateBoard(tempB)
            newSum = sum(tBoard)
            if newSum > curSum:
                score = (newSum*-1+curSum)*100
            else:
                score = maxPart(tempB, level+1, "Black")
            newT = copy.deepcopy(tempB)
            if isCheck(newT, "White"):
                continue
            if score < bestScore:
                bestScore = score
    return bestScore

# Used to find what the best response is for the AI after the human player has made his/her move.
# Currently just returns an evaluatation of the board using the neural network because going through
# an additional layer would take too much time.
def maxPart(gameBoard, level, color):
    if level == 1:
        tBoard = translateBoard(gameBoard)
        myNet.feedForward(tBoard)
        return myNet.getResults()
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
                bestScore = score
    return bestScore