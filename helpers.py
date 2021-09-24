#!/usr/bin/env python3

import cmd, textwrap
from os import system, name
from settings import *
from kitten import *

def viewPet():
	borderBreak()
	print(theKittens[PET][FRAME1])
	borderBreak()
	print('XP: %s - AGE: %s' % (theKittens[PET][XP], theKittens[PET][AGE]))
	print('Description: %s' % (theKittens[PET][DESC]))
	print('Holding: %s' % (theKittens[PET][HOLDING][0]))
	borderBreak()
	
def clear():
	
		# for windows
		if name == 'nt':
				_ = system('cls')
			
		# for mac and linux(here, os.name is 'posix')
		else:
				_ = system('clear')
			
def wrapPrint(txt):
	print('\n'.join(textwrap.wrap(txt, SCREEN_WIDTH)))
	
def titlePrint(title):
	MIDDLE = ((SCREEN_WIDTH/2) - (len(title)/2))-1
	borderBreak()
	newlineBorder()
	print('%s%s%s%s%s' % ('=',' ' * int(MIDDLE), title, ' ' * int(MIDDLE),'='))
	newlineBorder()
	borderBreak()
	
def centerText(txt, border):	
	if border == True:
		MIDDLE = ((SCREEN_WIDTH/2) - (len(txt)/2))-1
		print('%s%s%s%s%s' % ('=',' ' * int(MIDDLE), txt, ' ' * int(MIDDLE),'='))
	else:
		MIDDLE = ((SCREEN_WIDTH/2) - (len(txt)/2))
		print('%s%s%s' % (' ' * int(MIDDLE), txt, ' ' * int(MIDDLE),))
		
def newlineBorder():
	print('%s%s%s' % ('=',' ' * (SCREEN_WIDTH-2),'='))
	
def borderBreak():
	print('=' * SCREEN_WIDTH)
	