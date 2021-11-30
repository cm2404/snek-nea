import pygame, sys
from pygame.math import Vector2

class FOOD:
    def __init__(self):
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x, self.y)

    def draw_food(self):
        food_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen,(255,0,0),food_rect)

# setting up display
back_colour = (202,234,3)

cell_size = 30 # length and height of cell in pixels
cell_number = 20 # number of cells on each row
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption('Snek')

screen.fill(back_colour)
pygame.display.flip()

# clock
clock = pygame.time.Clock()

food = FOOD()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    food.draw_food()
    clock.tick(60)

