Brief Project Summary:
I made a chess game from scratch that has the rules of regular chess. It prevents players from making moves that put them in check and when there is a checkmate there is an endgame screen. The game has both AI and multiplayer.

The four game modes:

1. Tutorial Mode:
	- Players can click on each piece/move at the bottom and it will show 	  animation of how the piece moves after a few seconds
2. Training Mode:
	- A single player can play against themselves to practice making 	  certain moves. Regular chess rules apply.
3. Competitive Mode:
	- This is where the project gets juicy. In this mode players can play 	  against an AI. In order to teach through possible moves, the AI 	  uses the minimax algorithm to go through all possible moves and 	  then each of the human player’s moves that branch off after the 	  first node of moves. At each move if it identifies a move move for 	  itself where the opposing player can only make a really bad move, 	  then the AI automatically makes that move. Otherwise, the AI uses a 	  neural network I made (without any machine learning libraries) to 	  evaluate how good a certain move is when sifting through the 		  possible moves. The move that results in the worst possible moves 	  for the human player is chosen and the move is made.
4. Multiplayer Mode:
	- I used sockets to allow players to play each other from different 	  computers in this mode.

More Detail about AI:

Minimax- Minimax algorithm is when the AI first checks through its possible moves, then for each of those moves it sees how the human player will respond (my AI stops going through deeper move nodes at this point but minimax itself can hypothetically go through each possible succession of moves in the game but it just takes too much computing power). At this move stage, the minimax algorithm uses my neural network function in order to determine how good the board is for the moving player. The algorithm assumes that the human player will make the most optimal move in response, so it then sets the actual board score to this move. For each possible AI move, the true board score is given by the highest score the human player can score given the AI makes that move. Just to avoid the possibility of the neural network evaluating some awful move as good, if there is some move the AI can make (or not make) where they will lose much higher value pieces than the human player, they will not make (or make) that move.

Neural Net- My neural network is fully connected with 2 hidden layers of 44 neurons and 18 neurons, respectively. The neural network takes in 64 inputs, one for each space on the chess board with each input corresponding to a certain square on the board. If there is no piece on that square, the input neuron receives an input value of 0. Otherwise the inputs follow this scoring metric: Pawn: .01, Knight: .02, Bishop: .03, Rook: .04, Queen: .05, King: .06. If the piece is white, the input value for that space is the corresponding number. If the piece is black, the input is the corresponding number, but negative. To train the neural network I downloaded several PGN (Portable Game Notation) files (a unique file format to chess games which specifies the moves in the format 1. e4 e5 2. Nf3 Nc6) and iterated through hundreds of games by different players to evaluate each board after a new move was made. While evaluating the board position with my neural network, I simultaneously ran the chess board through the best chess engine in the world, Stockfish. I used supervised training for my neural network where I set the target evaluation for my neural network to be the evaluation stockfish gave the board. I then backpropagated through the neurons to update their weights to better fit Stockfish’s board evaluation.

Needed Libraries:
pygame- make sure you have pygame installed
python-chess- used to parse through training games and format with stockfish engine. To install run the following command in terminal/command prompt:
pip install python-chess[engine,gaviota]

How to Run:
1. Open up the terminal/command prompt and cd into the project folder.
2. Google your IP address and go into Server.py and Client.py and change the variable HOST to reflect your IP address (must update each time your IP address changes).
3. Run Server.py in terminal and then in another terminal window run Client.py
4. You should now be able to play the single player modes.
5. If you want to play multiplayer, you need to run Client.py in a different terminal window. 
6. If running on a different computer you need to download the source code and follow steps 1-2 as well as input the host server IP into your HOST variable in Client.py.
7. I recommend playing multiplayer on different computers since I chose to make it so users could not adjust the screen size.
