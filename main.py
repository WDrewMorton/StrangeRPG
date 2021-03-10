# Strange RPG
# 
# Created:		10/26/2020
# Author:		Drew
# 
# In this RPG the main character will explore a haunted mansion filled with monsters.
# Rooms will be random, to provide better replayability. The main character will be a 
# warrior with a non-significant background.

import sys # Only used to close the program while it is a text based.
import random

def main():
	pass

if __name__ == '__main__':
    main()
'''
What do I need to start? 
- Player : Name, Health, Room, State, Actions[Move[], Attack, Rest]

Endless Mode: 
- No movement
- 100 floors
- Every 10th floor boss
- Hp increase for all monsters by 10%
- Every middle floor actions[rest, continue]
-- Rest restore up to half max hp
'''
class Character:
	def __init__(self):
		self.name = ""
		self.health = 1
		self.health_max = 1
		# self.power = 0

class Player(Character):
	def __init__(self):
		Character.__init__(self)
		self.health = 25
		self.health_max = 25
		self.power = 2
		self.job = None
	def attack(self):
		print("{} attacks fiercely!".format(self.name))
	def quit(self):
		sys.exit(0)
	# def inventory(self): 
	# 	print("Here is your inventory!")
class Monster(Character):
	def __init__(self):
		Character.__init__(self)
		self.name = ""
		self.health = 10
		self.health_max = 10
		# self.power = 1
class Zombie(Monster):
	def __init__(self):
		Monster.__init__(self)
		self.name = "Zombie"

class Skeleton(Monster):
	def __init__(self):
		Monster.__init__(self)
		self.name = "Skeleton"

def fight(player, enemy):
	print("TEST You have encoutered {}".format(enemy.name))
	while player.health > 0 and enemy.health > 0:
		print("TEST HP Player {} Enemy {}\n".format(player.health, enemy.health))
		print("What will you do against this monster?")
		line = input("[fight | run] ")
		if line.lower() == "fight" or line[0].lower() == "f":
			player.attack()
			enemy.health = 0
			print("{} has been defeated\n".format(enemy.name))
		elif line.lower() == "run" or line[0].lower() == "r":
			print("You attempt to run!")
			if random.randint(1,100) <= 25:
				print("You have exscaped the monster!\n")
				break
			else:
				print("The fear in your soul has kept your feet from moving!\n")


player_actions = ["quit"]
player = Player()
player.name = input("What is your name? ")
print("Welcome to the endless flow of monsters {}!".format(player.name))
# player.job=print("Are you an Ogre, Warlock, or Vampire? [ogre, warlock, vampire]")
print("You currently have {} health and {} power.\n".format(player.health, player.power))

world_level = 0
print("You walk into the front door of the mansion.\n Welcome to floor 1. Climb as high" 
	+ " as you can! ")

# while True:
while player.health > 0:
	line = input("~| [quit, explore] ")
	line_actions = line.split()
	if (len(line_actions) > 0) and (len(line_actions) < 2):
		if line_actions[0].lower() == "quit" or line_actions[0].lower() == "q":
			player.quit()
		elif line_actions[0].lower() == "explore" or line_actions[0].lower() == "e":
			# TODO: Create random_monster() function
			r = random.randint(0,2)
			if r == 1:
				# monster_zombie = Zombie()
				monster = Zombie()
				print("A Zombie is on this floor. It must be defeated.")
				fight(player, monster)
			elif r == 2:
				monster = Skeleton()
				print("You find a Skeleton. It must be defeated.")
				fight(player, monster)
			else: # r == 0:
				print("You find an empty roomm. Continue exlporing.")
		else:
			print("{} doesn't know how to follow that command.".format(player.name))
	else:
		print("invalid choice")