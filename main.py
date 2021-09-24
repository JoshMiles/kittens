#!/usr/bin/env python3
from helpers import *

# Main loop

class KittenType(cmd.Cmd):
	prompt = '\n> '
	
	def default(self, arg):
		clear()
		print("I know nothing tf")

	# Actionable methods

	def do_quit(self, arg):
		return True
	
	def do_view(self, arg):
		viewPet()
	
	# Help methods
	
	def help_quit(self):
		print('Quit the game :)')
	
	def help_combat(self):
		print('you want kittens to fight? tf')


if __name__ == '__main__':
	titlePrint('KittenType')
	centerText('%s: %s' % (VERSION_TYPE, VERSION), True)
	borderBreak()
	centerText('(Type "help" for commands.)', False)
	print()
	KittenType().cmdloop()
	print('lol bye')
	