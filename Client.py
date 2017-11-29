#############################
# Sockets Client Demo
# by Rohan Varma
# adapted by Kyle Chin
#############################

import socket
import threading
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

#def multiplayerInit(data):
#  data.me = ["White", data.mainBoard.board]
#  data.otherStrangers = dict()

def sendMessage(data):
  msg = "playerMoved %s \n" %str(data.mainBoard.board)
  if (msg != ""):
    print ("sending: ", msg,)
# data.server.send(msg.encode())
    data.server.send(msg.encode())

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
          data.me.board.board = 
          print("WOOOSNISNCEFE")
          print(data.me.board.board)

      except:
        print("failed")
      data.serverMsg.task_done()