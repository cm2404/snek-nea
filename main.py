# https://www.youtube.com/watch?v=QFvqStqPCRU&t=2869s

import pygame, sys, random
from pygame.math import Vector2

# Control mappings
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
BG_COLOUR = (202,234,3)
SNEK_COLOUR = (39,59,0)
FOOD_COLOUR = (255,0,0)

# Board size stuff
CELL_SIZE = 30 # length and height of cell in pixels
CELL_NUMBER = 20 # number of cells on each row

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction =  Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos,y_pos,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen, SNEK_COLOUR, block_rect)

    def snake_move(self):
        if self.new_block == True:
            copy_body = self.body[:]
            copy_body.insert(0,copy_body[0] + self.direction)
            self.body = copy_body[:]
            self.new_block = False
        else:
            copy_body = self.body[:-1]
            copy_body.insert(0,copy_body[0] + self.direction)
            self.body = copy_body[:]


    def add_block(self):
        self.new_block = True

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

class Main:
    def __init__(self) -> None:
        self.snake = Snake()
        self.food = Food()

    def update(self):
        self.snake.snake_move()
        self.check_collision()

    def draw_elements(self):
          self.food.draw_food()
          self.snake.draw_snake()

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            print('snack')
            self.food.randomise()
            self.snake.add_block()

screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
pygame.display.set_caption('Snek')

screen.fill(BG_COLOUR)
pygame.display.flip()

# clock
clock = pygame.time.Clock()

game = Main()

UPDATE_SCREEN = pygame.USEREVENT
pygame.time.set_timer(UPDATE_SCREEN,150)

#game loop
while True:
    # Process input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == UPDATE_SCREEN:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key in CONTROLS_UP and game.snake.direction != DIRECTION_DOWN:
                game.snake.direction = DIRECTION_UP
            if event.key in CONTROLS_DOWN and game.snake.direction != DIRECTION_UP:
                game.snake.direction = DIRECTION_DOWN
            if event.key in CONTROLS_LEFT and game.snake.direction != DIRECTION_RIGHT:
                game.snake.direction = DIRECTION_LEFT
            if event.key in CONTROLS_RIGHT and game.snake.direction != DIRECTION_LEFT:
               game.snake.direction = DIRECTION_RIGHT

    # Update
    # check for collisions
    

    # Render
    screen.fill(BG_COLOUR)
    game.draw_elements()
    pygame.display.update()
    clock.tick(60)

