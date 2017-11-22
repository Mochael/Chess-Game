######## IDEAS ##########
# Maze solver- race neural network to solve maze, race friends, build your own
# course or have program build random maze for you.

########## Neural Network ##########
# Number of nodes, layers, starting values are built into computation graph
# Run session with optimizer that will start managing the weights based on cost fujnction that is built into the computation graph.
# When using tensor flow you just have to specifiy the cost function you do not need to specify how it does backpropogation.

# 2 Parts to Building Neural Network in Tensor Flow: 1. build computation graph 2. build what's supposed to happen in the session.

######################################
# C++ Tutorial Network in Python

import random

##### Network Functions #####

'''class Net(object):
    def __init__(self, topology):
        self.topology = topology
        self.inputVals = len(self.topology[0])
        self.layerList = []
        
    def makeLayers(self, topology):
        numLayers = len(topology)
    for layerNum in range(len(numLayers)):
        self.layerList.append(layer)
        if layerNum == numLayers-1:
            outputCount = 0
        else:
            outputCount = topology[layerNum+1]
    # Plus 1 makes bias neuron.
        for neuronNum in range(topology[layerNum]+1):
            layer.append(neuron)

    def feedForward(inputs):
        for input in range(self.inputVals):
            self.layerList[0][input].setOutput(self.inputVals[input])

        for layerN in range(1, self.layerList):
            prevL = self.layerList[layerN-1]
            for n in range(0, self.layerList[layerN]):
                self.layerList[layerN][n].forwardProp()
    
    def backProp(targets):
        error = 0
        for n in range(0, len(outputLayers)):
            delta = targets[n]-outputLayers[n].getOutputVals()
        return None
    
    def getResults(results):
        return None
# We need to declare the topology (outline of network, [3,2,1] indicates 3 layer network with 3 input neurons, 2 neurons in a single hidden layer, and 1 output neuron.
topology = [ 3, 2, 1 ]
numLayers = len(topology)
layerList = []
# We need to declare/define layer in the layer functions and neuron in neuron functions.

##### Connections Struct #####
class Connections(object):
    def ___init___(self):
        self.weight = random.rand(0,1)
        #self.weightChange

##### Neuron Functions #####

class Neuron(object):
    learningRate = .15
    multiplier = .5
    def __init__(self, outputCount):
        self.outputCount = outputCount
# made this a dictionary where key = connected neuron, and val = weight of connection
        self.outputWeights = dict()
        for w in range(self.outputCount):
#            self.outputWeights[next neuron place] = random.uniform(0,1)
    
    def updateWeights(self):
        for i in range(Net.prevL):

    def setOutputWeights(self):
        for output in range(self.outputCount):
            weight = random.uniform(0,1)
            #self.outputWeights.append() a connection that was previously made.
    
    def errorSum(self):
        sum = 0
        for i in range(len(Net.nextLayer)):
            sum += outPutWeights[Net.nextLayer[i]]*Net.nextLayer[i].gradient
        return sum

    def hiddenGradients():
        error = 
    def outputGradients():


    def transFunct(self):
        return tan(x)

    def transDeriv(self):
        return 1-x**2

    def feedForward(self):
        sum = 0
        for n in range(0, prevLayer):
            sum += prevLayer[n].getOutputValue*prevLayer[n].outputWeights[index]'''


##### Layer Functions #####

# We will have a list called Layer that holds the information of each neuron in that layer.

######################################




# Another Idea: Stock Tracer Game/Investment Tool- neural networks analyzes stock and predicts future pattern. Also has a user interface that tells yuou exactly how much money you'd be losing at each instant if you invest in that stock and displays other similar possible stock options. Also has game feature where you run around a 3D version of the stock itself.

# Another Idea- Circuit maker where it is easier to use for inexperienced people and works like a game to teach people how to make circuits. Player plays as the current and based on what cirucit they make them maneuver around on and try to travel in the direction of the current.

# Genetic drawer- Takes picture of someone's face and makes drawing of it with polygons using genetic algorithm. Or, it could mimic the style of a famous artist with a neural network and repaint the person's face in that style.


# Tutorial mode: animations for user to learn how chess works and what the pieces do (maybe make a youtube video explaining rules).

# Training mode: user plays against AI that tells user why it is making those moves. Maybe in this mode the chess AI can give you a visual display of the succession of moves it plans to make and show you how the paths of the moves change as you make your own moves.

# Competitive mode: user plays AI from different difficulties

# Multiplayer: user can play against different players online

# Difference in AI difficulties could be how far the AI can see into the future with its move predictions.

from tkinter import *
from PIL import Image, ImageTk
import ChessBoard as CB
import BackEndChess as BackEnd

def startScreen(canvas, data):
    canvas.create_text(data.width/2, data.height/4,
                        text = "Welcome to Chess Trainer",
                        font = "courier "+str(int(data.width/25))+" underline")
    canvas.create_text(data.width/2, data.height/2,
                        text = "select one of the below options to begin",
                        font = "courier "+str(int(data.width/30)))
# Modes for player to select.
    canvas.create_rectangle(data.x1-data.r,data.y1-data.r,data.x1+data.r,data.y1+data.r,
                            fill = "grey")
    canvas.create_text(data.x1, data.y1,
                        text = "tutorial \n  mode", 
                        font = "courier "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_rectangle(data.x2-data.r,data.y2-data.r,data.x2+data.r,data.y2+data.r,
                            fill = "grey")
    canvas.create_text(data.x2, data.y2,
                        text = "training \n  mode", 
                        font = "courier "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_rectangle(data.x3-data.r,data.y3-data.r,data.x3+data.r,data.y3+data.r,
                            fill = "grey")
    canvas.create_text(data.x3, data.y3,
                        text = "competitive \n    mode", 
                        font = "courier "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_rectangle(data.x4-data.r,data.y4-data.r,data.x4+data.r,data.y4+data.r,
                            fill = "grey")
    canvas.create_text(data.x4, data.y4,
                        text = "multiplayer \n   mode", 
                        font = "courier "+str(int(data.width/44)),
                        fill = "black")

def tutorialScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill='white', width=0)
    canvas.create_text(15, 15, 
                       text = "Back",
                       font = "courier "+str(int(data.width/25)))
    canvas.create_text(data.width/2, data.height/2, 
                       text = "Search the link below to watch the tutorial",
                       font = "courier "+str(int(data.width/25)))
    canvas.create_text(data.width/2, data.height*3/4, 
                       text = "https://www.youtube.com/watch?v=t-uwGvx4V_A",
                       font = "courier "+str(int(data.width/30)))
    
def trainingScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill='white', width=0)
    data.mainBoard.drawBoard(canvas)
    canvas.create_text(15, 15, 
                       text = "Back",
                       font = "courier "+str(int(data.width/25)))
    if data.mainBoard.clicked:
        canvas.create_rectangle(data.mainBoard.margin+data.mainBoard.colClick*data.mainBoard.cellWidth,
                                data.mainBoard.margin+data.mainBoard.rowClick*data.mainBoard.cellHeight,
                                data.mainBoard.margin+(data.mainBoard.colClick+1)*data.mainBoard.cellWidth,
                                data.mainBoard.margin+(data.mainBoard.rowClick+1)*data.mainBoard.cellHeight,
                                fill = "yellow")
    initialize(canvas, data)
    drawImages(canvas, data)

def competitiveScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill='white', width=0)
    data.mainBoard.drawBoard(canvas)
    canvas.create_text(15, 15, 
                       text = "Back",
                       font = "courier "+str(int(data.width/25)))
    if data.mainBoard.clicked:
        canvas.create_rectangle(data.mainBoard.margin+data.mainBoard.colClick*data.mainBoard.cellWidth,
                                data.mainBoard.margin+data.mainBoard.rowClick*data.mainBoard.cellHeight,
                                data.mainBoard.margin+(data.mainBoard.colClick+1)*data.mainBoard.cellWidth,
                                data.mainBoard.margin+(data.mainBoard.rowClick+1)*data.mainBoard.cellHeight,
                                fill = "yellow")
    initialize(canvas, data)
    drawImages(canvas, data)

def multiplayerScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill='white', width=0)
    data.mainBoard.drawBoard(canvas)
    canvas.create_text(15, 15, 
                       text = "Back",
                       font = "courier "+str(int(data.width/25)))
    if data.mainBoard.clicked:
        canvas.create_rectangle(data.mainBoard.margin+data.mainBoard.colClick*data.mainBoard.cellWidth,
                                data.mainBoard.margin+data.mainBoard.rowClick*data.mainBoard.cellHeight,
                                data.mainBoard.margin+(data.mainBoard.colClick+1)*data.mainBoard.cellWidth,
                                data.mainBoard.margin+(data.mainBoard.rowClick+1)*data.mainBoard.cellHeight,
                                fill = "yellow")
    initialize(canvas, data)
    drawImages(canvas, data)


def gameMode(event, data):
    if data.mode != "beginning":
        if 0 <= event.x <= 30:
            if 0 <= event.y <= 30:
                init(data)
    else:
        if data.x1-data.r <= event.x <= data.x1+data.r:
            if data.y1-data.r <= event.y <= data.y1+data.r:
                data.mode = "tutorial"
        if data.x2-data.r <= event.x <= data.x2+data.r:
            if data.y2-data.r <= event.y <= data.y2+data.r:
                data.mode = "training"
        if data.x3-data.r <= event.x <= data.x3+data.r:
            if data.y3-data.r <= event.y <= data.y3+data.r:
                data.mode = "competitive"
        if data.x4-data.r <= event.x <= data.x4+data.r:
            if data.y4-data.r <= event.y <= data.y4+data.r:
                data.mode = "multiplayer"

def moveWithMouse(event, data):
    if data.mainBoard.clicked:
        data.mainBoard.moveClick(event.x, event.y, data.player)
    else:
        data.mainBoard.mouseClick(event.x, event.y, data.player)
        data.player = data.mainBoard.turn


####################################
# customize these functions
####################################

def init(data):
    data.mode = "beginning"
    data.x1 = data.width/19*2
    data.y1 = data.height/4*3
    data.x2 = data.width/20*7
    data.y2 = data.height/4*3
    data.x3 = data.width/20*12
    data.y3 = data.height/4*3
    data.x4 = data.width/19*16
    data.y4 = data.height/4*3
    data.r = 50
    data.mainBoard = CB.Board(data.width, data.height)
    data.mainBoard.makeBoard()
    data.player = "White"

def initialize(canvas, data):
    canvas.shapes = data.mainBoard.drawings

def drawImages(canvas, data):
    for key in canvas.shapes:
        im = Image.open(canvas.shapes[key])
        im = im.resize((data.width//5-2*data.mainBoard.margin, data.height//5-2*data.mainBoard.margin), 
                        Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(im)
        label = Label(canvas, image=ph)
        label.image=ph  #need to keep the reference of your image to avoid garbage collection
        canvas.create_image(int(key[1]*data.mainBoard.cellWidth+data.mainBoard.cellWidth*(19/20)), 
                            int(key[0]*data.mainBoard.cellHeight+data.mainBoard.cellHeight*(19/20)),
                            image=ph)

def mousePressed(event, data):
    if data.mode != "beginning":
        moveWithMouse(event, data)
    gameMode(event, data)


def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    if data.mode == "beginning":
        startScreen(canvas, data)

    if data.mode == "tutorial":
        tutorialScreen(canvas, data)

    if data.mode == "training":
        trainingScreen(canvas, data)

    if data.mode == "competitive":
        competitiveScreen(canvas, data)

    if data.mode == "multiplayer":
        multiplayerScreen(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10000 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    initialize(canvas, data)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 400)