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
#import NeuralNet

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
with open("/Users/michaelkronovet/Desktop/15-112/AdamsOK.pgn") as f:
    count = 0
    for i in range(1):
        game = chess.pgn.read_game(f)
        while not game.is_end():
            count+= 1
            if count == 19:
                break
            node = game.variations[0]
            board = game.board() #print the board if you want, to make sure
            game = node
#        game = chess.pgn.read_game(f)
#        game = game.end()
#        board = game.board()
# board.piece_map() makes dictionary of piece positions based on square number.
# Bottom left corner is square 1, top right is square 64.
# Goes from left to right and then after each row is done it moves up a column.
#        print(board.piece_map())
            handler = chess.uci.InfoHandler()
            engine = chess.uci.popen_engine('/Users/michaelkronovet/Desktop/15-112/stockfish-8-mac/Mac/stockfish-8-64') #give correct address of your engine here
            engine.info_handlers.append(handler)

            #give your position to the engine:
            engine.position(board)

            #Set your evaluation time, in ms:
            evaltime = 1000 #so 5 seconds
            evaluation = engine.go(movetime=evaltime)
            print(board)
            if handler.info["score"][1] == None:
                continue
            evaluated = handler.info["score"][1].cp
#            print('evaluation value: ', handler.info["score"][1].cp/100.0)
            if board.turn == False:
                evaluated *= -1
            print("NEWEVALUATEDVALUE", evaluated)
    #        print('best move: ', board.san(evaluation[0]))
            print("LE SCORO", handler.info["score"])
            # Do this for if a move has no value or something. Maybe this error won't come up when checking moves.
            # This value is relative to who is making the move. negative means current player is losing pos means current player is winning.
            if handler.info["score"][1] == None:
                continue

'''
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