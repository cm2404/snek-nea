import pygame, random
from pygame.math import Vector2
from constants import *


class Food:
    def __init__(self):
        self.randomise()

    def draw_food(self, screen):
        # compute the position rectangle and then draw it
        food_rect = pygame.Rect(
            self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
        )
        pygame.draw.rect(screen, FOOD_COLOUR, food_rect)

    def randomise(self):
        # pick a random position on the board to place the food
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
