#############################
# Sockets Client Demo
# by Rohan Varma
# adapted by Kyle Chin
#############################

import socket
import threading
from queue import Queue
from FinalProject import *

HOST = "128.237.218.212" # put your IP address here if playing on multiple computers
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
import random
####################################
# customize these functions
####################################

#def multiplayerInit(data):
#  data.me = ["White", data.mainBoard.board]
#  data.otherStrangers = dict()

def sendMoveMessage(data):
  msg = "playerMoved %d %d %d %d %s \n" %(data.origRow, data.origCol, data.newRow, data.newCol, data.mainBoard.turn)
  if (msg != ""):
    print ("sending: ", msg,)
    data.server.send(msg.encode())

def sendCheckMate(data):
  msg = "checkMate %s \n" %(data.checkMate)
  if (msg != ""):
    print ("sending: ", msg,)
    data.server.send(msg.encode())

def keyPressed(event, data):
    pass

def clientTimerFired(data):
    # timerFired receives instructions and executes them
    while (data.serverMsg.qsize() > 0):
      msg = data.serverMsg.get(False)
      print("MESSAGE", msg)
      try:
        print("received: ", msg, "\n")
        msgL = msg.split()
        command = msgL[0]

        if (command == "myIDis"):
          data.me.ID = msgL[1]
          print(msgL[1])

        elif (command == "newPlayer"):
          data.other.ID = msgL[1]
          print(msgL[1])

        elif (command == "playerMoved"):
          oldRow = int(msgL[2])
          oldCol = int(msgL[3])
          newRow = int(msgL[4])
          newCol = int(msgL[5])
          data.mainBoard.turn = msgL[6]
          data.mainBoard.board[newRow][newCol] = data.mainBoard.board[oldRow][oldCol]
          data.mainBoard.board[newRow][newCol].posRow = newRow
          data.mainBoard.board[newRow][newCol].posCol = newCol
          data.mainBoard.board[oldRow][oldCol] = None

        elif (command == "checkMate"):
          data.checkMate = msgL[2]



#          print(ast.literal_eval(s))
#          board = ast.literal_eval(s)
#          data.other.board.board = data.mainBoard

      except:
        print("failed")
      data.serverMsg.task_done()