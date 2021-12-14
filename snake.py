import pygame
from pygame.math import Vector2
from constants import *


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self, screen):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, SNEK_COLOUR, block_rect)

    def snake_move(self):
        if self.new_block == True:
            copy_body = self.body[:]
            copy_body.insert(0, copy_body[0] + self.direction)
            self.body = copy_body[:]
            self.new_block = False
        else:
            copy_body = self.body[:-1]
            copy_body.insert(0, copy_body[0] + self.direction)
            self.body = copy_body[:]

    def add_block(self):
        self.new_block = True