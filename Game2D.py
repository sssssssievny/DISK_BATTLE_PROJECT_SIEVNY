import pygame
from Board import *

pygame.init()

SQUARESIZE = 100

width = BOARD_COLUMN * SQUARESIZE
height = (BOARD_ROW+1) * SQUARESIZE

size = (width,height)

screen = pygame.display.set_mode(size)