from PIL import Image, ImageTk

#photo = ImageTk.PhotoImage(Image.open("someFile.jpg"))

# If the player's move puts them in check, then the move is undone.
def isCheck(board):


class Pawn(object):
    def __init__(self, color, posRow, posCol):
        self.color = color
        self.posRow = posRow
        self.posCol = posCol
        self.image = ( xc, yc, r, "blue")
        self.moves = []
        self.takeMoves = []

    def getMoves(self, board):
        # Black pieces start at the top of the board.
        if self.color == "Black":
            if self.posRow == 6:
                self.moves == [[self.posRow,self.posRow+1],[self.posRow,self.posRow+2]]
            elif self.posRow != len(board)-1:
                self.moves = [[self.posRow,self.posRow+1]]
        # White pieces start at the bottom of the board.
        else:
            if self.posRow == 1:
                self.moves == [[self.posRow,self.posRow-1],[self.posRow,self.posRow-2]]
            elif self.posRow != 0:
                self.moves = [[self.posRow,self.posRow-1]]
        # Gets rid of moves where other pieces are blocking pawn.
        for move in self.moves:
            if board[move[0]][move[1]] != None:
                self.moves.remove(move)
    
    # Finds possible diagonal moves for taking pieces with a pawn.
    def findTakeMoves(self, board):
        if self.color == "Black":
            self.takeMoves.append(board[self.posRow+1][self.posCol-1])
            self.takeMoves.append(board[self.posRow+1][self.posCol+1])
            if self.posCol == 0:
                self.takeMoves.remove(board[self.posRow+1][self.posCol-1])
            if self.posCol == len(board)-1:
                self.takeMoves.remove(board[self.posRow+1][self.posCol+1])
        else:
            self.takeMoves.append(board[self.posRow-1][self.posCol-1])
            self.takeMoves.append(board[self.posRow-1][self.posCol+1])
            if self.posCol == 0:
                self.takeMoves.remove(board[self.posRow-1][self.posCol-1])
            if self.posCol == len(board)-1:
                self.takeMoves.remove(board[self.posRow-1][self.posCol+1])
        for i in range(len(self.takeMoves)):
            confirmTakeMoves([self.takeMoves[i],self.takeMoves[i][1]], board)

    # Only adds to takeMoves list of diagonal moves if the piece is the opposite color.
    def confirmTakeMoves(self, otherPos, board):
        if self.color != board[otherPos[0]][otherPos[1]].color:
            self.moves.append([otherPos[0],otherPos[1]])

class Rook(object):
    def __init__(self, color, posRow, posCol):
        self.color = color
        self.posRow = posRow
        self.posCol = posCol
        self.image = ( xc, yc, r, "red")
        self.moves = []

    # Finds all legal moves.
    def getMoves(self, board):
        for i in range(self.posRow-1, -1):
            if board[i][self.posCol] != None:
                if board[i][self.posCol].color != self.color:
                    self.moves.append([i, self.posCol])
                break
            self.moves.append([i,self.posCol])
        for j in range(self.posCol-1, -1):
            if board[self.posRow][j] != None:
                if board[self.posRow][j].color != self.color:
                    self.moves.append([self.posCol, j])
                break
            self.moves.append([self.posRow,j])
        for k in range(self.posRow, len(board)):
            if board[k][self.posCol] != None:
                if board[k][self.posCol] != self.color:
                    self.moves.append([k, self.posCol])
                break
            self.moves.append([k,self.posCol])
        for m in range(self.posCol, len(board[0])):
            if board[self.posRow][m] != None:
                if board[self.posRow][m] != self.color:
                    self.moves.append([self.posRow, m])
                break
            self.moves.append([self.posRow,m])
        

class Knight(object):
    def __init__(self, color, posRow, posCol):
        self.color = color
        self.posRow = posRow
        self.posCol = posCol
        self.image = ( xc, yc, r, "red")
        self.moves = []

    # Finds all moves.
    def getMoves(self, board, counter = 0):
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
        self.image = ( xc, yc, r, "red")
        self.moves = []
    
    def getMoves(self, board):
        adder = 0
        # Going diagonally down and to the right.
        while(self.posRow+adder <= 7 and self.posCol+adder <= 7):
            adder += 1
            if board[self.posRow+adder][self.posCol+adder] != None:
                if board[self.posRow+adder][self.posCol+adder].color != self.color:
                    self.moves.append([self.posRow+adder, self.posCol+adder])
                    break
            self.moves.append([self.posRow+adder, self.posCol+adder])
        adder = 0
        # Up and to the left.
        while(self.posRow+adder >= 0 and self.posCol+adder >= 0):
            adder -= 1
            if board[self.posRow+adder][self.posCol+adder] != None:
                if board[self.posRow+adder][self.posCol+adder].color != self.color:
                    self.moves.append([self.posRow+adder, self.posCol+adder])
                    break
            self.moves.append([self.posRow+adder, self.posCol+adder])
        adder = 0
        # Up and to the right.
        while(self.posRow-adder >= 0 and self.posCol+adder <= 7):
            adder += 1
            if board[self.posRow-adder][self.posCol+adder] != None:
                if board[self.posRow-adder][self.posCol+adder].color != self.color:
                    self.moves.append([self.posRow-adder, self.posCol+adder])
                    break
            self.moves.append([self.posRow-adder, self.posCol+adder])
        adder = 0
        # Down and to the left.
        while(self.posRow+adder <= 7 and self.posCol+adder >= 0):
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
        self.image = ( xc, yc, r, "red")
        self.moves = []

    def getStraightMoves(self, board):
        for i in range(self.posRow-1, -1):
            if board[i][self.posCol] != None:
                if board[i][self.posCol].color != self.color:
                    self.moves.append([i, self.posCol])
                break
            self.moves.append([i,self.posCol])
        for j in range(self.posCol-1, -1):
            if board[self.posRow][j] != None:
                if board[self.posRow][j].color != self.color:
                    self.moves.append([self.posCol, j])
                break
            self.moves.append([self.posRow,j])
        for k in range(self.posRow, len(board)):
            if board[k][self.posCol] != None:
                if board[k][self.posCol] != self.color:
                    self.moves.append([k, self.posCol])
                break
            self.moves.append([k,self.posCol])
        for m in range(self.posCol, len(board[0])):
            if board[self.posRow][m] != None:
                if board[self.posRow][m] != self.color:
                    self.moves.append([self.posRow, m])
                break
            self.moves.append([self.posRow,m])

    def getDiagonalMoves(self, board):
        adder = 0
        # Going diagonally down and to the right.
        while(self.posRow+adder <= 7 and self.posCol+adder <= 7):
            adder += 1
            if board[self.posRow+adder][self.posCol+adder] != None:
                if board[self.posRow+adder][self.posCol+adder].color != self.color:
                    self.moves.append([self.posRow+adder, self.posCol+adder])
                    break
            self.moves.append([self.posRow+adder, self.posCol+adder])
        adder = 0
        # Up and to the left.
        while(self.posRow+adder >= 0 and self.posCol+adder >= 0):
            adder -= 1
            if board[self.posRow+adder][self.posCol+adder] != None:
                if board[self.posRow+adder][self.posCol+adder].color != self.color:
                    self.moves.append([self.posRow+adder, self.posCol+adder])
                    break
            self.moves.append([self.posRow+adder, self.posCol+adder])
        adder = 0
        # Up and to the right.
        while(self.posRow-adder >= 0 and self.posCol+adder <= 7):
            adder += 1
            if board[self.posRow-adder][self.posCol+adder] != None:
                if board[self.posRow-adder][self.posCol+adder].color != self.color:
                    self.moves.append([self.posRow-adder, self.posCol+adder])
                    break
            self.moves.append([self.posRow-adder, self.posCol+adder])
        adder = 0
        # Down and to the left.
        while(self.posRow+adder <= 7 and self.posCol+adder >= 0):
            adder += 1
            if board[self.posRow+adder][self.posCol-adder] != None:
                if board[self.posRow+adder][self.posCol-adder].color != self.color:
                    self.moves.append([self.posRow+adder, self.posCol-adder])
                    break
            self.moves.append([self.posRow+adder, self.posCol-adder])

class King(object):
    def __init__(self, color, posRow, posCol):
        self.color = color
        self.posRow = posRow
        self.posCol = posCol
        self.image = ( xc, yc, r, "red")
        self.moves = []

    def getMoves(self, board):
        for i in range(-1, 2):
            self.moves.append([self.posRow-1, self.posCol+i])
            if board[self.posRow-1][self.posCol+i] != None:
                if board[self.posRow-1][self.posCol+i].color == self.color:
                    self.moves.remove([self.posRow-1, self.posCol+i])
        for j in range(-1, 2):
            self.moves.append([self.posRow+1, self.posCol+j])
            if board[self.posRow+1][self.posCol+j] != None:
                if board[self.posRow+1][self.posCol+j].color == self.color:
                    self.moves.remove([self.posRow+1, self.posCol+j])
        if (board[self.posRow][self.posCol-1] == None or 
        board[self.posRow][self.posCol-1].color == self.color):
                self.moves.append([self.posRow][self.posCol-1])
        if (board[self.posRow][self.posCol+1] == None or 
        board[self.posRow][self.posCol+1].color == self.color):
                self.moves.append([self.posRow][self.posCol+1])