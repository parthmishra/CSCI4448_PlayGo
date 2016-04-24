import pygame, sys, playgo
import config as c
from pygame.locals import *

class Label:

	def __init__(self, font, fontSize, underline, text, textColor, widthMod, heightMod, dx=0, dy=0):
		self.font = font
		self.fontSize = fontSize
		self.underline = underline
		self.text = text
		self.textColor = textColor
		self.labelObj = pygame.font.SysFont(font, fontSize)
		self.labelObj.set_underline(underline)
		self.labelText = self.labelObj.render(text, True, textColor)
		self.labelRect = self.labelText.get_rect()
		self.labelRect.center = (c.WINWIDTH * widthMod + dx, c.WINHEIGHT * heightMod + dy)

	def drawRect(self, surface, rectColor, inflateX=0, inflateY=0, width=0):
		if inflateX or inflateY != 0:
			self.labelRect.inflate(inflateX, inflateY)
		self.labelRect = pygame.draw.rect(surface, rectColor, self.labelRect, width)

def showStartScreen(DISPLAY, FPSCLOCK):
	mousex = 0
	mousey = 0
	
	#Adding text labels to the screen
	titleLabel = Label(c.STARTSCREENFONT, 40, True, "Start Game", c.BLACK, 0.5, 0.1)
	gridSizeLabel = Label(c.STARTSCREENFONT, 30, True, "Grid Size", c.BLACK, 0.5, 0.2)
	gameModeLabel = Label(c.STARTSCREENFONT, 30, False, "Game Mode", c.BLACK, 0.5, 0.4)
	nameLabel = Label(c.STARTSCREENFONT, 30, False, "Name", c.BLACK, 0.5, 0.6)


	
	#Displaying non-changing parts of the screen
	DISPLAY.fill(c.TAN)
	DISPLAY.blit(titleLabel.labelText, titleLabel.labelRect)
	DISPLAY.blit(gridSizeLabel.labelText, gridSizeLabel.labelRect)
	DISPLAY.blit(gameModeLabel.labelText, gameModeLabel.labelRect)
	DISPLAY.blit(nameLabel.labelText, nameLabel.labelRect)
	
	
	#Adding options buttons
	gridSize90Button = Label(c.STARTSCREENFONT, 25, False, "9 x 9", c.BLACK, 0.5,0.29, -150)
	gridSize90Button.drawRect(DISPLAY,c.WHITE,20,5)

	gridSize110Button = Label(c.STARTSCREENFONT, 25, False, "11 x 11", c.BLACK, 0.5,0.29)
	gridSize110Button.drawRect(DISPLAY,c.WHITE,20,5)

	gridSize190Button = Label(c.STARTSCREENFONT, 25, False, "19 x 19", c.BLACK, 0.5,0.29, 150)
	gridSize190Button.drawRect(DISPLAY,c.WHITE,20,5)

	mode2PlayerButton = Label(c.STARTSCREENFONT, 25, False, "2 Player", c.BLACK, 0.5,0.49,-75)
	mode2PlayerButton.drawRect(DISPLAY,c.WHITE,20,5)

	modeAIButton = Label(c.STARTSCREENFONT, 25, False, " vs. AI", c.BLACK, 0.5,0.49,75)
	modeAIButton.drawRect(DISPLAY,c.DRKGRAY,20,5)
	
	player1Button = Label(c.STARTSCREENFONT, 25, False, " Player 1 ", c.BLACK, 0.5,0.69,-75)
	player1Button.drawRect(DISPLAY, c.WHITE, 20, 5)

	player2Button = Label(c.STARTSCREENFONT, 25, False, " Player 2 ", c.BLACK, 0.5,0.69,75)
	player2Button.drawRect(DISPLAY, c.WHITE, 20, 5)

	startButton = Label(c.STARTSCREENFONT, 25, False, " START ", c.BLACK, 0.5,0.9)
	startButton.drawRect(DISPLAY, c.GREEN, 20, 5)

	DISPLAY.blit(mode2PlayerButton.labelText, mode2PlayerButton.labelRect)
	DISPLAY.blit(modeAIButton.labelText, modeAIButton.labelRect)
	DISPLAY.blit(player1Button.labelText, player1Button.labelRect)
	DISPLAY.blit(player2Button.labelText, player2Button.labelRect)
	DISPLAY.blit(startButton.labelText, startButton.labelRect)
	
	cont = True
	grid = 0
	
	while cont:
		mousePress = False
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP:
				if event.button == 1:
					mousex, mousey = event.pos
					mousePress = True
			elif event.type == KEYUP:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
		
		
		if mousePress:
			if gridSize90Button.labelRect.collidepoint(mousex, mousey):
				gridSize90Button.drawRect(DISPLAY, c.LTGRAY)
				gridSize110Button.drawRect(DISPLAY, c.WHITE)
				gridSize190Button.drawRect(DISPLAY, c.WHITE)
				gride = 9
			if gridSize110Button.labelRect.collidepoint(mousex, mousey):
				gridSize90Button.drawRect(DISPLAY, c.WHITE)
				gridSize110Button.drawRect(DISPLAY, c.LTGRAY)
				gridSize190Button.drawRect(DISPLAY, c.WHITE)
				grid = 11
			if gridSize190Button.labelRect.collidepoint(mousex, mousey):
				gridSize90Button.drawRect(DISPLAY, c.WHITE)
				gridSize110Button.drawRect(DISPLAY, c.WHITE)
				gridSize190Button.drawRect(DISPLAY, c.LTGRAY)
				grid = 19
			elif startButton.labelRect.collidepoint(mousex, mousey):
				cont = False
			
		DISPLAY.blit(gridSize90Button.labelText, gridSize90Button.labelRect)
		DISPLAY.blit(gridSize110Button.labelText, gridSize110Button.labelRect)
		DISPLAY.blit(gridSize190Button.labelText, gridSize190Button.labelRect)
		
		pygame.display.update()
		
		FPSCLOCK.tick(c.FPS)
	
	DISPLAY.fill(c.TAN)
	return grid
	