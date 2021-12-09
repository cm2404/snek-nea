import pygame, random
from pygame.math  import Vector2
from main import CELL_NUMBER, CELL_SIZE,FOOD_COLOUR, SNEK_COLOUR, screen

class Food:
    def __init__(self):
        self.randomise()

    def draw_food(self):
        food_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, FOOD_COLOUR,food_rect)

    def randomise(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)