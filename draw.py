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
