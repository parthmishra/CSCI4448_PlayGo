import pygame, sys, playgo
import config as c
import draw
from pygame.locals import *

def displayGame(gridsize, player1, player2, DISPLAY, FPSCLOCK):
	score_file = open("scores.txt", 'r+')
	words = score_file.read()
	DISPLAY.fill(c.BLACK)

	if player1.resigned:
		winner = player2.name
	else:
		winner = player1.name

	
	WinnerLabel = draw.Label(c.STARTSCREENFONT, 45, False,  winner + " has won", c.GREEN, 0.5, 0.6, 0, -150)
	DISPLAY.blit(WinnerLabel.labelText, WinnerLabel.labelRect)
	
	while True:
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
		pygame.display.update()
