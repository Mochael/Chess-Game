import random
import math

def activationFunction(x):
   return 1.0 / (1.0 + math.exp(-x))

class Node:
   def __init__(self):
      self.lastOutput = None
      self.lastInput = None
      self.error = None
      self.outgoingEdges = []
      self.incomingEdges = []
      self.addBias()

   def addBias(self):
      self.incomingEdges.append(Edge(BiasNode(), self))

   def evaluate(self, inputVector):
      if self.lastOutput is not None:
         return self.lastOutput

      self.lastInput = []
      weightedSum = 0

      for e in self.incomingEdges:
         theInput = e.source.evaluate(inputVector)
         self.lastInput.append(theInput)
         weightedSum += e.weight * theInput

      self.lastOutput = activationFunction(weightedSum)
      self.evaluateCache = self.lastOutput
      return self.lastOutput

   def getError(self, label):
      ''' Get the error for a given node in the network. If the node is an
         output node, label will be used to compute the error. For an input node, we
         simply ignore the error. '''

      if self.error is not None:
         return self.error

      assert self.lastOutput is not None

      if self.outgoingEdges == []: # this is an output node
         self.error = label - self.lastOutput
      else:
         self.error = sum([edge.weight * edge.target.getError(label) for edge in self.outgoingEdges])

      return self.error

   def updateWeights(self, learningRate):
      ''' Update the weights of a node, and all of its successor nodes.
         Assume self is not an InputNode. If the error, lastOutput, and
         lastInput are None, then this node has already been updated. '''

      if (self.error is not None and self.lastOutput is not None
            and self.lastInput is not None):

         for i, edge in enumerate(self.incomingEdges):
            edge.weight += (learningRate * self.lastOutput * (1 - self.lastOutput) *
                           self.error * self.lastInput[i])

         for edge in self.outgoingEdges:
            edge.target.updateWeights(learningRate)

         self.error = None
         self.lastInput = None
         self.lastOutput = None

   def clearEvaluateCache(self):
      if self.lastOutput is not None:
         self.lastOutput = None
         for edge in self.incomingEdges:
            edge.source.clearEvaluateCache()


class InputNode(Node):
   ''' Input nodes simply evaluate to the value of the input for that index.
    As such, each input node must specify an index. We allow multiple copies
    of an input node with the same index (why not?). '''

   def __init__(self, index):
      Node.__init__(self)
      self.index = index;

   def evaluate(self, inputVector):
      self.lastOutput = inputVector[self.index]
      return self.lastOutput

   def updateWeights(self, learningRate):
      for edge in self.outgoingEdges:
         edge.target.updateWeights(learningRate)

   def getError(self, label):
      for edge in self.outgoingEdges:
         edge.target.getError(label)

   def addBias(self):
      pass

   def clearEvaluateCache(self):
      self.lastOutput = None


class BiasNode(InputNode):
   def __init__(self):
      Node.__init__(self)

   def evaluate(self, inputVector):
      return 1.0


class Edge:
   def __init__(self, source, target):
      self.weight = random.uniform(0,1)
      self.source = source
      self.target = target

      # attach the edges to its nodes
      source.outgoingEdges.append(self)
      target.incomingEdges.append(self)


class Network:
   def __init__(self):
      self.inputNodes = []
      self.outputNode = None

   def evaluate(self, inputVector):
      print(inputVector)
      assert max([v.index for v in self.inputNodes]) < len(inputVector)
      self.outputNode.clearEvaluateCache()

      output = self.outputNode.evaluate(inputVector)
      return output

   def propagateError(self, label):
      for node in self.inputNodes:
         node.getError(label)

   def updateWeights(self, learningRate):
      for node in self.inputNodes:
         node.updateWeights(learningRate)

   def train(self, labeledExamples, learningRate=0.9, maxIterations=10000):
      while maxIterations > 0:
         print("EXAMPLE", labeledExamples)
         output = self.evaluate(labeledExamples[0])
         print("OUTPUT", output)
         self.propagateError(labeledExamples[1])
         self.updateWeights(learningRate)

         maxIterations -= 1

    




'''#Backpropagation algorithm written in Python by annanay25.
import string
import math
import random

class Neural:
	def __init__(self, pattern):
		#
		# Lets take 2 input nodes, 3 hidden nodes and 1 output node.
		# Hence, Number of nodes in input(ni)=2, hidden(nh)=3, output(no)=1.
		#
		self.ni=3
		self.nh=3
		self.no=1

		#
		# Now we need node weights. We'll make a two dimensional array that maps node from one layer to the next.
		# i-th node of one layer to j-th node of the next.
		#
		self.wih = []
		for i in range(self.ni):
			self.wih.append([0.0]*self.nh)

		self.who = []
		for j in range(self.nh):
			self.who.append([0.0]*self.no)

		#
		# Now that weight matrices are created, make the activation matrices.
		#
		self.ai, self.ah, self.ao = [],[],[]
		self.ai=[1.0]*self.ni
		self.ah=[1.0]*self.nh
		self.ao=[1.0]*self.no

		#
		# To ensure node weights are randomly assigned, with some bounds on values, we pass it through randomizeMatrix()
		#
		randomizeMatrix(self.wih,-0.2,0.2)
		randomizeMatrix(self.who,-2.0,2.0)

		#
		# To incorporate momentum factor, introduce another array for the 'previous change'.
		#
		self.cih = []
		self.cho = []
		for i in range(self.ni):
			self.cih.append([0.0]*self.nh)
		for j in range(self.nh):
			self.cho.append([0.0]*self.no)

	# backpropagate() takes as input, the patterns entered, the target values and the obtained values.
	# Based on these values, it adjusts the weights so as to balance out the error.
	# Also, now we have M, N for momentum and learning factors respectively.
	def backpropagate(self, inputs, expected, output, N=0.5, M=0.1):
		# We introduce a new matrix called the deltas (error) for the two layers output and hidden layer respectively.
		output_deltas = [0.0]*self.no
		for k in range(self.no):
			# Error is equal to (Target value - Output value)
			error = expected[k] - output[k]
			output_deltas[k]=error*dsigmoid(self.ao[k])

		# Change weights of hidden to output layer accordingly.
		for j in range(self.nh):
			for k in range(self.no):
				delta_weight = self.ah[j] * output_deltas[k]
				self.who[j][k]+= M*self.cho[j][k] + N*delta_weight
				self.cho[j][k]=delta_weight

		# Now for the hidden layer.
		hidden_deltas = [0.0]*self.nh
		for j in range(self.nh):
			# Error as given by formule is equal to the sum of (Weight from each node in hidden layer times output delta of output node)
			# Hence delta for hidden layer = sum (self.who[j][k]*output_deltas[k])
			error=0.0
			for k in range(self.no):
				error+=self.who[j][k] * output_deltas[k]
			# now, change in node weight is given by dsigmoid() of activation of each hidden node times the error.
			hidden_deltas[j]= error * dsigmoid(self.ah[j])

		for i in range(self.ni):
			for j in range(self.nh):
				delta_weight = hidden_deltas[j] * self.ai[i]
				self.wih[i][j]+= M*self.cih[i][j] + N*delta_weight
				self.cih[i][j]=delta_weight

	# Main testing function. Used after all the training and Backpropagation is completed.
	def test(self, patterns):
		for p in patterns:
			inputs = p[0]
			print 'For input:', p[0], ' Output -->', self.runNetwork(inputs), '\tTarget: ', p[1]


	# So, runNetwork was needed because, for every iteration over a pattern [] array, we need to feed the values.
	def runNetwork(self, feed):
		if(len(feed)!=self.ni-1):
			print 'Error in number of input values.'

		# First activate the ni-1 input nodes.
		for i in range(self.ni-1):
			self.ai[i]=feed[i]

		#
		# Calculate the activations of each successive layer's nodes.
		#
		for j in range(self.nh):
			sum=0.0
			for i in range(self.ni):
				sum+=self.ai[i]*self.wih[i][j]
			# self.ah[j] will be the sigmoid of sum. # sigmoid(sum)
			self.ah[j]=sigmoid(sum)

		for k in range(self.no):
			sum=0.0
			for j in range(self.nh):
				sum+=self.ah[j]*self.wih[j][k]
			# self.ah[k] will be the sigmoid of sum. # sigmoid(sum)
			self.ao[k]=sigmoid(sum)

		return self.ao


	def trainNetwork(self, pattern):
		for i in range(500):
			# Run the network for every set of input values, get the output values and Backpropagate them.
			for p in pattern:
				# Run the network for every tuple in p.
				inputs = p[0]
				out = self.runNetwork(inputs)
				expected = p[1]
				self.backpropagate(inputs,expected,out)
		self.test(pattern)

# End of class.


def randomizeMatrix ( matrix, a, b):
	for i in range ( len (matrix) ):
		for j in range ( len (matrix[0]) ):
			# For each of the weight matrix elements, assign a random weight uniformly between the two bounds.
			matrix[i][j] = random.uniform(a,b)


# Now for our function definition. Sigmoid.
def sigmoid(x):
	return 1 / (1 + math.exp(-x))


# Sigmoid function derivative.
def dsigmoid(y):
	return y * (1 - y)


def main():
	# take the input pattern as a map. Suppose we are working for AND gate.
	pat = [
		[[0,0], [0]],
		[[0,1], [1]],
		[[1,0], [1]],
		[[1,1], [1]]
	]
	newNeural = Neural(pat)
	newNeural.trainNetwork(pat)


if __name__ == "__main__":
	main()'''