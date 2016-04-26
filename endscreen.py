import pygame, sys, playgo
import config as c
import draw
from pygame.locals import *

def displayGame(gridsize, player1, player2, DISPLAY, FPSCLOCK):
	score_file = open("scores.txt", 'r+')
	words = score_file.read()
	DISPLAY.fill(c.TAN)

	if player1.resigned:
		winner = player2.name
	else:
		winner = player1.name

	
	gameOverLabel = draw.Label(c.STARTSCREENFONT, 45, False, " Game Over ", c.BLACK, 0.5, 0.3)
	winnerLabel = draw.Label(c.STARTSCREENFONT, 45, False,  winner + "wins!", c.BLACK, 0.5, .5, 0,)
	
	newGameLabel = draw.Label(c.STARTSCREENFONT, 30, False, " New Game ", c.BLACK, 0.5, .8, -150, 0)
	newGameLabel.drawRect(DISPLAY, c.WHITE, 100, 200, 0)
	newGameLabel.drawRect(DISPLAY, c.BLACK, 101, 201, 1)
	
	quitLabel = draw.Label(c.STARTSCREENFONT, 30, False, "     Quit     ", c.BLACK, 0.5, .8, 150, 0)
	quitLabel.drawRect(DISPLAY, c.WHITE, 100, 200, 0)
	quitLabel.drawRect(DISPLAY, c.BLACK, 101, 201, 1)
	
	DISPLAY.blit(gameOverLabel.labelText, gameOverLabel.labelRect)
	DISPLAY.blit(winnerLabel.labelText, winnerLabel.labelRect)
	DISPLAY.blit(newGameLabel.labelText, newGameLabel.labelRect)
	DISPLAY.blit(quitLabel.labelText, quitLabel.labelRect)
	
	newGame = False
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
					
		if mousePress:
			if newGameLabel.labelRect.collidepoint(mousex, mousey):
				newGame = True
				cont = False
			elif quitLabel.labelRect.collidepoint(mousex, mousey): 
				newGame = False
				cont = False
		
		pygame.display.update()

	return newGame
