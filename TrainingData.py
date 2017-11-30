# Make a neural network to determine the evaluation function of the game instead of hard coding this information.
# Attempt genetic algorithm, simulated annealing, and minimax move searching.

# https://arxiv.org/pdf/1509.01549.pdf
# Train neural network to match an evaluation function's assesment of a board position. Multiply output by 30,000 or something to match stockfish's evaluation score.
# The first looks at the global state of the game, such as the number and type of pieces on each side, which side is to move, castling rights and so on. 
# The second looks at piece-centric features such as the location of each piece on each side
# the final aspect is to map the squares that each piece attacks and defends.

# Database for chess training data
# http://ficsgames.org/download.html
# 
# For each number, first move is top player, second move is bottom player.
# If it is a pawn move, there is no P in front. For every other one
# x denotes piece taking another one.
# O-O means castling. O-O-O means a the longer castle
# kNight	N
# Bishop	B
# Rook	R
# Queen	Q
# King	K

# ftp://ftp.cs.kent.ac.uk/pub/djb/pgn-extract/help.html 

# https://chess.stackexchange.com/questions/18182/stockfish-evaluation-of-a-position-from-pgn
# This explains exactly how to get evaluation values for the given board.


import chess
import chess.uci
import chess.pgn
import sys
import string
import NeuralNet
from substituteNet import *

#network = NeuralNet.Net([42, 42, 32, 16, 1])

# I get my chess data from http://chessproblem.my-free-games.com/chess/games/Download-PGN.php

#arguments = sys.argv
#print(arguments)
#pgnfilename = str(arguments[1])

'''infile = open("/Users/michaelkronovet/Desktop/adams_kasparov_2005.pgn")
lines = infile.readlines()
for line in lines:
    count = line.count(". ")
    for i in range(count):
        line.replace(". ", ".")
print(infile)'''


#Read pgn file:
topology = [64, 44, 18, 1]
#topology = [64, 58, 1]
evalNet = NeuralNet.Net(topology)
#network = Network()
#inputNodes = [InputNode(i) for i in range(3)]
#hiddenNodes = [Node() for i in range(3)]
#outputNode = Node()

# weights are all randomized
#for inputNode in inputNodes:
#    for node in hiddenNodes:
#        Edge(inputNode, node)

#for node in hiddenNodes:
#    Edge(node, outputNode)

#network.outputNode = outputNode
#network.inputNodes.extend(inputNodes)


with open("/Users/michaelkronovet/Desktop/15-112/AdamsOK.pgn") as f:
    count = 0 
    for i in range(2):
        game = chess.pgn.read_game(f)
        while not game.is_end():
            count+= 1
            if count == 20:
                break
            node = game.variations[0]
            board = game.board()
            game = node
#        game = chess.pgn.read_game(f)
#        game = game.end()
#        board = game.board()
# board.piece_map() makes dictionary of piece positions based on square number.
# Bottom left corner is square 1, top right is square 64.
# Goes from left to right and then after each row is done it moves up a column.
            piecePos = board.piece_map()
#            print(piecePos)
            inputsL = []
            for i in range(64):
                if i in piecePos:
                    if piecePos[i].color == False:
                        inputsL.append(-1*piecePos[i].piece_type)
                    else:
                        inputsL.append(piecePos[i].piece_type)
                else:
                    inputsL.append(0)
#            print("Inputs: ", inputsL)
            
            evalNet.feedForward(inputsL)
            resultVals = evalNet.getResults()
            print("Outputs: ", resultVals)
            
# Pawn=1,Knight=2,Bishop=3,Rook=4,Queen=5,King=6
            handler = chess.uci.InfoHandler()
            engine = chess.uci.popen_engine('/Users/michaelkronovet/Desktop/15-112/stockfish-8-mac/Mac/stockfish-8-64') #give correct address of your engine here
            engine.info_handlers.append(handler)

            #give your position to the engine:
            engine.position(board)
            #Set your evaluation time, in ms:
            evaltime = 1000 #so 5 seconds
            evaluation = engine.go(movetime=evaltime)
#            print(board)
            if handler.info["score"][1] == None:
                continue
            evaluated = handler.info["score"][1].cp
            
#            print('evaluation value: ', handler.info["score"][1].cp/100.0)
# makes this 
            if board.turn == True:
                evaluated *= -1
#            L = [inputsL, evaluated/1000]
            print("TARGET", evaluated)
            evalNet.backProp([evaluated/1000])

#            network.train(L, maxIterations=1)
#            print("target value: ", evaluated/3000)
#            print(evalNet.layers[-1][0].getOutputVal())
    #        print('best move: ', board.san(evaluation[0]))

            # Do this for if a move has no value or something. Maybe this error won't come up when checking moves.
            # This value is relative to who is making the move. negative means current player is losing pos means current player is winning.
#            print("Average error: ", evalNet.getRecentAverageError())

'''firstWeights = []
secondWeights = []
#thirdWeights = []

for layer in range(len(topology)-1):
    for neuron in range(len(evalNet.layers[layer])):
        if layer == 1:
            firstWeights.append(evalNet.layers[layer][neuron].outputWeights)
        elif layer == 2:
            secondWeights.append(evalNet.layers[layer][neuron].outputWeights)
#        elif layer == 3:
#            thirdWeights.append(evalNet.layers[layer][neuron].outputWeights)

open("/Users/michaelkronovet/Desktop/15-112/FinalProject/TrainedWeightsText.txt", "w").close()
file = open("/Users/michaelkronovet/Desktop/15-112/FinalProject/TrainedWeightsText.txt", "w")
file.write(str(firstWeights))
file.write(str(secondWeights))
file.write(str(thirdWeights))




    first_game = chess.pgn.read_game(f)
#   print(first_game)
    second_game = chess.pgn.read_game(f)
#   print("THISIISISISISI",second_game)

#Go to the end of the game and create a chess.Board() from it:
first_game = first_game.end()
board = first_game.board()

#So if you want, here's also your PGN to FEN conversion:
#print('FEN of the last position of the game: ', board.fen())

#or if you want to loop over all game nodes:
#while not game.is_end():
#    node = game.variations[0]
#    board = game.board() #print the board if you want, to make sure
#    game = node
    #Now we have our board ready, load your engine:
handler = chess.uci.InfoHandler()
engine = chess.uci.popen_engine('/Users/michaelkronovet/Desktop/15-112/stockfish-8-mac/Mac/stockfish-8-64') #give correct address of your engine here
engine.info_handlers.append(handler)

#give your position to the engine:
engine.position(board)

#Set your evaluation time, in ms:
evaltime = 1000 #so 5 seconds
evaluation = engine.go(movetime=evaltime)

#print best move, evaluation and mainline:
print('best move: ', board.san(evaluation[0]))
print('evaluation value: ', handler.info["score"][1].cp/100.0)
print('Corresponding line: ', board.variation_san(handler.info["pv"][1]))




second_game = second_game.end()
board = second_game.board()

#So if you want, here's also your PGN to FEN conversion:
print('FEN of the last position of the game: ', board.fen())

#or if you want to loop over all game nodes:
while not second_game.is_end():
    node = second_game.variations[0]
    board = second_game.board() #print the board if you want, to make sure
    game = node
    #Now we have our board ready, load your engine:
    handler = chess.uci.InfoHandler()
    engine = chess.uci.popen_engine('/Users/michaelkronovet/Desktop/15-112/stockfish-8-mac/Mac/stockfish-8-64') #give correct address of your engine here
    engine.info_handlers.append(handler)

    #give your position to the engine:
    engine.position(board)

    #Set your evaluation time, in ms:
    evaltime = 1000 #so 5 seconds
    evaluation = engine.go(movetime=evaltime)

    #print best move, evaluation and mainline:
    print('best move: ', board.san(evaluation[0]))
    print('evaluation value: ', handler.info["score"][1].cp/100.0)
    print('Corresponding line: ', board.variation_san(handler.info["pv"][1]))'''