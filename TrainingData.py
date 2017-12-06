# This file was used to train the neural network. I am parsing through the PGN file I
# input and evaluating the given board using my neural network and editing
# it based off of its deviation from the evaluation the stockfish engine gives it.
# It then puts the new trained weights from this training session into a text file
# for me to reference when loading the neural network for the AI.

# Citation: Database for chess training data
# https://www.pgnmentor.com/files.html

# Citation: Used Stockfish Engine to train my neural network.
# https://stockfishchess.org

import chess
import chess.uci
import chess.pgn
import sys
import string
import NeuralNet
import os
import ast


# Neural net topology
topology = [64, 44, 18, 1]

# Assigns the existing trained weights in the text file to the neural net.
with open("./TrainedWeightsText.txt", "r") as myfile:
    weightsF=myfile.read().replace('\n', '')
weightsL = ast.literal_eval(weightsF)
evalNet = NeuralNet.Net(topology)
for layer in range(len(evalNet.layers)-1):
    for neuron in range(len(evalNet.layers[layer])):
        evalNet.layers[layer][neuron].outputWeights = weightsL[layer][neuron]

path = "./PGNFiles/McDonnell.pgn"

# Trains neural network.
with open(path) as f:
    count = 0
    for n in range(100):
        try:
            print("GAMECOUNT", n)
            game = chess.pgn.read_game(f)
            while not game.is_end():
                node = game.variations[0]
                board = game.board()
                game = node
                piecePos = board.piece_map()
                inputsL = []
                for i in range(64):
                    if i in piecePos:
                        if piecePos[i].color == False:
                            inputsL.append(-1*piecePos[i].piece_type/100)
                        else:
                            inputsL.append(piecePos[i].piece_type/100)
                    else:
                        inputsL.append(0.0)
                evalNet.feedForward(inputsL)
                resultVals = evalNet.getResults()
                handler = chess.uci.InfoHandler()
                engine = chess.uci.popen_engine("./stockfish-8-mac/Mac/stockfish-8-64") #give correct address of your engine here
                engine.info_handlers.append(handler)
                engine.position(board)
                evaltime = 1000
                evaluation = engine.go(movetime=evaltime)
                evaluated = handler.info["score"][1].cp
                if evaluated == None:
                    continue
                evaluated /= 700
                if abs(evaluated) > 1:
                    if evaluated < 0:
                        evaluated = -1
                    else:
                        evaluated = 1
                if board.turn == True:
                    evaluated *= -1
                print("TARGET", evaluated)
                print("OUTPUTS", resultVals)
                evalNet.backProp(evaluated)
        except:
            continue

# Updates the weights in the text file to reflect this training session.
firstWeights = []
secondWeights = []
thirdWeights = []
for layer in range(len(topology)-1):
    for neuron in range(len(evalNet.layers[layer])):
        if layer == 0:
            firstWeights.append(evalNet.layers[layer][neuron].outputWeights)
        elif layer == 1:
            secondWeights.append(evalNet.layers[layer][neuron].outputWeights)
        elif layer == 2:
            thirdWeights.append(evalNet.layers[layer][neuron].outputWeights)
weightsList = []
weightsList.append(firstWeights)
weightsList.append(secondWeights)
weightsList.append(thirdWeights)
open("./TrainedWeightsText.txt", "w").close()
file = open("./TrainedWeightsText.txt", "w")
file.write(str(weightsList))