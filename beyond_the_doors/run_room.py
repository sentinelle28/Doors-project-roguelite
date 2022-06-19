import os
import pygame



class Scene():

	def __init__(self, door, normal_door): 
		self.background = pygame.image.load("background.png").convert_alpha()
		self.background_rect = self.background.get_rect(topleft = [0, 0])
		if door == 3:
			self.image_1 = pygame.image.load(normal_door).convert()
			self.image_2 = pygame.image.load(normal_door).convert()
			self.image_3 = pygame.image.load(normal_door).convert()
			self.rect_1 = self.image_1.get_rect(topleft = [350, 100])
			self.rect_2 = self.image_2.get_rect(topleft = [450, 100])
			self.rect_3 = self.image_3.get_rect(topleft = [500, 100])
		if door == 2:
			self.image_1 = pygame.image.load(normal_door).convert()
			self.image_2 = pygame.image.load(normal_door).convert()
			self.rect_1 = self.image_1.get_rect(topleft = [200, 100])
			self.rect_2 = self.image_2.get_rect(topleft = [210, 100])
		else:
			self.image_1 = pygame.image.load(normal_door).convert()
			self.rect_1 = self.image_1.get_rect(topleft = [200, 100])
		


	def  draw(self, screen, door):
		screen.blit(self.background, self.background_rect)
		if door == 3:
			screen.blit(self.image_1, self.rect_1)
			screen.blit(self.image_2, self.rect_2)
			screen.blit(self.image_3, self.rect_3)
		if door == 2:
			screen.blit(self.image_1, self.rect_1)
			screen.blit(self.image_2, self.rect_2)
		elif door == 1:
			screen.blit(self.image_1, self.rect_1)

		


	def Is_mouse_on_door_1(self, animated_door, normal_door):
		
		if self.rect_1.collidepoint(pygame.mouse.get_pos()):
			self.image_1 = pygame.image.load(animated_door).convert()
			self.rect_1 = self.image_1.get_rect(topleft = [200, 100])
			self.on_door_1 = True
		else:
			self.image_1 = pygame.image.load(normal_door).convert()
			self.rect_1 = self.image_1.get_rect(topleft = [200, 100])
			self.on_door_1 = False

	def Is_mouse_on_door_2(self, animated_door, normal_door):
		
		if self.rect_2.collidepoint(pygame.mouse.get_pos()):
			self.image_2 = pygame.image.load(animated_door).convert()
			self.rect_2 = self.image_1.get_rect(topleft = [350, 100])
			self.on_door_2 = True
		else:
			self.image_2 = pygame.image.load(normal_door).convert()
			self.rect_2 = self.image_1.get_rect(topleft = [350, 100])
			self.on_door_2 = False

	def Is_mouse_on_door_3(self, animated_door, normal_door):
		
		if self.rect_3.collidepoint(pygame.mouse.get_pos()):
			self.image_3 = pygame.image.load(animated_door).convert()
			self.rect_3 = self.image_1.get_rect(topleft = [500, 100])
			self.on_door_3 = True
		else:
			self.image_3 = pygame.image.load(normal_door).convert()
			self.rect_3 = self.image_1.get_rect(topleft = [500, 100])
			self.on_door_3 = False