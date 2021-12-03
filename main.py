# https://www.youtube.com/watch?v=QFvqStqPCRU&t=2869s

import pygame, sys, random
from pygame.math import Vector2

# Control mappings
CONTROLS_UP = set([pygame.K_UP, pygame.K_w, pygame.K_i])
CONTROLS_DOWN = set([pygame.K_DOWN, pygame.K_s, pygame.K_k])
CONTROLS_LEFT = set([pygame.K_LEFT, pygame.K_a, pygame.K_j])
CONTROLS_RIGHT = set([pygame.K_RIGHT, pygame.K_d, pygame.K_l])

# Colours
BG_COLOUR = (202,234,3)

# Board size stuff
CELL_SIZE = 30 # length and height of cell in pixels
CELL_NUMBER = 20 # number of cells on each row


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction =  Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos,y_pos,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen, (39,59,0), block_rect)

    def snake_move(self):
        copy_body = self.body[:-1]
        copy_body.insert(0,copy_body[0] + self.direction)
        self.body = copy_body[:]
 
        

class FOOD:
    def __init__(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_food(self):
        food_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen,(255,0,0),food_rect)

screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
pygame.display.set_caption('Snek')

screen.fill(BG_COLOUR)
pygame.display.flip()

# clock
clock = pygame.time.Clock()

food = FOOD()
snake = SNAKE()

UPDATE_SCREEN = pygame.USEREVENT
pygame.time.set_timer(UPDATE_SCREEN,150)

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == UPDATE_SCREEN:
            snake.snake_move()
        if event.type == pygame.KEYDOWN:
            if event.key in CONTROLS_UP:
                snake.direction = Vector2(0,-1)
            if event.key in CONTROLS_DOWN:
                snake.direction = Vector2(0,1)
            if event.key in CONTROLS_LEFT:
                snake.direction = Vector2(-1,0)
            if event.key in CONTROLS_RIGHT:
                snake.direction = Vector2(1,0)
    
    screen.fill(BG_COLOUR)
    food.draw_food()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)

