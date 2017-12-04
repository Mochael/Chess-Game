# This file includes the neural network that I made to evaluate given boards.

# Citation:
# Neural network in C++ tutorial. Used ideas for updating weights and neural network implementation.
# https://www.youtube.com/watch?v=KkwX7FkLfug

# Structure of Neural Network:
# Each input neuron indicates a square on the board.
# White pieces are given positive values while black pieces are given negative values.
# Each piece is assigned a number (Empty = 0, Pawn = .01, Knight = .02, Bishop = .03, Rook = .04, Queen = .05, King = .06)

import random
import math

# Network class of the entire network
class Net(object):
    # Initializes a neural network with random weights.
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

    # Returns the final output of the neural network.
    def getResults(self):
        return self.layers[-1][0].outputVal

    # Updates the weights of the neural network based off of the target value when training.
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

    # Given certain input neurons this has the neural network run those inputs through the network.
    def feedForward(self, inputVals):
        for i in range(len(inputVals)):
            self.layers[0][i].outputVal = inputVals[i]
        for layerNum in range(1, len(self.layers)):
            prevLayer = self.layers[layerNum-1]
            for n in range(len(self.layers[layerNum])-1):
                self.layers[layerNum][n].feedForward(prevLayer)

# Used to make individual neuron objects.
class Neuron(object):
    learningRate = .15
    pcm = .5
    # Initializes neuron that is fully connected to every neuron in the next layer with random weights.
    def __init__(self, numOutputs, myIndex):
        self.outputWeights = []
        self.myIndex = myIndex
        self.outputVal = 0
        self.gradient = 0
        for i in range(numOutputs):
            self.outputWeights.append([random.uniform(0,.1),0])

    # This is used when backpropagating through the network to update weights based off the target value.
    def updateInputWeights(self, prevL):
        for i in range(len(prevL)):
            oldDeltaWeight = prevL[i].outputWeights[self.myIndex][1]
            newDeltaWeight = Neuron.learningRate*prevL[i].outputVal*self.gradient+Neuron.pcm*oldDeltaWeight
            prevL[i].outputWeights[self.myIndex][1] = newDeltaWeight
            prevL[i].outputWeights[self.myIndex][0] += newDeltaWeight
    
    # Calculates gradient of neurons in the hidden layer to determine which direction
    # the hidden layer outputs should go.
    def calcHiddenGradients(self, nextLayer):
        sum = 0.0
        for i in range(len(nextLayer)-1):
            sum += self.outputWeights[i][0]*nextLayer[i].gradient
        self.gradient = sum*self.transferFunctionDerivative(self.outputVal)

    # Calculates the gradient of the output to determine which direction the value converge
    # to to reach a global maximum.
    def calcOutputGradients(self, targetVal):
        delta = targetVal-self.outputVal
        self.gradient = delta*self.transferFunctionDerivative(self.outputVal)

    # Converges the outputs of the neurons (aside from input neurons) as values between -1 to 1
    # using the hyperbolic tangent graph as the activation function.
    @staticmethod
    def transferFunction(x):
        return math.tanh(x)

    # Derivative of hyperbolic tangent is used to approximate gradients of outputs.
    @staticmethod
    def transferFunctionDerivative(x):
        return 1-(math.tanh(x))**2

    # This determines the new output for a neuron as the sum of the weights times the corresponding
    # outputs of the previous layer when put through the activiation function.
    def feedForward(self, prevLayer):
        sum = 0.0
        for i in range(len(prevLayer)):
            sum += prevLayer[i].outputVal*prevLayer[i].outputWeights[self.myIndex][0]
        self.outputVal = self.transferFunction(sum)