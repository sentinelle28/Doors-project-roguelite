import pygame
import os
import random

class Starting_door():
	def __init__(self):
		self.image_1 = pygame.image.load("starting_door.png")
		
		self.image_2 = pygame.image.load("animated_starting_door.png")
		self.image = self.image_1
		self.rect = self.image.get_rect(topleft = [200, 200])
		self.clicked = True


	def Is_mouse_on_the_starting_door(self):
		self.on_it  = False

		if self.rect.collidepoint(pygame.mouse.get_pos()):
			self.image = self.image_2
			self.rect = self.image.get_rect(topleft = [200, 200])
			self.on_it = True




		else:


			self.image = self.image_1
			self.rect = self.image.get_rect(topleft = [200, 200])
			
			


		


	def  draw(self, screen):
		screen.blit(self.image, self.rect)

		