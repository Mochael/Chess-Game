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
import random
####################################
# customize these functions
####################################

def multiplayerInit(data):
  data.me = ["White", data.mainBoard.board]
  data.otherStrangers = dict()

def sendMessage(board):
  msg = "playerMoved %s \n" % str(board)
  if (msg != ""):
    print ("sending: ", msg,)
# data.server.send(msg.encode())
    server.send(msg.encode())

'''def multiplayerMouse(event, data):
    moveWithMouse(event, data)
    msg = "playerMoved %l \n" % data.mainBoard.board
    if (msg != ""):
      print ("sending: ", msg,)
      data.server.send(msg.encode())'''

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