import pygame, sys
import config as c
import board as board
from pygame.locals import *


def main():
	global DISPLAY, FPSCLOCK
	pygame.init()
	pygame.display.set_caption("PlayGo!")
	DISPLAY = pygame.display.set_mode((c.WINWIDTH, c.WINHEIGHT))
	FPSCLOCK = pygame.time.Clock()
	
	gridsize = board.showStartScreen(DISPLAY, pygame.time.Clock()) 		#Make this a tuple to collect game mode and names
	playGo(gridsize)

	
def playGo(gridsize):
	mousex = 0
	mousey = 0
	
	boxStartY = 75
	gridDimension = c.WINHEIGHT - (boxStartY * 2)
	boxDimension = gridDimension / gridsize
	boxStartX = (c.WINWIDTH / 2) - (boxDimension * (float(gridsize) / 2))
	
	for i in range (0, gridsize):
		for j in range(0, gridsize):
			pygame.draw.rect(DISPLAY, c.BLACK, (boxStartX + (i * boxDimension), boxStartY + (j * boxDimension), boxDimension, boxDimension), 2)
	
	boardDimension = gridDimension + boxDimension
	boardStartX = boxStartX - (boxDimension / 2)
	boardStartY = boxStartY - (boxDimension / 2)
	boardSurface = pygame.Surface((boardDimension, boardDimension))
	boardSurface.fill(c.TAN)
	boardSurface.set_alpha(1)
	boardArr = []
	for i in range (0, gridsize + 1):
		for j in range (0, gridsize + 1):
			boardArr.append( pygame.draw.circle(boardSurface, LTGRAY, ((boxDimension / 2) + (i * boxDimension), (boxDimension / 2) + (j * boxDimension)), boxDimension / 3) )
	
	cont = True
	while cont:
		
		
		mousePress = False
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP:
				if event.button == 1:
					mousex, mousey = event.pos
					mousePress = True
			elif event.type == MOUSEMOTION:
					mousex, mousey = event.pos
			elif event.type == KEYUP:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
		
		pieceSurface = pygame.Surface((boardDimension, boardDimension))
		pieceSurface.fill(c.TAN)
		pieceArr = []
		for i in range (0, gridsize + 1):
			for j in range (0, gridsize + 1):
				pieceArr.append(False)
		
		for i in range (0, gridsize + 1):
			for j in range (0, gridsize + 1):
				if boardArr[(gridsize + 1) * i + j].collidepoint(mousex - boardStartX, mousey - boardStartY):
					pygame.draw.circle(pieceSurface, LTGRAY, ((boxDimension / 2) + (i * boxDimension), (boxDimension / 2) + (j * boxDimension)), boxDimension / 3)
				else:
					pygame.draw.circle(pieceSurface, c.TAN, ((boxDimension / 2) + (i * boxDimension), (boxDimension / 2) + (j * boxDimension)), boxDimension / 3)

		if mousePress:
			for i in range (0, gridsize + 1):
				for j in range (0, gridsize + 1):
					if boardArr[(gridsize + 1) * i + j].collidepoint(mousex - boardStartX, mousey - boardStartY):
						print i, j
						
		DISPLAY.blit(pieceSurface, (boardStartX, boardStartY))
		
		for i in range (0, gridsize):
			for j in range(0, gridsize):
				pygame.draw.rect(DISPLAY, c.BLACK, (boxStartX + (i * boxDimension), boxStartY + (j * boxDimension), boxDimension, boxDimension), 2)
						
		pygame.display.update()
	

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

# Test insc.TANtiation of Player 1
"""
name = "Test Player"
color = "white"
player1 = Player(color,name)
print "Player name is: " + name + " and color is:", color
"""

