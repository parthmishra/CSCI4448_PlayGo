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
		
		cont = gameboard.updateGrid(mousePress, mousex, mousey)
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
			
			p1Label = draw.Label(c.STARTSCREENFONT, 30, False, self.player1.name, c.WHITE, 0, 0, 75, 20)
			p1Label.drawRect(self.display, c.BLACK, 50, 50)
			p2Label = draw.Label(c.STARTSCREENFONT, 30, False, self.player2.name, c.BLACK, 1, 0, -75, 20)
			p2Label.drawRect(self.display, c.BLACK, 50, 50, 1)
			
			for i in range (0, self.gridsize + 1):
				for j in range (0, self.gridsize + 1):
					self.placedPieces.append([False, self.currentplayer])
			
			self.display.blit(p1Label.labelText, p1Label.labelRect)
			self.display.blit(p2Label.labelText, p2Label.labelRect)
		
		def __updateGrid(self, mousePress, mousex, mousey):
			keepPlaying = True
			
			pieceSurface = pygame.Surface((self.boardDimension, self.boardDimension))
			pieceSurface.fill(c.TAN)
			
			resignButton = draw.Label(c.STARTSCREENFONT, 30, False, " RESIGN ", c.BLACK, 1, 1, -75, -40)
			resignButton.drawRect(self.display, c.BLACK, 0, 0, 1)
			
			passButton = draw.Label(c.STARTSCREENFONT, 30, False, " PASS ", c.BLACK, 1, 1, -75, -80)
			passButton.drawRect(self.display, c.BLACK, 0, 0, 1)
							
			self.display.blit(passButton.labelText, passButton.labelRect)
			self.display.blit(resignButton.labelText, resignButton.labelRect)
			
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
				if passButton.labelRect.collidepoint(mousex, mousey): 
					keepPlaying = self.__pass()	
				if resignButton.labelRect.collidepoint(mousex, mousey):
					keepPlaying = self.__resign()
				else:	
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
			
			p1passed = draw.Label(c.STARTSCREENFONT, 15, False, "Passed", c.BLACK, 0, 0, 75, 50)
			p2passed = draw.Label(c.STARTSCREENFONT, 15, False, "Passed", c.BLACK, 1, 0, -75, 50)
			if self.player1.passed:
				p1passed.drawRect(self.display, c.WHITE, 20, 20)
				self.display.blit(p1passed.labelText, p1passed.labelRect)
			else:
				p1passed.drawRect(self.display, c.WHITE, 20, 20)
			
			if self.player2.passed:
				p2passed.drawRect(self.display, c.WHITE, 20, 20)
				self.display.blit(p2passed.labelText, p2passed.labelRect)
			else:
				p2passed.drawRect(self.display, c.WHITE, 20, 20)
			
			
			return keepPlaying
			
		def __getGridSize(self):
			return self.gridsize
		
		def __switchPlayer(self):
			if self.currentplayer == self.player1:
				self.currentplayer = self.player2
				self.currentplayer.passed = False
			else:
				self.currentplayer = self.player1
				self.currentplayer.passed = False
		
		def __calcValidity(self, i, j): #returns True for a valid move, False for an invalid move
			self.placedPieces[i * (self.gridsize + 1) + j] = [True, self.currentplayer]
			self.__calcCapture(i, j)
			self.placedPieces[i * (self.gridsize + 1) + j] = [False, self.currentplayer]
			return self.__calcLiberties(i, j)			
		
		def __calcCapture(self, i, j):
			if not((i - 1) < 0):
				if self.placedPieces[(i - 1) * (self.gridsize + 1) + j][0] and not(self.placedPieces[(i - 1) * (self.gridsize + 1) + j][1] == self.currentplayer):
					if not(self.__calcLiberties((i - 1), j)):
						self.placedPieces[(i - 1) * (self.gridsize + 1) + j] = [False, self.currentplayer]
			if not((j - 1) < 0):
				if self.placedPieces[i * (self.gridsize + 1) + (j - 1)][0] and not(self.placedPieces[i * (self.gridsize + 1) + (j - 1)][1] == self.currentplayer):
					if not(self.__calcLiberties(i, (j - 1))):
						self.placedPieces[i * (self.gridsize + 1) + (j - 1)] = [False, self.currentplayer]
			if not((j + 1) > self.gridsize):
				if self.placedPieces[i * (self.gridsize + 1) + (j + 1)][0] and not(self.placedPieces[i * (self.gridsize + 1) + (j + 1)][1] == self.currentplayer):
					if not(self.__calcLiberties(i, (j + 1))):
						self.placedPieces[i * (self.gridsize + 1) + (j + 1)] = [False, self.currentplayer]
			if not((i + 1) > self.gridsize):
				if self.placedPieces[(i + 1) * (self.gridsize + 1) + j][0] and not(self.placedPieces[(i + 1) * (self.gridsize + 1) + j][1] == self.currentplayer):
					if not(self.__calcLiberties((i + 1), j)):
						self.placedPieces[(i + 1) * (self.gridsize + 1) + j] = [False, self.currentplayer]
			
		def __calcLiberties(self, i, j): #returns True for free or sympathetic liberties, False for filled liberties
			print "Check liberties:", i, j
			numlibs = 0
			if not((i - 1) < 0):
				print "Checking", i - 1, j
				if self.placedPieces[(i - 1) * (self.gridsize + 1) + j][0]:
					if self.placedPieces[(i - 1) * (self.gridsize + 1) + j][1] == self.placedPieces[i * (self.gridsize + 1) + j][1]:
						print "lib at: ", i - 1, j
						numlibs += 1
				else:
					print "lib at: ", i - 1, j
					numlibs += 1
			if not((j - 1) < 0):
				print "Checking", i, j - 1
				if self.placedPieces[i * (self.gridsize + 1) + j - 1][0]:
					if self.placedPieces[i * (self.gridsize + 1) + j - 1][1] == self.placedPieces[i * (self.gridsize + 1) + j][1]:
						print "lib at: ", i, j - 1
						numlibs += 1
				else:
					print "lib at: ", i, j - 1
					numlibs += 1
			if not((j + 1) > self.gridsize):
				print "Checking", i, j + 1
				if self.placedPieces[i * (self.gridsize + 1) + j + 1][0]:
					if self.placedPieces[i * (self.gridsize + 1) + j + 1][1] == self.placedPieces[i * (self.gridsize + 1) + j][1]:
						print "lib at: ", i, j + 1
						numlibs += 1
				else:
					print "lib at: ", i, j + 1
					numlibs += 1
			if not((i + 1) > self.gridsize):
				print "Checking", i + 1, j
				if self.placedPieces[(i + 1) * (self.gridsize + 1) + j][0]:
					if self.placedPieces[(i + 1) * (self.gridsize + 1) + j][1] == self.placedPieces[i * (self.gridsize + 1) + j][1]:
						print "lib at: ", i + 1, j
						numlibs += 1
				else:
					print "lib at: ", i + 1, j
					numlibs += 1
			print i, j, ":", numlibs
			if numlibs:
				return True
			else:
				return False
			
		def __pass(self):
			self.currentplayer.passed = True
			print self.currentplayer.name, "passed"
			if self.player1.passed and self.player2.passed: #if both players have passed
				return False
			self.__switchPlayer()
			return True
			
		def __resign(self):
			self.currentplayer.resigned = True
			print self.currentplayer.name, "resigned"
			return False


	instance = None
	def __init__(self, DISPLAY, gridsize, boxStartY, player1, player2):
		if not Grid.instance:
			Grid.instance = Grid.__Grid(DISPLAY, gridsize, boxStartY, player1, player2)
	
	def drawGrid(self):
		Grid.instance.__drawGrid()
	
	def updateGrid(self, mousePress, mousex, mousey):
		return Grid.instance.__updateGrid(mousePress, mousex, mousey)
	
	def getSize(self):
		return Grid.instance.gridsize
	
	def getDimension(self):
		return Grid.instance.boardDimension
	
	def getValidStr(self):
		return Grid.instance.validstr

