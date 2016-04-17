import pygame, sys
from pygame.locals import *

#COLOR TABLE 	R    G    B
WHITE		= (255,	255, 255)
BLACK 		= (  0,   0,   0)
DRKGRAY		= (100, 100, 100)
LTGRAY		= (175, 175, 175)
TAN			= (224,	176,  54)
GREEN		= (  0, 255,   0)

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
	
	#Adding text labels to the screen
	titleFontObj = pygame.font.SysFont(STARTSCREENFONT, 40)
	titleFontObj.set_underline(True)
	titleText = titleFontObj.render("Start Game", True, BLACK)
	titleTextRect = titleText.get_rect()
	titleTextRect.center = (WINWIDTH * 0.5, WINHEIGHT * 0.1)
	
	gridSizeTextObj = pygame.font.SysFont(STARTSCREENFONT, 30)
	gridSizeText = gridSizeTextObj.render("Grid Size", True, BLACK)
	gridSizeTextRect = gridSizeText.get_rect()
	gridSizeTextRect.center = (WINWIDTH * 0.5, WINHEIGHT * 0.2)
	
	gameModeTextObj = pygame.font.SysFont(STARTSCREENFONT, 30)
	gameModeText = gameModeTextObj.render("Game Mode", True, BLACK)
	gameModeTextRect = gameModeText.get_rect()
	gameModeTextRect.center = (WINWIDTH * 0.5, WINHEIGHT * 0.4)
	
	nameTextObj = pygame.font.SysFont(STARTSCREENFONT, 30)
	nameText = nameTextObj.render("Name", True, BLACK)
	nameTextRect = nameText.get_rect()
	nameTextRect.center = (WINWIDTH * 0.5, WINHEIGHT * 0.6)
	
	
	#Displaying non-changing parts of the screen
	DISPLAY.fill(TAN)
	DISPLAY.blit(titleText, titleTextRect)
	DISPLAY.blit(gridSizeText, gridSizeTextRect)
	DISPLAY.blit(gameModeText, gameModeTextRect)
	DISPLAY.blit(nameText, nameTextRect)
	
	
	#Adding options buttons
	gridSize9OptButtonObj = pygame.font.SysFont(STARTSCREENFONT, 25)
	gridSize9OptButton = gridSize9OptButtonObj.render(" 9 X 9 ", True, BLACK)
	gridSize9OptButtonRect = gridSize9OptButton.get_rect()
	gridSize9OptButtonRect.center = (WINWIDTH * 0.5 - 150, WINHEIGHT * 0.29)
	gridSize9Rect = pygame.draw.rect(DISPLAY, WHITE, gridSize9OptButtonRect.inflate(20, 5), 0)
	
	gridSize11OptButtonObj = pygame.font.SysFont(STARTSCREENFONT, 25)
	gridSize11OptButton = gridSize11OptButtonObj.render("11 X 11", True, BLACK)
	gridSize11OptButtonRect = gridSize11OptButton.get_rect()
	gridSize11OptButtonRect.center = (WINWIDTH * 0.5, WINHEIGHT * 0.29)
	gridSize11Rect = pygame.draw.rect(DISPLAY, WHITE, gridSize11OptButtonRect.inflate(20, 5), 0)
	
	gridSize19OptButtonObj = pygame.font.SysFont(STARTSCREENFONT, 25)
	gridSize19OptButton = gridSize19OptButtonObj.render("19 X 19", True, BLACK)
	gridSize19OptButtonRect = gridSize19OptButton.get_rect()
	gridSize19OptButtonRect.center = (WINWIDTH * 0.5 + 150, WINHEIGHT * 0.29)
	gridSize19Rect = pygame.draw.rect(DISPLAY, WHITE, gridSize19OptButtonRect.inflate(20, 5), 0)
	
	mode2PButtonObj = pygame.font.SysFont(STARTSCREENFONT, 25)
	mode2PButton = mode2PButtonObj.render("2 Player", True, BLACK)
	mode2PButtonRect = mode2PButton.get_rect()
	mode2PButtonRect.center = (WINWIDTH * 0.5 - 75, WINHEIGHT * 0.49)
	mode2PRect = pygame.draw.rect(DISPLAY, WHITE, mode2PButtonRect.inflate(20, 5), 0)
	
	modeAIButtonObj = pygame.font.SysFont(STARTSCREENFONT, 25)
	modeAIButton = modeAIButtonObj.render("  vs. AI  ", True, BLACK)
	modeAIButtonRect = modeAIButton.get_rect()
	modeAIButtonRect.center = (WINWIDTH * 0.5 + 75, WINHEIGHT * 0.49)
	modeAIRect = pygame.draw.rect(DISPLAY, DRKGRAY, modeAIButtonRect.inflate(20, 5), 0)
	
	player1ButtonObj = pygame.font.SysFont(STARTSCREENFONT, 25)
	player1Button = player1ButtonObj.render("  Player 1  ", True, BLACK)
	player1ButtonRect = player1Button.get_rect()
	player1ButtonRect.center = (WINWIDTH * 0.5 - 75, WINHEIGHT * 0.69)
	player1Rect = pygame.draw.rect(DISPLAY, WHITE, player1ButtonRect.inflate(20, 5), 0)
	
	player2ButtonObj = pygame.font.SysFont(STARTSCREENFONT, 25)
	player2Button = player2ButtonObj.render("      AI       ", True, BLACK)
	player2ButtonRect = player2Button.get_rect()
	player2ButtonRect.center = (WINWIDTH * 0.5 + 75, WINHEIGHT * 0.69)
	player2Rect = pygame.draw.rect(DISPLAY, WHITE, player2ButtonRect.inflate(20, 5), 0)
	
	startButtonObj = pygame.font.SysFont(STARTSCREENFONT, 25)
	startButton = startButtonObj.render("  START  ", True, BLACK)
	startButtonRect = startButton.get_rect()
	startButtonRect.center = (WINWIDTH * 0.5, WINHEIGHT * 0.9)
	startRect = pygame.draw.rect(DISPLAY, GREEN, startButtonRect.inflate(20, 5), 0)
	
	DISPLAY.blit(mode2PButton, mode2PButtonRect)
	DISPLAY.blit(modeAIButton, modeAIButtonRect)
	DISPLAY.blit(player1Button, player1ButtonRect)
	DISPLAY.blit(player2Button, player2ButtonRect)
	DISPLAY.blit(startButton, startButtonRect)
	
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
			if gridSize9OptButtonRect.collidepoint(mousex, mousey):
				gridSize9Rect = pygame.draw.rect(DISPLAY, LTGRAY, gridSize9Rect, 0)
				gridSize11Rect = pygame.draw.rect(DISPLAY, WHITE, gridSize11Rect, 0)
				gridSize19Rect = pygame.draw.rect(DISPLAY, WHITE, gridSize19Rect, 0)
				grid = 9
			if gridSize11OptButtonRect.collidepoint(mousex, mousey):
				gridSize9Rect = pygame.draw.rect(DISPLAY, WHITE, gridSize9Rect, 0)
				gridSize11Rect = pygame.draw.rect(DISPLAY, LTGRAY, gridSize11Rect, 0)
				gridSize19Rect = pygame.draw.rect(DISPLAY, WHITE, gridSize19Rect, 0)
				grid = 11
			if gridSize19OptButtonRect.collidepoint(mousex, mousey):
				gridSize9Rect = pygame.draw.rect(DISPLAY, WHITE, gridSize9Rect, 0)
				gridSize11Rect = pygame.draw.rect(DISPLAY, WHITE, gridSize11Rect, 0)
				gridSize19Rect = pygame.draw.rect(DISPLAY, LTGRAY, gridSize19Rect, 0)
				grid = 19
			elif startButtonRect.collidepoint(mousex, mousey):
				cont = False
			
		DISPLAY.blit(gridSize9OptButton, gridSize9OptButtonRect)
		DISPLAY.blit(gridSize11OptButton, gridSize11OptButtonRect)
		DISPLAY.blit(gridSize19OptButton, gridSize19OptButtonRect)
		
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

