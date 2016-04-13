#!/usr/bin/python

class scoreBoard:

	def getScore():
		pass
	
	def getGameHistory():
		pass

	def endGame():
		pass

class Grid:

	def getGrid():
		pass

	def calcValidity():
		pass

	def calcCapture():
		pass

class Piece:

	def __init__(self, color):
		self.color = color

class Player:
	
	def __init__(self, color, name):
		self.color = color
		self.name = name

	def placePiece():
		pass

	def resign():
		pass

	def passMove(): # changed 'pass' to 'passMove' for clarity
		pass

# Test instantiation of Player 1
"""
name = "Test Player"
color = "white"
player1 = Player(color,name)
print "Player name is: " + name + " and color is:", color
"""

