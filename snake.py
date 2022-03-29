import pygame
from pygame.math import Vector2
from constants import *


class Snake:
    def __init__(self):
        # stores positions of each part of the snake
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]

        # stores the snake's direction of motion
        self.direction = Vector2(0, 0)

        # flags whether to add a new block the next time the snake moves
        self.new_block = False

        # sound effects
        self.snake_sound = pygame.mixer.Sound("beep.mp3")
        self.snake_death = pygame.mixer.Sound("death.mp3")

    def draw_snake(self, screen):
        # draw each block of the snake to the screen
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, SNEK_COLOUR, block_rect)

    def snake_move(self):
        # move the snake
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
        # set the new block flag
        self.new_block = True

    def play_snake_sound(self):
        # play sound for collecting apple
        self.snake_sound.play()

    def play_snake_death(self):
        # play death sound
        self.snake_death.play()

    def reset(self):
        # reset the position and movement direction of the snake
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        # self.play_snake_death()
