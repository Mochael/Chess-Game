# This file is the main file for the project which handles the majority of the front end UI as well as
# tells the game when to run all of the different functions that are spread out across the different
# project files.

# Citation: Chess piece images from https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent
# Citation: Tutorial images from https://chess24.com
# Citation: Music is from https://www.youtube.com/watch?v=kQRpogpId4w

from tkinter import *
import PIL.Image
import PIL.ImageTk
import ChessBoard as CB
import BackEndChess as BackEnd
from Client import *
import socket
import threading
from queue import Queue
import AISearchAlgs as AI
import pygame
import imageio

# Makes the initial start screen.
def startScreen(canvas, data):
    anImage = PIL.Image.open("./PieceImages/coolchesspicture.jpg")
    anImage = anImage.resize((int(data.width*1.5), int(data.height*1.1)), PIL.Image.ANTIALIAS)
    aPhoto = PIL.ImageTk.PhotoImage(anImage)
    aLabel = Label(image=aPhoto)
    aLabel.image = aPhoto
    canvas.create_image(data.width/2+data.margin*2, data.height/2,image = aPhoto)
    for col in range(7):
        if col%2 == 0:
            canvas.create_rectangle(data.margin+col*int(data.width/7.5), 
            14.6296*data.margin+int(data.height/7),
            data.margin+(col+1)*int(data.width/7.5), 
            14.6296*data.margin+2*int(data.height/7), 
            fill = "tan", width = data.height//100)
        else:
            canvas.create_rectangle(data.margin+col*int(data.width/7.5), 
            14.6296*data.margin+int(data.height/7),
            data.margin+(col+1)*int(data.width/7.5), 
            14.6296*data.margin+2*int(data.height/7), 
            fill = "brown", width = data.height//100)
        if data.hover != None:
            canvas.create_rectangle(data.hover[0], data.hover[1], 
                                    data.hover[2], data.hover[3], fill = "yellow")
    canvas.create_text(data.width/2, data.height/5,
                        text = "Welcome to Intellichess",
                        font = "fixedsys "+str(int(data.width/15))+" bold",
                        fill = "Black")
    canvas.create_text(data.width/2, data.height/2,
                        text = "Select One of the Below Options to Begin",
                        font = "fixedsys "+str(int(data.width/30)), fill = "White", 
                        )
    # Modes for player to select
    canvas.create_text(data.x1, data.y,
                        text = "tutorial", 
                        font = "fixedsys "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_text(data.x2, data.y,
                        text = "training", 
                        font = "fixedsys "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_text(data.x3, data.y,
                        text = "competitive", 
                        font = "fixedsys "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_text(data.x4, data.y,
                        text = "multiplayer", 
                        font = "fixedsys "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_text((data.x2+data.x1)/2.6, data.margin, 
                       text = "Toggle Music: "+data.music,
                       font = "courier "+str(int(data.width/30)))

# Makes and updates drawings of tutorial screen when player has made some selection.
def tutorialScreen(canvas, data):
    anImage = PIL.Image.open("./PieceImages/coolchesspicture.jpg")
    anImage = anImage.resize((int(data.width*1.5), int(data.height*1.1)), PIL.Image.ANTIALIAS)
    aPhoto = PIL.ImageTk.PhotoImage(anImage)
    aLabel = Label(image=aPhoto)
    aLabel.image = aPhoto
    canvas.create_image(data.width/2+data.margin*2, data.height/2,image = aPhoto)
    canvas.create_text(data.width/2, data.height*.03, 
                       text = "Tutorial",
                       font = "courier "+str(int(data.width/25))+" underline bold")
    canvas.create_text(data.width*.053, data.height*.0273, 
                       text = "Back",
                       font = "courier "+str(int(data.width/26)))
    for col in range(7):
        if col%2 == 0:
            canvas.create_rectangle(data.margin+col*int(data.width/7.5), 
            14.6296*data.margin+int(data.height/7),
            data.margin+(col+1)*int(data.width/7.5), 
            14.6296*data.margin+2*int(data.height/7), 
            fill = "tan", width = data.height//100)
        else:
            canvas.create_rectangle(data.margin+col*int(data.width/7.5), 
            14.6296*data.margin+int(data.height/7),
            data.margin+(col+1)*int(data.width/7.5), 
            14.6926*data.margin+2*int(data.height/7), 
            fill = "brown", width = data.height//100)
        if data.hover != None:
            canvas.create_rectangle(data.hover[0], data.hover[1], 
                                    data.hover[2], data.hover[3], fill = "yellow")
        if data.instructImage != None:
            instructImage = PIL.Image.open(data.instructImage)
            instructImage = instructImage.resize((int(data.width/2), int(data.height/8*5)), PIL.Image.ANTIALIAS)
            instructPhoto = PIL.ImageTk.PhotoImage(instructImage)
            instructLabel = Label(image=instructPhoto)
            instructLabel.image = instructPhoto
            canvas.create_image(data.width/2, data.height/8*3,image = instructPhoto)
    canvas.create_text(data.x1, data.y,
                        text = "pawn", 
                        font = "fixedsys "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_text((data.x2+data.x1)/2, data.y,
                        text = "rook", 
                        font = "fixedsys "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_text(data.x2, data.y,
                        text = "knight", 
                        font = "fixedsys "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_text((data.x3+data.x2)/2, data.y,
                        text = "bishop", 
                        font = "fixedsys "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_text(data.x3, data.y,
                        text = "queen", 
                        font = "fixedsys "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_text((data.x4+data.x3)/2, data.y,
                        text = "king", 
                        font = "fixedsys "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_text(data.x4, data.y,
                        text = "castling", 
                        font = "fixedsys "+str(int(data.width/44)),
                        fill = "black")

# Makes and updates drawings of single player game board when player makes a move.
def trainingScreen(canvas, data):
    anImage = PIL.Image.open("./PieceImages/coolchesspicture.jpg")
    anImage = anImage.resize((int(data.width*1.5), int(data.height*1.1)), PIL.Image.ANTIALIAS)
    aPhoto = PIL.ImageTk.PhotoImage(anImage)
    aLabel = Label(image=aPhoto)
    aLabel.image = aPhoto
    canvas.create_image(data.width/2+data.margin*2, data.height/2,image = aPhoto)
    data.mainBoard.drawBoard(canvas)
    canvas.create_text(data.width/2, data.height*.03, 
                       text = "Training",
                       font = "courier "+str(int(data.width/25))+" underline bold")
    canvas.create_text(data.width*.053, data.height*.0273, 
                       text = "Back",
                       font = "courier "+str(int(data.width/26)))
    sameBoards(canvas, data)

# Makes and updates drawings of game board when player or AI makes a move.
def competitiveScreen(canvas, data):
    anImage = PIL.Image.open("./PieceImages/coolchesspicture.jpg")
    anImage = anImage.resize((int(data.width*1.5), int(data.height*1.1)), PIL.Image.ANTIALIAS)
    aPhoto = PIL.ImageTk.PhotoImage(anImage)
    aLabel = Label(image=aPhoto)
    aLabel.image = aPhoto
    canvas.create_image(data.width/2+data.margin*2, data.height/2,image = aPhoto)
    data.mainBoard.drawBoard(canvas)
    canvas.create_text(data.width/2, data.height*.03, 
                       text = "Competitive",
                       font = "courier "+str(int(data.width/25))+" underline bold")
    canvas.create_text(data.width/20*18, data.height/25, text = "You are "+data.player,
                       font = "courier "+str(int(data.width/40)), fill = data.player)
    canvas.create_text(data.width*.053, data.height*.0273, 
                       text = "Back",
                       font = "courier "+str(int(data.width/26)))
    sameBoards(canvas, data)

# Makes and updates drawings of the game board when either player makes a move.
def multiplayerScreen(canvas, data):
    anImage = PIL.Image.open("./PieceImages/coolchesspicture.jpg")
    anImage = anImage.resize((int(data.width*1.5), int(data.height*1.1)), PIL.Image.ANTIALIAS)
    aPhoto = PIL.ImageTk.PhotoImage(anImage)
    aLabel = Label(image=aPhoto)
    aLabel.image = aPhoto
    canvas.create_image(data.width/2+data.margin*2, data.height/2,image = aPhoto)
    data.mainBoard.drawBoard(canvas)
    canvas.create_text(data.width/2, data.height*.03, 
                       text = "Multiplayer",
                       font = "courier "+str(int(data.width/25))+" underline bold")
    canvas.create_text(data.width*.053, data.height*.0273, 
                       text = "Back",
                       font = "courier "+str(int(data.width/26)))
    if data.other.ID != None:
        sameBoards(canvas, data)
        canvas.create_text(data.width/20*18, data.height/25, text = "You are "+data.me.ID,
                           font = "courier "+str(int(data.width/40)), fill = data.me.ID)
    else:
        canvas.create_rectangle(5*data.margin, data.height//2-3*data.margin, 
        data.width-5*data.margin, data.height//2+3*data.margin,
        fill = "Grey")
        canvas.create_text(data.width//2, data.height//2, text = "Waiting for second player...",
        fill = "tan", font = "fixedsys "+str(int(data.r/1.4)))

# This function is called to draw moves and board screen for the three playing modes.
def sameBoards(canvas, data):
    if data.mainBoard.kingCheck != None:
        canvas.create_rectangle(data.mainBoard.horMargin+data.mainBoard.kingCheck[1]*data.mainBoard.cellWidth,
                                data.mainBoard.vertMargin+data.mainBoard.kingCheck[0]*data.mainBoard.cellHeight,
                                data.mainBoard.horMargin+(data.mainBoard.kingCheck[1]+1)*data.mainBoard.cellWidth,
                                data.mainBoard.vertMargin+(data.mainBoard.kingCheck[0]+1)*data.mainBoard.cellHeight,
                                fill = "red2")
    if data.mainBoard.clicked:
        canvas.create_rectangle(data.mainBoard.horMargin+data.mainBoard.colClick*data.mainBoard.cellWidth,
                                data.mainBoard.vertMargin+data.mainBoard.rowClick*data.mainBoard.cellHeight,
                                data.mainBoard.horMargin+(data.mainBoard.colClick+1)*data.mainBoard.cellWidth,
                                data.mainBoard.vertMargin+(data.mainBoard.rowClick+1)*data.mainBoard.cellHeight,
                                fill = "yellow")
    initialize(canvas, data)
    drawImages(canvas, data)
    canvas.create_rectangle(data.width/2-3*data.r, data.height/20*18.4,
                            data.width/2+3*data.r, data.height/20*19.8,
                            fill = "grey")
    if data.mainBoard.turn == "White":
        canvas.create_text(data.width/2, data.height/20*19.08, 
                        text = "White's turn",
                        font = "courier "+str(int(data.width/25)), fill = "White")
    else:
        canvas.create_text(data.width/2, data.height/20*19.08, 
                        text = "Black's turn",
                        font = "courier "+str(int(data.width/25)), fill = "Black")

# Switches game mode if player selects an option on the start screen. If player clicks back then it takes them
# back to the home screen.
def gameMode(event, data):
    if data.mode != "beginning":
        if 0 <= event.x <= data.width*.1:
            if 0 <= event.y <= data.height*.04615:
                init(data)
    else:
        if 0 <= event.x <= data.width*.3412:
            if 0 <= event.y <= data.height*.0615:
                if data.music == "On":
                    data.music = "Off"
                    pygame.mixer.music.pause()
                else:
                    data.music = "On"
                    pygame.mixer.init()
                    pygame.mixer.music.load(songDir)
                    pygame.mixer.music.play(-1)
        if data.x1-data.r <= event.x <= data.x1+data.r:
            if data.y-data.r <= event.y <= data.y+data.r:
                data.mode = "tutorial"
        if data.x2-data.r <= event.x <= data.x2+data.r:
            if data.y-data.r <= event.y <= data.y+data.r:
                data.mode = "training"
        if data.x3-data.r <= event.x <= data.x3+data.r:
            if data.y-data.r <= event.y <= data.y+data.r:
                data.mode = "competitive"
        if data.x4-data.r <= event.x <= data.x4+data.r:
            if data.y-data.r <= event.y <= data.y+data.r:
                data.mode = "multiplayer"

# If the player is on some current game board this calls the moveClick and mouseClick functions
# to indicate that a player has either selected a piece or made a move. 
def moveWithMouse(event, data):
    if data.checkMate == None:
        if data.mainBoard.clicked:
            if data.mode == "multiplayer":
                if data.other.ID != None:
                    data.mainBoard.moveClick(event.x, event.y, data.me.ID, data)
                    if data.moved:
                        sendMoveMessage(data)
                        if data.checkMate != None:
                            sendCheckMate(data)
                        data.moved = False
            else:
                data.mainBoard.moveClick(event.x, event.y, data.player, data)
                if data.mode == "training":
                    data.player = data.mainBoard.turn
                elif data.mode == "competitive":
                    data.timerFiredCount = 0
        else:
            if data.mode == "multiplayer":
                data.mainBoard.mouseClick(event.x, event.y, data.me.ID)
            else:
                data.mainBoard.mouseClick(event.x, event.y, data.player)


# This is used to create a new person when another player is initiated in multiplayer mode.
class Person(object):
    def __init__(self, board, ID = None):
        self.board = board
        self.ID = ID

def init(data):
    data.mode = "beginning"
    data.y = data.height/4*3.3
    data.x1 = data.width*.098
    data.x2 = data.width*.3629
    data.x3 = data.width/20*12.6
    data.x4 = data.width/19*17
    data.r = data.width/17
    data.margin = int(data.width/31)
    data.mainBoard = CB.Board(data.width, data.height)
    data.mainBoard.makeBoard()
    data.player = "White"
    data.timerFiredCount = 0
    data.origRow = None
    data.origCol = None
    data.newRow = None
    data.newCol = None
    data.moved = False
    data.hover = None
    data.checkMate = None
    data.instructImage = "./MoveImages/MovePawn.png"
    data.music = "On"
    try:
        return data.other.ID
    except:
        data.me = Person(data.mainBoard)
        data.other = Person(data.mainBoard)


# Sets the canvas to store the current pieces on the board.
def initialize(canvas, data):
    canvas.shapes = data.mainBoard.drawings

# Draws the pieces to the current board.
def drawImages(canvas, data):
    for key in canvas.shapes:
        im = PIL.Image.open(canvas.shapes[key])
        im = im.resize((int(data.width/5.8-data.mainBoard.horMargin), int(data.height/5.7-data.mainBoard.vertMargin)), 
                        PIL.Image.ANTIALIAS)
        ph = PIL.ImageTk.PhotoImage(im)
        label = Label(canvas, image=ph)
        label.image=ph
        canvas.create_image(int(key[1]*data.mainBoard.cellWidth+data.mainBoard.cellWidth*(26/20)), 
                            int(key[0]*data.mainBoard.cellHeight+data.mainBoard.cellHeight*(26/20)),
                            image=ph)

# Determines for mouse functions which state player is in.
def mousePressed(event, data):
    if data.mode != "beginning":
        if data.mode == "tutorial":
            tutorialMouse(event, data)
        else:
            moveWithMouse(event, data)
    gameMode(event, data)


def keyPressed(event, data):
    pass

# Used to tell AI when to move and update start/tutorial screens when they are clicked.
def timerFired(data):
    data.timerFiredCount += 1
    if data.mode != "beginning":
        data.mainBoard.convertPawns()
    if data.mode == "multiplayer":
        clientTimerFired(data)
    elif data.mode == "competitive" and data.mainBoard.turn == "Black" and data.timerFiredCount == 2:
        newBoard = AI.minimaxSearch(data.mainBoard.board, "Black", data)
        data.mainBoard.board = newBoard
        data.mainBoard.turn = "White"
    elif data.mode == "tutorial":
        changeTutorialImage(data)

# Draws whichever screen player is in.
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
    if data.checkMate == "Black":
        canvas.create_rectangle(5*data.margin, data.height//2-3*data.margin, 
        data.width-5*data.margin, data.height//2+3*data.margin,
        fill = "Grey")
        canvas.create_text(data.width//2, data.height//2.1, text = "Game Over",
        fill = "tan", font = "fixedsys 20 bold")
        canvas.create_text(data.width//2, data.height//1.9, text = "White Wins",
        fill = "white", font = "fixedsys 20 bold")
    elif data.checkMate == "White":
        canvas.create_rectangle(5*data.margin, data.height//2-3*data.margin, 
        data.width-5*data.margin, data.height//2+3*data.margin,
        fill = "Grey")
        canvas.create_text(data.width//2, data.height//2.1, text = "Game Over",
        fill = "tan", font = "fixedsys 20 bold")
        canvas.create_text(data.width//2, data.height//1.9, text = "Black Wins",
        fill = "black", font = "fixedsys 20 bold")

# Tells the game which box should be highlighted when in start/tutorial mode.
def motion(event, data):
    if data.mode == "beginning":
        if data.margin <= event.x <= data.margin+int(data.width/7.5):
            if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
                data.hover = [data.margin, 15*data.margin-10+int(data.height/7), data.margin+int(data.width/7.5), 15*data.margin-10+2*int(data.height/7)]
        elif data.margin+2*int(data.width/7.5) <= event.x <= data.margin+3*int(data.width/7.5):
            if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
                data.hover = [data.margin+2*int(data.width/7.5), 15*data.margin-10+int(data.height/7), data.margin+3*int(data.width/7.5), 15*data.margin-10+2*int(data.height/7)]
        elif data.margin+4*int(data.width/7.5) <= event.x <= data.margin+5*int(data.width/7.5):
            if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
                data.hover = [data.margin+4*int(data.width/7.5), 15*data.margin-10+int(data.height/7), data.margin+5*int(data.width/7.5), 15*data.margin-10+2*int(data.height/7)]
        elif data.margin+6*int(data.width/7.5) <= event.x <= data.margin+7*int(data.width/7.5):
            if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
                data.hover = [data.margin+6*int(data.width/7.5), 15*data.margin-10+int(data.height/7), data.margin+7*int(data.width/7.5), 15*data.margin-10+2*int(data.height/7)]
        else:
            data.hover = None
    elif data.mode == "tutorial":
        if data.margin <= event.x <= data.margin+int(data.width/7.5):
            if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
                data.hover = [data.margin, 15*data.margin-10+int(data.height/7), data.margin+int(data.width/7.5), 15*data.margin-10+2*int(data.height/7)]
        elif data.margin+2*int(data.width/7.5) <= event.x <= data.margin+3*int(data.width/7.5):
            if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
                data.hover = [data.margin+2*int(data.width/7.5), 15*data.margin-10+int(data.height/7), data.margin+3*int(data.width/7.5), 15*data.margin-10+2*int(data.height/7)]
        elif data.margin+4*int(data.width/7.5) <= event.x <= data.margin+5*int(data.width/7.5):
            if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
                data.hover = [data.margin+4*int(data.width/7.5), 15*data.margin-10+int(data.height/7), data.margin+5*int(data.width/7.5), 15*data.margin-10+2*int(data.height/7)]
        elif data.margin+6*int(data.width/7.5) <= event.x <= data.margin+7*int(data.width/7.5):
            if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
                data.hover = [data.margin+6*int(data.width/7.5), 15*data.margin-10+int(data.height/7), data.margin+7*int(data.width/7.5), 15*data.margin-10+2*int(data.height/7)]
        elif data.margin+int(data.width/7.5) <= event.x <= data.margin+2*int(data.width/7.5):
            if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
                data.hover = [data.margin+int(data.width/7.5), 15*data.margin-10+int(data.height/7), data.margin+2*int(data.width/7.5), 15*data.margin-10+2*int(data.height/7)]
        elif data.margin+3*int(data.width/7.5) <= event.x <= data.margin+4*int(data.width/7.5):
            if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
                data.hover = [data.margin+3*int(data.width/7.5), 15*data.margin-10+int(data.height/7), data.margin+4*int(data.width/7.5), 15*data.margin-10+2*int(data.height/7)]
        elif data.margin+5*int(data.width/7.5) <= event.x <= data.margin+6*int(data.width/7.5):
            if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
                data.hover = [data.margin+5*int(data.width/7.5), 15*data.margin-10+int(data.height/7), data.margin+6*int(data.width/7.5), 15*data.margin-10+2*int(data.height/7)]
        else:
            data.hover = None

# Indicates which tutorial image to show based on which option is clicked.
def tutorialMouse(event, data):
    if data.margin <= event.x <= data.margin+int(data.width/7.5):
        if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
            data.instructImage = "./MoveImages/MovePawn.png"
    elif data.margin+2*int(data.width/7.5) <= event.x <= data.margin+3*int(data.width/7.5):
        if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
            data.instructImage = "./MoveImages/RegKnight.png"
    elif data.margin+4*int(data.width/7.5) <= event.x <= data.margin+5*int(data.width/7.5):
        if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
            data.instructImage = "./MoveImages/RegQueen.png"
    elif data.margin+6*int(data.width/7.5) <= event.x <= data.margin+7*int(data.width/7.5):
        if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
            data.instructImage = "./MoveImages/RegCastle.png"
    elif data.margin+int(data.width/7.5) <= event.x <= data.margin+2*int(data.width/7.5):
        if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
            data.instructImage = "./MoveImages/RegRook.png"
    elif data.margin+3*int(data.width/7.5) <= event.x <= data.margin+4*int(data.width/7.5):
        if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
            data.instructImage = "./MoveImages/RegBishop.png"
    elif data.margin+5*int(data.width/7.5) <= event.x <= data.margin+6*int(data.width/7.5):
        if 15*data.margin-10+int(data.height/7) <= event.y <= 15*data.margin-10+2*int(data.height/7):
            data.instructImage = "./MoveImages/RegKing.png"
    
# Changes the tutorial image after a certain period of time for tutorial move animation.
def changeTutorialImage(data):
    if data.timerFiredCount%7 == 0:
        # Pawn Images
        if data.instructImage == "./MoveImages/MovePawn.png":
            data.instructImage = "./MoveImages/RegPawn.png"
        elif data.instructImage == "./MoveImages/RegPawn.png":
            data.instructImage = "./MoveImages/TakePawn.png"
        elif data.instructImage == "./MoveImages/TakePawn.png":
            data.instructImage = "./MoveImages/MovePawn.png"
        # Rook Images
        elif data.instructImage == "./MoveImages/RegRook.png":
            data.instructImage = "./MoveImages/MoveRook.png"
        elif data.instructImage == "./MoveImages/MoveRook.png":
            data.instructImage = "./MoveImages/RegRook.png"
        # Knight Images
        elif data.instructImage == "./MoveImages/RegKnight.png":
            data.instructImage = "./MoveImages/MoveKnight.png"
        elif data.instructImage == "./MoveImages/MoveKnight.png":
            data.instructImage = "./MoveImages/RegKnight.png"
        # Bishop Images
        elif data.instructImage == "./MoveImages/RegBishop.png":
            data.instructImage = "./MoveImages/MoveBishop.png"
        elif data.instructImage == "./MoveImages/MoveBishop.png":
            data.instructImage = "./MoveImages/RegBishop.png"
        # Queen Images
        elif data.instructImage == "./MoveImages/RegQueen.png":
            data.instructImage = "./MoveImages/MoveQueen.png"
        elif data.instructImage == "./MoveImages/MoveQueen.png":
            data.instructImage = "./MoveImages/RegQueen.png"
        # King Images
        elif data.instructImage == "./MoveImages/RegKing.png":
            data.instructImage = "./MoveImages/MoveKing.png"
        elif data.instructImage == "./MoveImages/MoveKing.png":
            data.instructImage = "./MoveImages/RegKing.png"
        # Castling Images
        elif data.instructImage == "./MoveImages/RegCastle.png":
            data.instructImage = "./MoveImages/MoveCastle.png"
        elif data.instructImage == "./MoveImages/MoveCastle.png":
            data.instructImage = "./MoveImages/RegCastle.png"



# Citation: 15-112 animation framework.

def run(width=300, height=300, serverMsg = None, server = None):
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

    def motionWrapper(event, canvas, data):
        motion(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.server = server
    data.serverMsg = serverMsg
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    root.resizable(width=False, height=False)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    initialize(canvas, data)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    if data.mode == "beginning" or data.mode == "tutorial":
        root.bind('<Motion>', lambda event:
                                motionWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()
songDir = "./MozartPianoConcertoNo4Andante.mp3"
pygame.mixer.init()
pygame.mixer.music.load(songDir)
pygame.mixer.music.play(-1)
run(850, 650, serverMsg, server)