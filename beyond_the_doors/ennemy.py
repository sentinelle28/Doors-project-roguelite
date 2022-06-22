import os
import pygame
import random

class Enemy():
	def __init__(self, image, animated_image ,hp_max, min_damage, max_damage, my_precision, self_damage, position_x, position_y):
		
		self.hp = hp_max
		self.normal_hp = hp_max
		self.min_damage = min_damage
		self.max_damage = max_damage
		self.my_precision = my_precision
		self.self_damage = self_damage
		self.on_it = False
		self.dead = False
		self.position_y = position_y
		self.position_x = position_x
		self.clicked = False
		self.for_one_attack = 0
		self.base_image = pygame.image.load(image).convert_alpha()
		self.base_rect = self.base_image.get_rect(topleft = [self.position_x, self.position_y])

		self.animated_image = pygame.image.load(animated_image).convert_alpha()
		self.animated_rect = self.animated_image.get_rect(topleft = [self.position_x, self.position_y])

		self.image = self.base_image
		self.rect = self.base_rect


	def Draw(self, screen):

		screen.blit(self.image, self.rect)
		
	def Attack(self, hp_player):
		if random.randint(1, self.my_precision) == 1:
			hp_player.hp -= random.randint(self.min_damage, self.max_damage)
		else:
			if self.self_damage:
				self.hp -= random.randint(self.min_damage, self.max_damage)
			pass

	def Reposition(self, X, Y):
		self.position_x = X
		self.position_y = Y


		self.animated_rect = self.animated_image.get_rect(topleft = [self.position_x, self.position_y])
		self.base_rect = self.base_image.get_rect(topleft = [self.position_x, self.position_y])
		self.image = self.base_image
		self.rect = self.base_rect
		
	


	def Is_mouse_on_an_ennemy(self):
		
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			
			self.on_it = True
			
			self.image = self.animated_image
			self.rect = self.animated_rect
			

		else:
			
			self.on_it = False
			
			self.image = self.base_image
			self.rect = self.base_rect
			