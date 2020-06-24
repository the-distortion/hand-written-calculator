import pygame

def setCursor():
	_DEFAULT_CURSOR = (
	    "                        ",
	    "                        ",
	    "   XXXXXXXXXXXXXXXXXX   ",
		"  X                  X  ",
		"  X                  X  ",
		"  X                  X  ",
		"  X                  X  ",
		"  X                  X  ",
		"  X                  X  ",
		"  X        XX        X  ",
		"  X        XX        X  ",
		"  X      XXXXXX      X  ",
		"  X      XXXXXX      X  ",
		"  X        XX        X  ",
		"  X        XX        X  ",
		"  X                  X  ",
		"  X                  X  ",
		"  X                  X  ",
		"  X                  X  ",
		"  X                  X  ",
		"  X                  X  ",
		"   XXXXXXXXXXXXXXXXXX   ",
		"                        ",
		"                        ",
	)	#size of square including X=20

	default = [(24, 24), (0,0)] + list(pygame.cursors.compile(_DEFAULT_CURSOR))
	pygame.mouse.set_cursor(*default)