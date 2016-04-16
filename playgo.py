#!/usr/bin/python
import pygame, sys
from pygame.locals import *

#COLOR TABLE 	R    G    B
WHITE		= (255,	255, 255)
BLACK 		= (  0,   0,   0)
TAN			= (224,	176,  54)

#Game Options
FPS = 20
STARTSCREENFONT = "arial"
WINWIDTH = 800
WINHEIGHT = 600

def main():
	global DISPLAY, FPSCLOCK
	pygame.init()
	pygame.display.set_caption("PlayGo!")
	DISPLAY = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
	FPSCLOCK = pygame.time.Clock()
	
	grid = showStartScreen()

def showStartScreen():
	mousex = 0
	mousey = 0
	
	titleFontObj = pygame.font.SysFont(STARTSCREENFONT, 40)
	titleFontObj.set_underline(True)
	titleText = titleFontObj.render("Start Game", True, BLACK)
	titleTextRect = titleText.get_rect()
	titleTextRect.center = (WINWIDTH * 0.5, WINHEIGHT * 0.1)
	
	gridSizeTextObj = pygame.font.SysFont(STARTSCREENFONT, 30)
	gridSizeText = gridSizeTextObj.render("Grid Size", True, BLACK)
	gridSizeTextRect = gridSizeText.get_rect()
	gridSizeTextRect.center = (WINWIDTH * 0.5, WINHEIGHT * 0.22)
	
	gameModeTextObj = pygame.font.SysFont(STARTSCREENFONT, 30)
	gameModeText = gameModeTextObj.render("Game Mode", True, BLACK)
	gameModeTextRect = gameModeText.get_rect()
	gameModeTextRect.center = (WINWIDTH * 0.5, WINHEIGHT * 0.44)
	
	nameTextObj = pygame.font.SysFont(STARTSCREENFONT, 30)
	nameText = nameTextObj.render("Name", True, BLACK)
	nameTextRect = nameText.get_rect()
	nameTextRect.center = (WINWIDTH * 0.5, WINHEIGHT * 0.66)
	 
	while True:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP:
				pygame.quit()
				sys.exit()
		
		DISPLAY.fill(TAN)
		
		DISPLAY.blit(titleText, titleTextRect)
		DISPLAY.blit(gridSizeText, gridSizeTextRect)
		DISPLAY.blit(gameModeText, gameModeTextRect)
		DISPLAY.blit(nameText, nameTextRect)
		pygame.display.update()
		
		FPSCLOCK.tick(FPS)

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
		

if __name__ == "__main__":
    main()

# Test instantiation of Player 1
"""
name = "Test Player"
color = "white"
player1 = Player(color,name)
print "Player name is: " + name + " and color is:", color
"""

