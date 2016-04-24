import pygame, sys
import config as c
import board as board
from pygame.locals import *

PLAYER1NAME = "Player 1"
PLAYER2NAME = "Player 2"

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
	
	player1 = Player(c.WHITE, PLAYER1NAME)
	player2 = Player(c.BLACK, PLAYER2NAME)
	
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
			boardArr.append( pygame.draw.circle(boardSurface, c.LTGRAY, ((boxDimension / 2) + (i * boxDimension), (boxDimension / 2) + (j * boxDimension)), boxDimension / 3) )
	
	
	#UI Overlay
	pygame.draw.rect(DISPLAY, c.WHITE, (0, 0, c.WINWIDTH, boxStartY))
	pygame.draw.rect(DISPLAY, c.WHITE, (0, boardStartY + boardDimension - (boxDimension / 2), c.WINWIDTH, boxStartY))
	
	p1TextObj = pygame.font.SysFont(c.STARTSCREENFONT, 30)
	p1Text = p1TextObj.render(player1.name, True, c.BLACK)
	p1TextRect = p1Text.get_rect()
	p1TextRect.center = (75, 20)
	
	p2TextObj = pygame.font.SysFont(c.STARTSCREENFONT, 30)
	p2Text = p2TextObj.render(player2.name, True, c.BLACK)
	p2TextRect = p2Text.get_rect()
	p2TextRect.center = (c.WINWIDTH - 75, 20)
	
	passButtonObj = pygame.font.SysFont(c.STARTSCREENFONT, 25)
	passButton = passButtonObj.render("  PASS  ", True, c.BLACK)
	passButtonRect = passButton.get_rect()
	passButtonRect.center = (c.WINWIDTH - 75, boardDimension + 75)
	gridSize11Rect = pygame.draw.rect(DISPLAY, c.BLACK, passButtonRect.inflate(20, 5), 1)
	
	DISPLAY.blit(p1Text, p1TextRect)
	DISPLAY.blit(p2Text, p2TextRect)
	DISPLAY.blit(passButton, passButtonRect)
	
	currentplayer = player1
	
	placedPieces = []
	for i in range (0, gridsize + 1):
		for j in range (0, gridsize + 1):
			placedPieces.append([False, currentplayer]) 		#First item is if the piece exists, 2nd item False = white, True = black to enable pieces with outlines
	
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
		
		tempCirX = 0
		tempCirY = 0
		for i in range (0, gridsize + 1):
			for j in range (0, gridsize + 1):
				if boardArr[(gridsize + 1) * i + j].collidepoint(mousex - boardStartX, mousey - boardStartY):
					tempCirX = (boxDimension / 2) + (i * boxDimension)
					tempCirY = (boxDimension / 2) + (j * boxDimension)
		
		pygame.draw.rect(pieceSurface, c.WHITE, (0, 0, boardDimension, boxDimension / 2))
		pygame.draw.rect(pieceSurface, c.WHITE, (0, boardDimension - (boxDimension / 2), boardDimension, boxDimension / 2)) 
		if (tempCirX and tempCirY):
			pygame.draw.circle(pieceSurface, c.LTGRAY, (tempCirX, tempCirY), boxDimension / 3)
		#else:
		#	pygame.draw.circle(pieceSurface, c.TAN, (tempCirX, tempCirY), boxDimension / 3)

		if mousePress:
			for i in range (0, gridsize + 1):
				for j in range (0, gridsize + 1):
					if boardArr[(gridsize + 1) * i + j].collidepoint(mousex - boardStartX, mousey - boardStartY):
						if not(placedPieces[(gridsize + 1) * i + j][0]): 			#if the piece is not placed yet
							print "adding piece at", i, j, "  ", currentplayer.name
							placedPieces[i * (gridsize + 1) + j] = [True, currentplayer]
							if currentplayer == player1:
								currentplayer = player2
							else:
								currentplayer = player1
						
		DISPLAY.blit(pieceSurface, (boardStartX, boardStartY))
		
		for i in range (0, gridsize):
			for j in range(0, gridsize):
				pygame.draw.rect(DISPLAY, c.BLACK, (boxStartX + (i * boxDimension), boxStartY + (j * boxDimension), boxDimension, boxDimension), 2)
		
		for i in range (0, gridsize + 1):
			for j in range (0, gridsize + 1):
				if placedPieces[i * (gridsize + 1) + j][0]:			
					placedPieces[i * (gridsize + 1) + j][1].placePiece( int(boardStartX + (boxDimension / 2) + (i * boxDimension)), int(boardStartY + (boxDimension / 2) + (j * boxDimension)), boxDimension / 3 )
						
		pygame.display.update()
		FPSCLOCK.tick(c.FPS)
	

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

	def placePiece(self, xcoord, ycoord, pieceWidth):
		pygame.draw.circle(DISPLAY, self.color, (xcoord, ycoord), pieceWidth)
		pygame.draw.circle(DISPLAY, c.BLACK if self.color == c.WHITE else c.WHITE, (xcoord, ycoord), pieceWidth, 1)

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

