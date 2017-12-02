
# Neural network segmentations:
    # First part is global game state (number and types of pieces on each side and which side is moving)
    # Location of each distinct piece on each side
    # Where each piece attacks and defends


# Citation:
# Neural network in C++ tutorial. Used ideas for updating weights and neural network implementation.
# https://www.youtube.com/watch?v=KkwX7FkLfug


# How Neural Network Works:
# It is used as the evaluation function for determining how good a certain chessboard is.
# Each input neuron indicates a square on the board.
# White pieces are given positive values while black pieces are given negative values.
# Each piece is assigned a number (Empty = 0, Pawn = 1, Knight = 2, Bishop = 3, Rook = 4, Queen = 5, King = 6)

import random
import math

class Net(object):
    def __init__(self, topology):
        numLayers = len(topology)
        self.topology = topology
        self.layers = []
        for layerNum in range(len(topology)):
            tempLayers = []
            if layerNum == len(topology)-1:
                numOutputs = 0
            else:
                numOutputs = topology[layerNum+1]
            for neuronNum in range(topology[layerNum]+1):
                tempLayers.append(Neuron(numOutputs, neuronNum))
            self.layers.append(tempLayers)
            self.layers[-1][-1].outputVal = 1.0

    def getResults(self):
        return self.layers[-1][0].outputVal

    def backProp(self, targetVal):
        self.layers[-1][0].calcOutputGradients(targetVal)
        for layerNum in range(len(self.layers)-2, 0, -1):
            hiddenLayer = self.layers[layerNum]
            nextLayer = self.layers[layerNum + 1]
            for n in range(len(hiddenLayer)):
                hiddenLayer[n].calcHiddenGradients(nextLayer)
        for layerNum in range(len(self.layers)-1, 0, -1):
            layer = self.layers[layerNum]
            prevLayer = self.layers[layerNum-1]
            for n in range(len(layer)-1):
                layer[n].updateInputWeights(prevLayer)

    def feedForward(self, inputVals):
        for i in range(len(inputVals)):
            self.layers[0][i].outputVal = inputVals[i]
        for layerNum in range(1, len(self.layers)):
            prevLayer = self.layers[layerNum-1]
            for n in range(len(self.layers[layerNum])-1):
                self.layers[layerNum][n].feedForward(prevLayer)


class Neuron(object):
    learningRate = .15
    pcm = .5
    def __init__(self, numOutputs, myIndex):
        self.outputWeights = []
        self.myIndex = myIndex
        self.outputVal = 0
        self.gradient = 0
        for i in range(numOutputs):
            self.outputWeights.append([random.uniform(0,1),0])

    def updateInputWeights(self, prevL):
        for i in range(len(prevL)):
            oldDeltaWeight = prevL[i].outputWeights[self.myIndex][1]
            newDeltaWeight = Neuron.learningRate*prevL[i].outputVal*self.gradient+Neuron.pcm*oldDeltaWeight
            prevL[i].outputWeights[self.myIndex][1] = newDeltaWeight
            prevL[i].outputWeights[self.myIndex][0] += newDeltaWeight
    
    def calcHiddenGradients(self, nextLayer):
        sum = 0.0
        for i in range(len(nextLayer)-1):
            sum += self.outputWeights[i][0]*nextLayer[i].gradient
        self.gradient = sum*self.outputVal
        
    def calcOutputGradients(self, targetVal):
        delta = targetVal-self.outputVal
        self.gradient = delta

    @staticmethod
    def transferFunction(x):
        return math.tanh(x)

    def feedForward(self, prevLayer):
        sum = 0.0
        for i in range(len(prevLayer)):
            sum += prevLayer[i].outputVal*prevLayer[i].outputWeights[self.myIndex][0]
        self.outputVal = self.transferFunction(sum)