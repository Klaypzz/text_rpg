import os
import random
import time
#from player.human import Human (import from another file)

races = [
	'Human',
	'Elf',
	'Dwarf',
]

def choose_race():
	character_choice = input('Choose race\n')
	cc = character_choice.lower().replace(character_choice[0].lower(), character_choice[0].upper(), 1)
	#print(cc)
	if cc in races:
		#string.replace(oldvalue, newvalue, count)
		#list.index(elmnt)
		print('You chose {} as your race.'.format(cc))
	else:
		print('Not a race.\nTry Again.')
		time.sleep(1)


def main_menu():
	os.system('cls')
	print('Text RPG')
	print('New Game')
	menu_choice = input('>>')

	if menu_choice == '1':
		choose_race()


def main_loop():
	main_menu()

if __name__ == '__main__':
	main_loop()
