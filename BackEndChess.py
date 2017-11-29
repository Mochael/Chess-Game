from PIL import Image, ImageTk
import copy
# photo = ImageTk.PhotoImage(Image.open("someFile.jpg"))
# Do canvas.create_image(xcenter, ycenter, image = photo)

# Identifies if a player is in check.
def isCheck(board, turn):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if isinstance(board[row][col], King) and board[row][col].color == turn:
                kingRow = row
                kingCol = col
                print("KINGROW", kingRow, "KINGCOL", kingCol)
                break
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != None and board[row][col].color != turn:
                    board[row][col].getMoves(board)
                    if [kingRow, kingCol] in board[row][col].moves:
                        print("NONONONONONO")
                        print(row,col)
                        print(board[row][col].moves)
                        print("CHECKED")
                        return True
    return False

# Run this function for both stalemate and checkmate. However, only run for checkmate if player is first in check.
def isCheckMate(board, turn):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != None and board[row][col].color == turn:
                board[row][col].getMoves(board)
                for move in board[row][col].moves:
                    tempB = copy.deepcopy(board)
                    tempB[move[0]][move[1]] = board[row][col]
                    tempB[move[0]][move[1]].posRow = move[0]
                    tempB[move[0]][move[1]].posCol = move[1]
                    tempB[row][col] = None
                    if not isCheck(tempB, turn):
                        return False
    return True
   
class Pawn(object):
    def __init__(self, color, posRow, posCol):
        self.color = color
        self.posRow = posRow
        self.posCol = posCol
        if self.color == "Black":
            self.image = "/Users/michaelkronovet/Desktop/15-112/FinalProject/PieceImages/BlackPawn.png"
        else:
            self.image = "/Users/michaelkronovet/Desktop/15-112/FinalProject/PieceImages/WhitePawn.png"
        self.moves = []
        self.takeMoves = []
    
    def __repr__(self):
        return self.color+" Pawn"

    def getMoves(self, board):
        self.moves = []
        # Black pieces start at the top of the board.
        if self.color == "Black":
            if self.posRow == 1:
                self.moves = [[self.posRow+1,self.posCol],[self.posRow+2,self.posCol]]
            else:
                self.moves = [[self.posRow+1,self.posCol]]
        # White pieces start at the bottom of the board.
        else:
            if self.posRow == 6:
                self.moves = [[self.posRow-1,self.posCol],[self.posRow-2,self.posCol]]
            else:
                self.moves = [[self.posRow-1,self.posCol]]
        # Gets rid of moves where other pieces are blocking pawn.
        for move in self.moves:
            if board[move[0]][move[1]] != None:
                self.moves.remove(move)
        self.findTakeMoves(board)
    
    # Finds possible diagonal moves for taking pieces with a pawn.
    def findTakeMoves(self, board):
        self.takeMoves = []
        if self.color == "Black":
            self.takeMoves.append([self.posRow+1, self.posCol-1])
            self.takeMoves.append([self.posRow+1, self.posCol+1])
            if self.posCol == 0:
                self.takeMoves.remove([self.posRow+1, self.posCol-1])
            if self.posCol == len(board)-1:
                self.takeMoves.remove([self.posRow+1, self.posCol+1])
        else:
            self.takeMoves.append([self.posRow-1, self.posCol-1])
            self.takeMoves.append([self.posRow-1, self.posCol+1])
            if self.posCol == 0:
                self.takeMoves.remove([self.posRow-1, self.posCol-1])
            if self.posCol == len(board)-1:
                self.takeMoves.remove([self.posRow-1, self.posCol+1])
        for i in range(len(self.takeMoves)):
            if (board[self.takeMoves[i][0]][self.takeMoves[i][1]] != None 
            and self.color != board[self.takeMoves[i][0]][self.takeMoves[i][1]].color):
                self.moves.append(self.takeMoves[i])


class Rook(object):
    def __init__(self, color, posRow, posCol):
        self.color = color
        self.posRow = posRow
        self.posCol = posCol
        if self.color == "Black":
            self.image = "/Users/michaelkronovet/Desktop/15-112/FinalProject/PieceImages/BlackRook.png"
        else:
            self.image = "/Users/michaelkronovet/Desktop/15-112/FinalProject/PieceImages/WhiteRook.png"
        self.moves = []
    
    def __repr__(self):
        return self.color+" Rook"

    # Finds all legal moves.
    def getMoves(self, board):
        self.moves = []
        for i in range(self.posRow-1, -1, -1):
            if board[i][self.posCol] != None:
                if board[i][self.posCol].color != self.color:
                    self.moves.append([i, self.posCol])
                break
            self.moves.append([i, self.posCol])
        for j in range(self.posCol-1, -1, -1):
            if board[self.posRow][j] != None:
                if board[self.posRow][j].color != self.color:
                    self.moves.append([self.posRow, j])
                break
            self.moves.append([self.posRow,j])
        for k in range(self.posRow+1, 8, 1):
            if board[k][self.posCol] != None:
                if board[k][self.posCol].color != self.color:
                    self.moves.append([k, self.posCol])
                break
            self.moves.append([k,self.posCol])
        for m in range(self.posCol+1, 8, 1):
            if board[self.posRow][m] != None:
                if board[self.posRow][m].color != self.color:
                    self.moves.append([self.posRow, m])
                break
            self.moves.append([self.posRow,m])
        

class Knight(object):
    def __init__(self, color, posRow, posCol):
        self.color = color
        self.posRow = posRow
        self.posCol = posCol
        if self.color == "Black":
            self.image = "/Users/michaelkronovet/Desktop/15-112/FinalProject/PieceImages/BlackKnight.png"
        else:
            self.image = "/Users/michaelkronovet/Desktop/15-112/FinalProject/PieceImages/WhiteKnight.png"
        self.moves = []

    def __repr__(self):
        return self.color+" Knight"

    # Finds all moves.
    def getMoves(self, board, counter = 0):
        self.moves = []
        for move in [[-1,-2],[-1,2],[-2,-1],[-2,1],[1,-2],[1,2],[2,-1],[2,1]]:
            if 0 <= self.posRow+move[0] <= 7 and 0 <= self.posCol+move[1] <= 7:
                if board[self.posRow+move[0]][self.posCol+move[1]] == None:
                    self.moves.append([self.posRow+move[0],self.posCol+move[1]])
                else:
                    if board[self.posRow+move[0]][self.posCol+move[1]].color != self.color:
                        self.moves.append([self.posRow+move[0],self.posCol+move[1]])


class Bishop(object):
    def __init__(self, color, posRow, posCol):
        self.color = color
        self.posRow = posRow
        self.posCol = posCol
        if self.color == "Black":
            self.image = "/Users/michaelkronovet/Desktop/15-112/FinalProject/PieceImages/BlackBishop.png"
        else:
            self.image = "/Users/michaelkronovet/Desktop/15-112/FinalProject/PieceImages/WhiteBishop.png"
        self.moves = []
    
    def __repr__(self):
        return self.color+" Bishop"
    
    def getMoves(self, board):
        self.moves = []
        adder = 0
        # Going diagonally down and to the right.
        while(self.posRow+adder <= 6 and self.posCol+adder <= 6):
            adder += 1
            if board[self.posRow+adder][self.posCol+adder] != None:
                if board[self.posRow+adder][self.posCol+adder].color != self.color:
                    self.moves.append([self.posRow+adder, self.posCol+adder])
                break
            self.moves.append([self.posRow+adder, self.posCol+adder])
        adder = 0
        # Up and to the left.
        while(self.posRow+adder >= 1 and self.posCol+adder >= 1):
            adder -= 1
            if board[self.posRow+adder][self.posCol+adder] != None:
                if board[self.posRow+adder][self.posCol+adder].color != self.color:
                    self.moves.append([self.posRow+adder, self.posCol+adder])
                break
            self.moves.append([self.posRow+adder, self.posCol+adder])
        adder = 0
        # Up and to the right.
        while(self.posRow-adder >= 1 and self.posCol+adder <= 6):
            adder += 1
            if board[self.posRow-adder][self.posCol+adder] != None:
                if board[self.posRow-adder][self.posCol+adder].color != self.color:
                    self.moves.append([self.posRow-adder, self.posCol+adder])
                break
            self.moves.append([self.posRow-adder, self.posCol+adder])
        adder = 0
        # Down and to the left.
        while(self.posRow+adder <= 6 and self.posCol-adder >= 1):
            adder += 1
            if board[self.posRow+adder][self.posCol-adder] != None:
                if board[self.posRow+adder][self.posCol-adder].color != self.color:
                    self.moves.append([self.posRow+adder, self.posCol-adder])
                break
            self.moves.append([self.posRow+adder, self.posCol-adder])


class Queen(object):
    def __init__(self, color, posRow, posCol):
        self.color = color
        self.posRow = posRow
        self.posCol = posCol
        if self.color == "Black":
            self.image = "/Users/michaelkronovet/Desktop/15-112/FinalProject/PieceImages/BlackQueen.png"
        else:
            self.image = "/Users/michaelkronovet/Desktop/15-112/FinalProject/PieceImages/WhiteQueen.png"
        self.moves = []
    
    def __repr__(self):
        return self.color+" Queen"

    def getStraightMoves(self, board):
        for i in range(self.posRow-1, -1, -1):
            if board[i][self.posCol] != None:
                if board[i][self.posCol].color != self.color:
                    self.moves.append([i, self.posCol])
                break
            self.moves.append([i,self.posCol])
        for j in range(self.posCol-1, -1, -1):
            if board[self.posRow][j] != None:
                if board[self.posRow][j].color != self.color:
                    self.moves.append([self.posRow, j])
                break
            self.moves.append([self.posRow,j])
        for k in range(self.posRow+1, 8):
            if board[k][self.posCol] != None:
                if board[k][self.posCol].color != self.color:
                    self.moves.append([k, self.posCol])
                break
            self.moves.append([k,self.posCol])
        for m in range(self.posCol+1, 8):
            if board[self.posRow][m] != None:
                if board[self.posRow][m].color != self.color:
                    self.moves.append([self.posRow, m])
                break
            self.moves.append([self.posRow,m])

    def getDiagonalMoves(self, board):
        adder = 0
        # Going diagonally down and to the right.
        while(self.posRow+adder <= 6 and self.posCol+adder <= 6):
            adder += 1
            if board[self.posRow+adder][self.posCol+adder] != None:
                if board[self.posRow+adder][self.posCol+adder].color != self.color:
                    self.moves.append([self.posRow+adder, self.posCol+adder])
                break
            self.moves.append([self.posRow+adder, self.posCol+adder])
        adder = 0
        # Up and to the left.
        while(self.posRow+adder >= 1 and self.posCol+adder >= 1):
            adder -= 1
            if board[self.posRow+adder][self.posCol+adder] != None:
                if board[self.posRow+adder][self.posCol+adder].color != self.color:
                    self.moves.append([self.posRow+adder, self.posCol+adder])
                break
            self.moves.append([self.posRow+adder, self.posCol+adder])
        adder = 0
        # Up and to the right.
        while(self.posRow-adder >= 1 and self.posCol+adder <= 6):
            adder += 1
            if board[self.posRow-adder][self.posCol+adder] != None:
                if board[self.posRow-adder][self.posCol+adder].color != self.color:
                    self.moves.append([self.posRow-adder, self.posCol+adder])
                break
            self.moves.append([self.posRow-adder, self.posCol+adder])
        adder = 0
        # Down and to the left.
        while(self.posRow+adder <= 6 and self.posCol-adder >= 1):
            adder += 1
            if board[self.posRow+adder][self.posCol-adder] != None:
                if board[self.posRow+adder][self.posCol-adder].color != self.color:
                    self.moves.append([self.posRow+adder, self.posCol-adder])
                break
            self.moves.append([self.posRow+adder, self.posCol-adder])

    def getMoves(self, board):
        self.moves = []
        self.getDiagonalMoves(board)
        self.getStraightMoves(board)

class King(object):
    def __init__(self, color, posRow, posCol):
        self.color = color
        self.posRow = posRow
        self.posCol = posCol
        if self.color == "Black":
            self.image = "/Users/michaelkronovet/Desktop/15-112/FinalProject/PieceImages/BlackKing.png"
        else:
            self.image = "/Users/michaelkronovet/Desktop/15-112/FinalProject/PieceImages/WhiteKing.png"
        self.moves = []

    def __repr__(self):
        return self.color+" King"

    def getMoves(self, board):
        self.moves = []
        for i in range(-1, 2):
            if 0 <= self.posRow-1 <= 7 and 0 <= self.posCol+i <= 7:
                self.moves.append([self.posRow-1, self.posCol+i])
                if board[self.posRow-1][self.posCol+i] != None:
                    if board[self.posRow-1][self.posCol+i].color == self.color:
                        self.moves.remove([self.posRow-1, self.posCol+i])
                        
        for j in range(-1, 2):
            if 0 <= self.posRow+1 <= 7 and 0 <= self.posCol+j <= 7:
                self.moves.append([self.posRow+1, self.posCol+j])
                if board[self.posRow+1][self.posCol+j] != None:
                    if board[self.posRow+1][self.posCol+j].color == self.color:
                        self.moves.remove([self.posRow+1, self.posCol+j])

        if 0 <= self.posRow <= 7 and 0 <= self.posCol-1 <= 7:
            if (board[self.posRow][self.posCol-1] == None or 
            board[self.posRow][self.posCol-1].color != self.color):
                self.moves.append([self.posRow, self.posCol-1])

        if 0 <= self.posRow <= 7 and 0 <= self.posCol+1 <= 7:
            if (board[self.posRow][self.posCol+1] == None or 
            board[self.posRow][self.posCol+1].color != self.color):
                self.moves.append([self.posRow, self.posCol+1])