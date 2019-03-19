import sys
import os
import random
import time
from player.human import Human


def character_creation():
	os.system('cls')
	### Choosing Race ###
	for race in races:
		print(race)
	choose_race = input('Choose race\n> ')
	cr = choose_race.lower().replace(choose_race[0].lower(), choose_race[0].upper(), 1)

	### Choosing Class ###
	for role in roles:
		print(role)
	choose_race = input('Choose role\n> ')
	cr = choose_race.lower().replace(choose_race[0].lower(), choose_race[0].upper(), 1)

	### Choosing Name ###
	name = input('Choose a name\n> ')

	if cr in races:
		#string.replace(oldvalue, newvalue, count)
		#list.index(elmnt)
		print('You chose {}'.format(cr))
	else:
		print('Character creation went wrong\nTry Again\nExiting...')
		time.sleep(1)
		sys.exit()

def main_menu():
	os.system('cls')
	print('Text RPG')
	print('New Game')
	menu_choice = input('> ')

	if menu_choice == '1':
		character_creation()


def main_loop():
	main_menu()

if __name__ == '__main__':
	main_loop()
