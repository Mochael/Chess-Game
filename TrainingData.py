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
# Came up with idea by reading about Giraffe chess engine.

# ftp://ftp.cs.kent.ac.uk/pub/djb/pgn-extract/help.html 

# https://chess.stackexchange.com/questions/18182/stockfish-evaluation-of-a-position-from-pgn
# This explains exactly how to get evaluation values for the given board.

# https://www.pgnmentor.com/files.html

import chess
import chess.uci
import chess.pgn
import sys
import string
import NeuralNet


topology = [64, 44, 18, 1]
evalNet = NeuralNet.Net(topology)


with open("/Users/michaelkronovet/Desktop/15-112/Alburt.pgn") as f:
    count  = 0
    for n in range(775):
        game = chess.pgn.read_game(f)
        count += 1
        if count == 2:
            break
        while not game.is_end():
            try:
                node = game.variations[0]
                board = game.board()
                game = node
                piecePos = board.piece_map()
                inputsL = []
                for i in range(64):
                    if i in piecePos:
                        if piecePos[i].color == False:
                            inputsL.append(-1*piecePos[i].piece_type)
                        else:
                            inputsL.append(piecePos[i].piece_type)
                    else:
                        inputsL.append(0)
                evalNet.feedForward(inputsL)
                resultVals = evalNet.getResults()
                handler = chess.uci.InfoHandler()
                engine = chess.uci.popen_engine('/Users/michaelkronovet/Desktop/15-112/stockfish-8-mac/Mac/stockfish-8-64') #give correct address of your engine here
                engine.info_handlers.append(handler)
                engine.position(board)
                evaltime = 1000
                evaluation = engine.go(movetime=evaltime)
                evaluated = handler.info["score"][1].cp
                if evaluated == None:
                    continue
                if board.turn == True:
                    evaluated *= -1
                print("OUTPUT", resultVals)

                print("TARGET", evaluated/700)
                evalNet.backProp(evaluated/700)
                
#                print("TARGET", evaluated/1000)
#                evalNet.backProp(evaluated/1000)
            except:
                continue


#            network.train(L, maxIterations=1)
#            print("target value: ", evaluated/3000)
#            print(evalNet.layers[-1][0].getOutputVal())
    #        print('best move: ', board.san(evaluation[0]))

            # Do this for if a move has no value or something. Maybe this error won't come up when checking moves.
            # This value is relative to who is making the move. negative means current player is losing pos means current player is winning.
#            print("Average error: ", evalNet.getRecentAverageError())

firstWeights = []
secondWeights = []
thirdWeights = []

for layer in range(len(topology)-1):
    for neuron in range(len(evalNet.layers[layer])):
        if layer == 1:
            firstWeights.append(evalNet.layers[layer][neuron].outputWeights)
        elif layer == 2:
            secondWeights.append(evalNet.layers[layer][neuron].outputWeights)
        elif layer == 3:
            thirdWeights.append(evalNet.layers[layer][neuron].outputWeights)

open("/Users/michaelkronovet/Desktop/15-112/FinalProject/TrainedWeightsText.txt", "w").close()
file = open("/Users/michaelkronovet/Desktop/15-112/FinalProject/TrainedWeightsText.txt", "w")
file.write(str(firstWeights))
file.write(str(secondWeights))
file.write(str(thirdWeights))