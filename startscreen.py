import pygame, sys, playgo
import config as c
import draw
from pygame.locals import *                        
                        
# Helper function
def identify_key():
        text_buffer = ""
        while True: 
                for event in pygame.event.get():
                        if event.type == KEYUP:
                                if event.key == K_ESCAPE:
                                        pygame.quit()
                                        sys.exit()
                                else:
                                        if event.key == K_RETURN:
                                                return text_buffer
                                        elif (len(text_buffer) >= 10):
                                                return text_buffer
                                        str_key = str(chr(event.key))
                                        text_buffer+=str_key
                                        

def showStartScreen(DISPLAY, FPSCLOCK, player1name, player2name):

        # namebox class
        class Namebox:
                
                # attributes
                namebox_count = 0
                def __init__(self, screenx, screeny, scalex, scaley):
                        self.screenx = screenx
                        self.screeny = screeny
                        self.scalex = scalex
                        self.scaley = scaley
                        
                        Namebox.namebox_count += 1
                        
                        input_name = identify_key()
                        name_box = draw.Label(c.STARTSCREENFONT, 18, False, input_name, c.WHITE, self.screenx, self.screeny, self.scalex, self.scaley)
                        name_box.drawRect(DISPLAY, c.BLACK, 20, 5)
                        DISPLAY.blit(name_box.labelText, name_box.labelRect)
                        self.name = input_name
                        
	mousex = 0
	mousey = 0

	
	#Adding text labels to the screen
	titleLabel = draw.Label(c.STARTSCREENFONT, 40, True, "Start Game", c.BLACK, 0.5, 0.1)
	gridSizeLabel = draw.Label(c.STARTSCREENFONT, 30, False, "Grid Size", c.BLACK, 0.5, 0.2)
	gameModeLabel = draw.Label(c.STARTSCREENFONT, 30, False, "Game Mode", c.BLACK, 0.5, 0.4)
	nameLabel = draw.Label(c.STARTSCREENFONT, 30, False, "Name", c.BLACK, 0.5, 0.6)


	
	#Displaying non-changing parts of the screen
	DISPLAY.fill(c.TAN)
	DISPLAY.blit(titleLabel.labelText, titleLabel.labelRect)
	DISPLAY.blit(gridSizeLabel.labelText, gridSizeLabel.labelRect)
	DISPLAY.blit(gameModeLabel.labelText, gameModeLabel.labelRect)
	DISPLAY.blit(nameLabel.labelText, nameLabel.labelRect)
	
	
	#Adding options buttons
	gridSize9Button = draw.Label(c.STARTSCREENFONT, 25, False, "  9 x 9  ", c.BLACK, 0.5,0.29, -150)
	gridSize9Button.drawRect(DISPLAY,c.WHITE,20,5)

	gridSize11Button = draw.Label(c.STARTSCREENFONT, 25, False, " 11 x 11 ", c.BLACK, 0.5,0.29)
	gridSize11Button.drawRect(DISPLAY,c.WHITE,20,5)

	gridSize19Button = draw.Label(c.STARTSCREENFONT, 25, False, " 19 x 19 ", c.BLACK, 0.5,0.29, 150)
	gridSize19Button.drawRect(DISPLAY,c.WHITE,20,5)

	mode2PlayerButton = draw.Label(c.STARTSCREENFONT, 25, False, " 2 Player ", c.BLACK, 0.5,0.49,-75)
	mode2PlayerButton.drawRect(DISPLAY,c.WHITE,20,5)

	modeAIButton = draw.Label(c.STARTSCREENFONT, 25, False, "  vs. AI  ", c.BLACK, 0.5,0.49,75)
	modeAIButton.drawRect(DISPLAY,c.DRKGRAY,20,5)
	
	player1Button = draw.Label(c.STARTSCREENFONT, 25, False, player1name, c.BLACK, 0.5,0.69,-75)
	player1Button.drawRect(DISPLAY, c.WHITE, 20, 5)

	player2Button = draw.Label(c.STARTSCREENFONT, 25, False, player2name, c.BLACK, 0.5,0.69,75)
	player2Button.drawRect(DISPLAY, c.WHITE, 20, 5)

	startButton = draw.Label(c.STARTSCREENFONT, 25, False, " START ", c.BLACK, 0.5,0.9)
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
			if gridSize9Button.labelRect.collidepoint(mousex, mousey):
				gridSize9Button.drawRect(DISPLAY, c.LTGRAY)
				gridSize11Button.drawRect(DISPLAY, c.WHITE)
				gridSize19Button.drawRect(DISPLAY, c.WHITE)
				grid = 9
			if gridSize11Button.labelRect.collidepoint(mousex, mousey):
				gridSize9Button.drawRect(DISPLAY, c.WHITE)
				gridSize11Button.drawRect(DISPLAY, c.LTGRAY)
				gridSize19Button.drawRect(DISPLAY, c.WHITE)
				grid = 11
			if gridSize19Button.labelRect.collidepoint(mousex, mousey):
				gridSize9Button.drawRect(DISPLAY, c.WHITE)
				gridSize11Button.drawRect(DISPLAY, c.WHITE)
				gridSize19Button.drawRect(DISPLAY, c.LTGRAY)
				grid = 19
							
			if player1Button.labelRect.collidepoint(mousex, mousey):
				namebox1 = Namebox(0.5,0.69,-75, 25)
				player1name = namebox1.name
                                
			if player2Button.labelRect.collidepoint(mousex, mousey):
				namebox1 = Namebox(0.5,0.69,-75, 25)
				player1name = namebox1.name
				namebox2 = Namebox(0.5,0.69, 75, 25)
				player2name = namebox2.name

			elif startButton.labelRect.collidepoint(mousex, mousey):
				if grid:
					cont = False
				else:
					errorMessageText = "Choose grid size"
					errorMessage = draw.Label(c.STARTSCREENFONT, 20, False, errorMessageText, c.RED, 0.5, 0.85)
					DISPLAY.blit(errorMessage.labelText, errorMessage.labelRect)
		
		DISPLAY.blit(gridSize9Button.labelText, gridSize9Button.labelRect)
		DISPLAY.blit(gridSize11Button.labelText, gridSize11Button.labelRect)
		DISPLAY.blit(gridSize19Button.labelText, gridSize19Button.labelRect)
		
		pygame.display.update()
		
		FPSCLOCK.tick(c.FPS)
	
	return grid, player1name, player2name
	
