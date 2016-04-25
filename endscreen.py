import pygame, sys, playgo
import config as c
import draw
from pygame.locals import *

def displayGame(gridsize, player1, player2, DISPLAY, FPSCLOCK):
        score_file = open("scores.txt", 'r+')
        words = score_file.read()
        

        if player1.resigned:
                winner = player2.name
        else:
                winner = player1.name

	WinnerLabel = draw.Label(c.STARTSCREENFONT, 45, False,  winner + " has won", c.GREEN, 0.5, 0.6, 0, -150)
	DISPLAY.blit(WinnerLabel.labelText, WinnerLabel.labelRect)
	
        pygame.display.update()
