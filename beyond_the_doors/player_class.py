import os
import pygame
import random

class Player:
	def __init__(self,hp_max):
		self.image = pygame.image.load("player.png").convert_alpha()
		self.rect = self.image.get_rect(topleft = [100,200])
		self.hp = hp_max
		self.precision = 2
		self.self_damage = False
		self.bonus_damage = 0
		self.is_on_fight = False
		self.number_max_of_weapon = 3
		self.min_damage = 1
		self.max_damage = 7
		self.attack_value = 0
		self.weapon_equipped = [False, False, False]
		

		

	def Attack(self, hp_monster):
		
		if random.randint(1, self.precision) == 1:
			self.attack_value = 0
			self.attack_value = random.randint(self.min_damage, self.max_damage) + self.bonus_damage 
			hp_monster.hp -= self.attack_value                                                                  #you need to put self because attack can change
		else:
			self.attack_value = 0
			if self.self_damage:
				self.hp -= random.randint(self.min_damage, self.max_damage)	
			


	def Draw(self, screen):

		screen.blit(self.image, self.rect)








class Weapon:
	def __init__(self, image, animated_image, min_damage, max_damage, position_x, position_y):
		self.image = pygame.image.load(image).convert()
		self.rect = self.image.get_rect(topleft = [200, 100])
		self.clicked = False
		self.position_y = position_y
		self.position_x = position_x
		self.min_damage = min_damage
		self.max_damage = max_damage
		self.base_image = pygame.image.load(image).convert_alpha()
		self.base_rect = self.base_image.get_rect(topleft = [self.position_x, self.position_y])

		self.animated_image = pygame.image.load(animated_image).convert_alpha()
		self.animated_rect = self.animated_image.get_rect(topleft = [self.position_x, self.position_y])
		self.image = self.base_image
		self.rect = self.base_rect

	
	def Is_mouse_on_the_weapon(self, clicked_question):
		

		if self.rect.collidepoint(pygame.mouse.get_pos()) or clicked_question == True :
			
			self.on_it = True
			
			self.image = self.animated_image
			self.rect = self.animated_rect
			

		else:
			
			self.on_it = False
			
			self.image = self.base_image
			self.rect = self.base_rect

			
	def Draw(self, screen):

		screen.blit(self.image, self.rect)


		


	
		