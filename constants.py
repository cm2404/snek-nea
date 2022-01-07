import pygame
from pygame.math import Vector2

# Control mappings
CONTROLS_GAME_START = set([pygame.K_SPACE])
CONTROLS_UP = set([pygame.K_UP, pygame.K_w, pygame.K_i])
CONTROLS_DOWN = set([pygame.K_DOWN, pygame.K_s, pygame.K_k])
CONTROLS_LEFT = set([pygame.K_LEFT, pygame.K_a, pygame.K_j])
CONTROLS_RIGHT = set([pygame.K_RIGHT, pygame.K_d, pygame.K_l])

# Direction vectors
DIRECTION_UP = Vector2(0, -1)
DIRECTION_DOWN = Vector2(0, 1)
DIRECTION_LEFT = Vector2(-1, 0)
DIRECTION_RIGHT = Vector2(1, 0)

# Colours
BG_COLOUR = (202, 234, 3)
SNEK_COLOUR = (39, 59, 0)
FOOD_COLOUR = (255, 0, 0)

# Board size stuff
CELL_SIZE = 30  # length and height of cell in pixels
CELL_NUMBER = 20  # number of cells on each row

# How often to update the game state in ms
UPDATE_EVENT_INTERVAL = 150

# Print debug output to console (at the moment this only displays FPS)
DEBUG_OUTPUT = True
