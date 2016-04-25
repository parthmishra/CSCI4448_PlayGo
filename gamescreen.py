import pygame, sys, playgo
import config as c
import draw
from pygame.locals import *

def displayGame(gridsize, player1, player2, DISPLAY, FPSCLOCK):
	DISPLAY.fill(c.WHITE)
	mousex = 0
	mousey = 0
	
	gameboard = Grid(DISPLAY, gridsize, 75, player1, player2)
	gameboard.drawGrid()
	
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
		
		gameboard.updateGrid(mousePress, mousex, mousey)
		validLabel = draw.Label(c.STARTSCREENFONT, 20, False, gameboard.getValidStr(), c.RED, 0, 1, 75, -40)
		validLabel.drawRect(DISPLAY, c.WHITE, 0, 0, 0)
		DISPLAY.blit(validLabel.labelText, validLabel.labelRect)		
				
		pygame.display.update()
		FPSCLOCK.tick(c.FPS)
		
class Grid:				#Singleton Pattern
	class __Grid:
		def __init__(self, DISPLAY, gridsize, boxStartY, player1, player2):
			self.gridsize = gridsize
			self.gridDimension = c.WINHEIGHT - (boxStartY * 2)
			self.boxDimension = self.gridDimension / self.gridsize
			self.boardDimension = self.gridDimension + self.boxDimension
			self.boxStartY = boxStartY
			self.boxStartX = (c.WINWIDTH / 2) - (self.boxDimension * (float(gridsize) / 2))
			self.boardStartY = self.boxStartY - (self.boxDimension / 2)
			self.boardStartX = self.boxStartX - (self.boxDimension / 2)
			self.player1 = player1
			self.player2 = player2
			self.currentplayer = player1
			self.display = DISPLAY
			self.boardArr = []
			self.placedPieces = []
			self.validstr = ""
			
		def __drawGrid(self):
			for i in range (0, self.gridsize):
				for j in range(0, self.gridsize):
					pygame.draw.rect(self.display, c.BLACK, (self.boxStartX + (i * self.boxDimension), self.boxStartY + (j * self.boxDimension), self.boxDimension, self.boxDimension), 2)
			
			boardSurface = pygame.Surface((self.boardDimension, self.boardDimension))
			boardSurface.fill(c.TAN)
			boardSurface.set_alpha(1)
			for i in range (0, self.gridsize + 1):
				for j in range (0, self.gridsize + 1):
					self.boardArr.append( pygame.draw.circle(boardSurface, c.LTGRAY, ((self.boxDimension / 2) + (i * self.boxDimension), (self.boxDimension / 2) + (j * self.boxDimension)), self.boxDimension / 3) )
			
			
			#UI Overlay
			pygame.draw.rect(self.display, c.WHITE, (0, 0, c.WINWIDTH, self.boxStartY))
			pygame.draw.rect(self.display, c.WHITE, (0, self.boardStartY + self.boardDimension - (self.boxDimension / 2), c.WINWIDTH, self.boxStartY))
			
			p1Label = draw.Label(c.STARTSCREENFONT, 30, False, self.player1.name, c.BLACK, 0, 0, 75, 20)
			p2Label = draw.Label(c.STARTSCREENFONT, 30, False, self.player2.name, c.BLACK, 1, 0, -75, 20)
			
			
			passButton = draw.Label(c.STARTSCREENFONT, 30, False, " PASS ", c.BLACK, 1, 1, -75, -40)
			passButton.drawRect(self.display, c.BLACK, 0, 0, 1)
			
			for i in range (0, self.gridsize + 1):
				for j in range (0, self.gridsize + 1):
					self.placedPieces.append([False, self.currentplayer])
			
			self.display.blit(p1Label.labelText, p1Label.labelRect)
			self.display.blit(p2Label.labelText, p2Label.labelRect)
			self.display.blit(passButton.labelText, passButton.labelRect)
		
		def __updateGrid(self, mousePress, mousex, mousey):
			pieceSurface = pygame.Surface((self.boardDimension, self.boardDimension))
			pieceSurface.fill(c.TAN)
			
			#Fill edges of board with white
			pygame.draw.rect(pieceSurface, c.WHITE, (0, 0, self.boardDimension, self.boxDimension / 2))													#TOP
			pygame.draw.rect(pieceSurface, c.WHITE, (0, self.boxDimension * self.gridsize + (self.boxDimension / 2), self.boardDimension, 2 * self.boxDimension)) 		#BOTTOM
			pygame.draw.rect(pieceSurface, c.WHITE, (0, 0, self.boxDimension / 2, self.boardDimension))													#LEFT
			pygame.draw.rect(pieceSurface, c.WHITE, (self.boxDimension * self.gridsize + (self.boxDimension / 2), 0, 2 * self.boxDimension, self.boardDimension))		#RIGHT
			
			pieceArr = []
			for i in range (0, self.gridsize + 1):
				for j in range (0, self.gridsize + 1):
					pieceArr.append(False)
			
			tempCirX = 0
			tempCirY = 0
			for i in range (0, self.gridsize + 1):
				for j in range (0, self.gridsize + 1):
					if self.boardArr[(self.gridsize + 1) * i + j].collidepoint(mousex - self.boardStartX, mousey - self.boardStartY):
						tempCirX = (self.boxDimension / 2) + (i * self.boxDimension)
						tempCirY = (self.boxDimension / 2) + (j * self.boxDimension)
						
			if (tempCirX and tempCirY):
				pygame.draw.circle(pieceSurface, c.LTGRAY, (tempCirX, tempCirY), self.boxDimension / 3)
			
			if mousePress:		
				for i in range (0, self.gridsize + 1):
					for j in range (0, self.gridsize + 1):
						if self.boardArr[(self.gridsize + 1) * i + j].collidepoint(mousex - self.boardStartX, mousey - self.boardStartY):
							if not(self.placedPieces[(self.gridsize + 1) * i + j][0]) and self.__calcValidity(i, j): 			#if the piece is not placed yet
								print "adding piece at", i, j, "  ", self.currentplayer.name
								self.placedPieces[i * (self.gridsize + 1) + j] = [True, self.currentplayer]
								self.__switchPlayer()
								self.validstr = "                   " #Spaces need to exist to create a rect that covers the previous one
							else:
								self.validstr = "Invalid move"
								
			self.display.blit(pieceSurface, (self.boardStartX, self.boardStartY))
			
			for i in range (0, self.gridsize):
				for j in range(0, self.gridsize):
					pygame.draw.rect(self.display, c.BLACK, (self.boxStartX + (i * self.boxDimension), self.boxStartY + (j * self.boxDimension), self.boxDimension, self.boxDimension), 2)
			
			for i in range (0, self.gridsize + 1):
				for j in range (0, self.gridsize + 1):
					if self.placedPieces[i * (self.gridsize + 1) + j][0]:			
						self.placedPieces[i * (self.gridsize + 1) + j][1].placePiece( int(self.boardStartX + (self.boxDimension / 2) + (i * self.boxDimension)), int(self.boardStartY + (self.boxDimension / 2) + (j * self.boxDimension)), self.boxDimension / 3 )
			
		def __getGridSize(self):
			return self.gridsize
		
		def __switchPlayer(self):
			if self.currentplayer == self.player1:
				self.currentplayer = self.player2
			else:
				self.currentplayer = self.player1
		
		def __calcValidity(self, i, j): #returns True for a valid move, False for an invalid move
			if not(self.placedPieces[(i - 1) * (self.gridsize + 1) + j][0]) or self.placedPieces[(i - 1) * (self.gridsize + 1) + j][1] == self.currentplayer: return True
			if not(self.placedPieces[i * (self.gridsize + 1) + j - 1][0]) or self.placedPieces[i * (self.gridsize + 1) + j - 1][1] == self.currentplayer: return True
			if not(self.placedPieces[i * (self.gridsize + 1) + j + 1][0]) or self.placedPieces[i * (self.gridsize + 1) + j + 1][1] == self.currentplayer: return True
			if not(self.placedPieces[(i + 1) * (self.gridsize + 1) + j][0]) or self.placedPieces[(i + 1) * (self.gridsize + 1) + j][1] == self.currentplayer: return True
			return False
		
		def __calcCapture(self, i, j):
			
			
			
	instance = None
	def __init__(self, DISPLAY, gridsize, boxStartY, player1, player2):
		if not Grid.instance:
			Grid.instance = Grid.__Grid(DISPLAY, gridsize, boxStartY, player1, player2)
	
	def drawGrid(self):
		Grid.instance.__drawGrid()
	
	def updateGrid(self, mousePress, mousex, mousey):
		Grid.instance.__updateGrid(mousePress, mousex, mousey)
	
	def getSize(self):
		return Grid.instance.gridsize
	
	def getDimension(self):
		return Grid.instance.boardDimension
	
	def getValidStr(self):
		return Grid.instance.validstr
	
	
	
	
	
	
#	def getGrid():
#		if (theGrid == None):
#			theGrid = Grid(
#
#	def calcValidity():
#		pass
#
#	def calcCapture():
#		pass

