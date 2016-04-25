import pygame, sys
import config as c
import draw
import gamescreen
import startscreen as startscreen
from pygame.locals import *

def main():
	global DISPLAY, FPSCLOCK
	pygame.init()
	pygame.display.set_caption("PlayGo!")
	DISPLAY = pygame.display.set_mode((c.WINWIDTH, c.WINHEIGHT))
	FPSCLOCK = pygame.time.Clock()
	
	gridsize = startscreen.showStartScreen(DISPLAY, pygame.time.Clock()) 		#Make this a tuple to collect game mode and names
	
	player1name = "Player 1"
	player2name = "Player 2"
	player1 = Player(c.BLACK, player1name)
	player2 = Player(c.WHITE, player2name)
	gamescreen.displayGame(gridsize, player1, player2, DISPLAY, FPSCLOCK)
	

class scoreBoard:

	def getScore():
		pass
	
	def getGameHistory():
		pass

	def endGame():
		pass

class Player:
	
	def __init__(self, color, name):
		self.color = color
		self.name = name
		self.captures = 0

	def placePiece(self, xcoord, ycoord, pieceWidth):
		pygame.draw.circle(DISPLAY, self.color, (xcoord, ycoord), pieceWidth)
		pygame.draw.circle(DISPLAY, c.BLACK if self.color == c.WHITE else c.WHITE, (xcoord, ycoord), pieceWidth + 1, 1)

	def resign():
		pass

	def passMove(): # changed 'pass' to 'passMove' for clarity
		pass
		

if __name__ == "__main__":
    main()
	
# Test instantiation of Player 1
"""
name = "Test Player"
color = "white"
player1 = Player(color,name)
print "Player name is: " + name + " and color is:", color
"""

