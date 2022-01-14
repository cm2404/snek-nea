import atexit
from tkinter import CENTER
import pygame
import time
import sys

from pygame import font

from constants import *
from snake import Snake
from food import Food


class Game:
    def __init__(self):
        """Initialise pygame and gameplay related classes"""

        # Initialise pygame
        pygame.init()

        # Display
        self.screen = pygame.display.set_mode(
            (CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE)
        )
        pygame.display.set_caption("Snek")

        # Timing stuff
        self.clock = pygame.time.Clock()
        self.update_event_id = pygame.USEREVENT
        pygame.time.set_timer(self.update_event_id, UPDATE_EVENT_INTERVAL)

        # Text
        self.game_font = pygame.font.Font("Minecrafter.Reg.ttf", 40)

        # Gameplay related code
        self.snake = Snake()
        self.food = Food()

        # Add trailing new line to debug FPS output
        if DEBUG_OUTPUT:
            atexit.register(lambda: print())

    def update(self):
        self.snake.snake_move()
        self.check_collision()
        self.check_fail()

    def render(self):
        self.screen.fill(BG_COLOUR)
        self.draw_elements()
        pygame.display.update()

    def draw_elements(self):
        self.food.draw_food(self.screen)
        self.snake.draw_snake(self.screen)
        self.draw_score()

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomise()
            self.snake.add_block()

    def check_fail(self):
        if (not 0 <= self.snake.body[0].x < CELL_NUMBER) or (
            not 0 <= self.snake.body[0].y < CELL_NUMBER
        ):
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(CELL_SIZE * CELL_NUMBER - 60)
        score_y = int(CELL_SIZE * CELL_NUMBER - 40)
        score_rect = score_surface.get_rect()
        self.screen.blit(score_surface, score_rect)

    def loop(self):
        while True:
            for event in pygame.event.get():
                # Input events
                if event.type == pygame.KEYDOWN:
                    if (
                        event.key in CONTROLS_UP
                        and self.snake.direction != DIRECTION_DOWN
                    ):
                        self.snake.direction = DIRECTION_UP
                    elif (
                        event.key in CONTROLS_DOWN
                        and self.snake.direction != DIRECTION_UP
                    ):
                        self.snake.direction = DIRECTION_DOWN
                    elif (
                        event.key in CONTROLS_LEFT
                        and self.snake.direction != DIRECTION_RIGHT
                    ):
                        self.snake.direction = DIRECTION_LEFT
                    elif (
                        event.key in CONTROLS_RIGHT
                        and self.snake.direction != DIRECTION_LEFT
                    ):
                        self.snake.direction = DIRECTION_RIGHT

                # Update game state
                elif event.type == self.update_event_id:
                    self.update()

                # Application has been requested to close
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if DEBUG_OUTPUT:
                print(f"\rFPS: {self.clock.get_fps():.0f}", end="")

            self.render()
            self.clock.tick()
