# This file is where I include the minimax algorithm for my chess AI which calls the neural network.


import copy
from BackEndChess import *
from ChessBoard import *
import random
import NeuralNet
import ast

#myNet.feedForward([.01,.01,.01,.01,.01,.01,.01,.01, .02,.03,.04,.05,.06,.02,.03,.04, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, .01,.01,.01,.01,.01,.01,.01,.01, .02,.03,.04,.05,.06,.02,.03,.04])
#print(myNet.getResults())
#myNet.feedForward([-.01,-.01,-.01,.01,.01,.01,.01,.01, .02,.03,.04,.05,.06,.02,.03,.04, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, .01,.01,.01,.01,.01,.01,.01,.01, .02,.03,.04,.05,.06,.02,.03,.04])
#print(myNet.getResults())
#myNet.feedForward([.1,.1,.1,.1,.1,.1,.1,.1, .2,.3,.4,.5,.6,.2,.3,.4, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, .1,.1,.1,.1,.1,.1,.1,.1, .2,.3,.4,.5,.6,.2,.3,.4])
#print(myNet.getResults())
#myNet.feedForward([-.1,-.1,-.1,.1,.1,.1,.1,.1, .2,.3,.4,.5,.6,.2,.3,.4, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, .1,.1,.1,.1,.1,.1,.1,.1, .2,.3,.4,.5,.6,.2,.3,.4])
#print(myNet.getResults())

# Converts string of weights to actual list of weights.
with open("/Users/michaelkronovet/Desktop/15-112/FinalProject/RealWeights/RealWeights9.txt", "r") as myfile:
    weightsF = myfile.read().replace('\n', '')
weightsL = ast.literal_eval(weightsF)

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
#    print("INPUTS", tBoard)
    return tBoard

# Makes dictionary of all moves where each object has its own list of moves.
def getAllMoves(board, AIcolor):
    allMoves = dict()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != None and board[row][col].color == AIcolor:
                board[row][col].getMoves(board)
                allMoves[board[row][col]] = board[row][col].moves
    return allMoves

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
            # Evaulate would be the neural network evaluation function
            tBoard = translateBoard(tempB)
            score = minPart(tempB, 0, "White")
            if sum(tBoard) < sum(curBoard):
                newSum = (sum(tBoard)*-1 + sum(curBoard))*100
                print("TAKEMOVE", newSum)
                print("MINISCORE", score)
                if abs(score) <= abs(newSum):
#                    score = sum(tBoard)*-1
                    score = newSum
            if score > bestScore:
                bestMove = [key, move]
                bestScore = score
    print("MINPARTSCORE", minPart(tempB, 0, "White"))  
    print("SCORE", bestScore)
    return makeMove(bestMove, board)

def makeMove(bestMove, board):
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