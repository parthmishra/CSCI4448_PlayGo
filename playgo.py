import pygame, sys
import config as c
import draw
import gamescreen
import startscreen
import endscreen
from pygame.locals import *

def main():
	global DISPLAY, FPSCLOCK
	pygame.init()
	pygame.display.set_caption("PlayGo!")
	DISPLAY = pygame.display.set_mode((c.WINWIDTH, c.WINHEIGHT))
	FPSCLOCK = pygame.time.Clock()
	player1name = "Player 1"
	player2name = "Player 2"
	
	keepPlaying = True
	while keepPlaying:
		print "\nNew game!"
		(gridsize, player1name, player2name) = startscreen.showStartScreen(DISPLAY, pygame.time.Clock(), player1name, player2name) 		#Make this a tuple to collect game mode and names
		player1 = Player(c.BLACK, " " + player1name + " ")
		player2 = Player(c.WHITE, " " + player2name + " ")
		print player1name, " vs. ", player2name, "on", gridsize, "x", gridsize, "\n"
		gamescreen.displayGame(gridsize, player1, player2, DISPLAY, FPSCLOCK)

		keepPlaying = endscreen.displayGame(gridsize, player1, player2, DISPLAY, FPSCLOCK)

class Player:
	
	def __init__(self, color, name):
		self.color = color
		self.name = name
		self.captures = 0
		self.passed = False
		self.resigned = False

	def placePiece(self, xcoord, ycoord, pieceWidth):
		pygame.draw.circle(DISPLAY, self.color, (xcoord, ycoord), pieceWidth)
		pygame.draw.circle(DISPLAY, c.BLACK if self.color == c.WHITE else c.WHITE, (xcoord, ycoord), pieceWidth + 1, 1)

		

if __name__ == "__main__":
    main()
	
# Test instantiation of Player 1
"""
name = "Test Player"
color = "white"
player1 = Player(color,name)
print "Player name is: " + name + " and color is:", color
"""

