########## Neural Network ##########
# Number of nodes, layers, starting values are built into computation graph
# Run session with optimizer that will start managing the weights based on cost fujnction that is built into the computation graph.
# When using tensor flow you just have to specifiy the cost function you do not need to specify how it does backpropogation.

# 2 Parts to Building Neural Network in Tensor Flow: 1. build computation graph 2. build what's supposed to happen in the session.



# Neural network segmentations:
    # First part is global game state (number and types of pieces on each side and which side is moving)
    # Location of each distinct piece on each side
    # Where each piece attacks and defends

import random

##### Network Functions #####
def makeGlobalInputs():
    pass
def makeDistinctInputs():
    pass
def makeAttackingInputs():
    pass

class Net(object):
    def __init__(self, topology):
        self.topology = topology
        self.layers = []
        self.recentAverageSmoothingFactor = 100.0
        self.error = 0
        self.recentAverageError = 0

        for layerNum in range(len(topology)):
            tempLayers = []
            if layerNum == len(topology)-1:
                numOutputs = 0
            else:
                numOutputs = topology[layerNum+1]
            for neuronNum in range(topology[layerNum]):
                tempLayers.append(Neuron(numOutputs, neuronNum))
                print("Made a Neuron!")
            self.layers.append(tempLayers)
            self.layers[-1][-1].setOutputVal(1.0)

    def getRecentAverageError(self):
        return self.recentAverageError
        
    def getResults(self, resultVals):
        resultVals = []
        for i in range(len(self.layers[-1])-1):
            resultVals.append(self.layers[-1][i].getOutputVal())

    def backProp(self, targetVals):
        outputLayer = self.layers[-1]
        self.error = 0.0
        for i in range(len(outputLayer.size())-1):
            delta = targetVals[i]-outputLayer[i].getOutputVal()
            self.error += delta*delta
        self.error /= len(outputLayer)-1
        self.error = self.error**.5
        self.recentAverageError = (self.recentAverageError*self.recentAverageSmoothingFactor+self.error)/(self.recentAverageSmoothingFactor + 1.0)
        for j in range(len(outputLayer)-1):
            outputLayer[j].calcOutputGradients(targetVals[j])
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
        assert(len(inputVals) == len(self.layers[0])-1)
        for i in range(len(inputVals)):
            self.layers[0][i].setOutputVal(inputVals[i])
        for layerNum in range(len(self.layers)):
            prevLayer = self.layers[layerNum - 1]
            for n in range(len(self.layers[layerNum])-1):
                self.layers[layerNum][n].feedForward(prevLayer)


##### Neuron Functions #####

class Neuron(object):
    eta = .15
    alpha = .5
    def __init__(self, numOutputs, myIndex):
        self.outputWeights = []
        self.myIndex = myIndex
#        self.connects = connects
        self.outputVal = 0
        self.gradient = 0
        for i in range(numOutputs):
            self.outputWeights.append([random.uniform(0,1),0])

    def setOutputVal(self, val):
        self.outputVal = val
        
    def getOutputVal(self):
        return self.outputVal

    def updateInputWeights(self, prevL):
        for i in range(len(prevL)):
            neuron = prevL[n]
            oldDeltaWeight = self.outputWeights[myIndex][1]
            newDeltaWeight = Neuron.eta*neuron.getOutputVal()*self.gradient+Neuron.alpha*oldDeltaWeight
            self.outputWeights[self.myIndex][1] = newDeltaWeight
            self.outputWeights[self.myIndex][0] += newDeltaWeight

    def sumDOW(self, nextLayer):
        sum = 0.0
        for i in range(len(nextLayer)):
            sum += self.outputWeights[n][0]*nextLayer[n].gradient
        return sum
    
    def calcHiddenGradients(self, nextLayer):
        dow = sumDOW(nextLayer)
        self.gradient = dow*transferFunctionDerivative(self.outputVal)
        
    def calcOutputGradients(self, targetVal):
        delta = targetVal-self.outputVal
        gradient = delta*self.transferFunctionDerivative(self.outputVal)

    @staticmethod
    def transferFunction(x):
        return tanh(x)

    @staticmethod
    def transferFunctionDerivative(x):
        return 1.0-x*x

    def feedForward(self, prevLayer):
        sum = 0.0
        for i in range(len(prevLayer)):
            sum += prevLayer[i].getOutputVal()*prevLayer[i].outputWeights[self.myIndex][0]
        self.outputVal = transferFunction(sum)

# We need to declare the topology (outline of network, [3,2,1] indicates 3 layer network with 3 input neurons, 2 neurons in a single hidden layer, and 1 output neuron.
topology = [ 3, 2, 1 ]
numLayers = len(topology)
print(Net(topology))