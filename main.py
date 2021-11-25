import pygame, sys

# setting up display
back_colour = (202,234,3)
screen = pygame.display.set_mode((300,300))
pygame.display.set_caption('Snek')

screen.fill(back_colour)
pygame.display.flip()

# clock
clock = pygame.time.Clock()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)

