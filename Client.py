#############################
# Sockets Client Demo
# by Rohan Varma
# adapted by Kyle Chin
#############################

import socket
import threading
import ast
from queue import Queue
from FinalProject import *

HOST = "128.237.184.27" # put your IP address here if playing on multiple computers
PORT = 50003
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST,PORT))
print("connected to server")

def handleServerMsg(server, serverMsg):
  server.setblocking(1)
  msg = ""
  command = ""
  while True:
    msg += server.recv(10).decode("UTF-8")
    command = msg.split("\n")
    while (len(command) > 1):
      readyMsg = command[0]
      msg = "\n".join(command[1:])
      serverMsg.put(readyMsg)
      command = msg.split("\n")

# events-example0.py from 15-112 website
# Barebones timer, mouse, and keyboard events

from tkinter import *
from FinalProject import *
import random
####################################
# customize these functions
####################################

def multiplayerInit(data):
    data.me = ["White", data.mainBoard.board]
    data.otherStrangers = dict()

def multiplayerMouse(event, data):
    moveWithMouse(event, data)
    msg = "playerMoved %l \n" % data.mainBoard.board
    if (msg != ""):
      print ("sending: ", msg,)
      data.server.send(msg.encode())

def keyPressed(event, data):
    pass

def clientTimerFired(data):
    # timerFired receives instructions and executes them
    while (serverMsg.qsize() > 0):
      msg = serverMsg.get(False)
      try:
        print("received: ", msg, "\n")
        msg = msg.split()
        command = msg[0]

        if (command == "myIDis"):
          myPID = msg[1]
          data.me.changePID(myPID)

        elif (command == "newPlayer"):
          newPID = msg[1]
          data.otherStrangers[newPID] = ["Black", data.mainBoard]

        elif (command == "playerMoved"):
          PID = msg[1]
          board = ast.literal_eval(msg[2])
          data.otherStrangers[PID].board = board

      except:
        print("failed")
      serverMsg.task_done()

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