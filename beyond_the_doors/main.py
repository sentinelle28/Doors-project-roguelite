import os
import pygame
import random
from starting_screen import *
from run_room import *
from ennemy import *
from player_class import *


class Game():
	def __init__(self,screen):
		self.screen = screen
		self.running = True
		self.clock = pygame.time.Clock()
		self.starting_door = Starting_door()
		self.normal_room = Scene(3, "door_frame_1.png")
		self.player = Player(30)
		self.new_room = 1
		self.number_of_monster_done = False
		self.number_of_monster = 0
		
		self.number_of_monster_kill = 0
		
		self.monster_list = [Enemy("bat_eyed_monster.png","one_eyed_bat_selected.png", 15, 0, 10, 3, False, 200, 200), 
		Enemy("bat_eyed_monster.png","one_eyed_bat_selected.png", 15, 0, 10, 3, False, 100, 100)



		]
		self.spawn_weapon_chance = 200
		self.weapon = [Weapon("rock.png", "rock_selected.png", 1, 7, 50, 100)]
		
		self.player.weapon_equipped[0] = self.weapon[0]

		self.monster_spawned = []
		

	def handling_evenement(self):

		
			
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
		




			if event.type == pygame.MOUSEBUTTONDOWN:                   
				if self.starting_door.on_it:
					if self.starting_door.clicked == True:                    #starting door procedure
						self.starting_door.clicked = False



				if self.normal_room.on_door_1 or self.normal_room.on_door_2 or self.normal_room.on_door_3: #generation procedure
					if self.player.is_on_fight != True:

						self.new_room = random.randint(1, 2)

						if self.new_room == 1:
							self.player.is_on_fight = False

						elif self.new_room == 2:
							self.player.is_on_fight = True
						
					else:
						
						if self.player.weapon_equipped[0].on_it:                                                           #check if the player is on the weapon
							self.player.weapon_equipped[0].clicked = True
						if self.number_of_monster_done:

							
							for attack in self.monster_spawned:
								print("number of kill:", self.number_of_monster_kill, "/", self.number_of_monster)
								print(f"pos X{attack - 1}: {self.monster_spawned[attack - 1].position_x}    pos Y{attack - 1}: {self.monster_spawned[attack - 1].position_y}")
								if self.monster_spawned[attack - 1].on_it and self.monster_spawned[attack].dead == False:
									self.monster_spawned[attack - 1].on_it.clicked = True
									self.monster_spawned[attack - 1].for_one_attack = 1
								else:
									self.monster_spawned[attack - 1].on_it.clicked = False


						

						
					


	def run(self):
		while self.running:
			self.handling_evenement()
			self.update()
			self.display()
			self.clock.tick(60)
			pass

	def update(self):

		self.player.weapon_equipped[0].Is_mouse_on_the_weapon(self.player.weapon_equipped[0].clicked)          #call is on fonction here so the detection fontion
		self.starting_door.Is_mouse_on_the_starting_door()                 


		if self.player.is_on_fight == False:
			self.normal_room.Is_mouse_on_door_1("door_frame_2.png", "door_frame_1.png")
			self.normal_room.Is_mouse_on_door_2("door_frame_2.png", "door_frame_1.png")
			self.normal_room.Is_mouse_on_door_3("door_frame_2.png", "door_frame_1.png")
			pass
		else:
			if self.number_of_monster_done == False:                      #checking if it's already done
				self.number_of_monster = random.randint(1, 3)
				
				self.number_of_monster_kill = 0
				
				self.monster_spawned.clear() 
				for monster in range(1, self.number_of_monster):
					self.monster_spawned.append("not finished")
					self.monster_spawned[monster - 1] = self.monster_list[random.randint(0, 1)]
					self.monster_spawned[monster - 1].Reposition(200, 200, screen)                              #to put the image at the correct place
					self.monster_spawned[monster - 1].dead = False
					self.monster_spawned[monster - 1].hp = self.monster_spawned[monster - 1].normal_hp
					

				
				
				self.number_of_monster_done = True
				
			else:
				if self.number_of_monster_kill == self.number_of_monster:
					self.player.is_on_fight = False
					self.number_of_monster_done = False




					self.number_of_monster = 0
					self.player.weapon_equipped[0].clicked = False
					self.player.weapon_equipped[0].Is_mouse_on_the_weapon(self.player.weapon_equipped[0].clicked)
					self.spawn_weapon_chance = random.randint(1, 2)
					if self.spawn_weapon_chance == 1:
						pass


					
				for number_of_monster_here in self.monster_spawned:
					self.monster_spawned[number_of_monster_here - 1].Is_mouse_on_an_ennemy()
					if self.monster_spawned[number_of_monster_here - 1].clicked and self.monster_spawned[number_of_monster_here - 1].for_one_attack and self.player.weapon_equipped[0].clicked:
						self.player.Attack(self.monster_spawned[number_of_monster_here - 1])
						self.player.weapon_equipped[0].clicked = False
						self.monster_spawned[number_of_monster_here - 1].clicked = False
						self.monster_spawned[number_of_monster_here - 1].on_it = False
						self.monster_spawned[number_of_monster_here - 1].for_one_attack = 0
						if self.monster_spawned[number_of_monster_here - 1].hp <= 0 :
							self.number_of_monster_kill += 1
							self.monster_spawned[number_of_monster_here - 1].dead = True


				

				
				
					
			

		

	def display(self):
		screen.fill((0, 0, 0))
		if self.starting_door.clicked:
			
			self.starting_door.draw(screen)
			
		else:
			
			if self.player.is_on_fight == False:
				self.normal_room.draw(screen, 3)
				pass
			else:
				
				
				self.normal_room.draw(screen, 0) # put all behind this one pls me
				
				self.player.weapon_equipped[0].Draw(screen)

				
				for draw in self.monster_spawned:
					print(draw - 1)
					if self.monster_spawned[draw - 1].dead == False:
						self.monster_spawned[draw - 1].Draw(screen)

				
						
					

				

			self.player.Draw(screen)


		pygame.display.flip()
		
		


	




pygame.init()
screen = pygame.display.set_mode((700, 700))
game = Game(screen)
game.run()
pygame.quit()
