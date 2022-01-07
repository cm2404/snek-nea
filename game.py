import atexit
import pygame
import time
import sys

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

        # Gameplay related code
        self.snake = Snake()
        self.food = Food()

        # This flag indicates whether
        # the game should update it's state or not
        self.running = False

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
        pygame.quit()
        sys.exit()
        # check if snake is outside of screen
        # check if snake hits itself

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

                    elif event.key in CONTROLS_GAME_START:
                        # We should now start the game
                        self.running = True

                # Update game state
                elif event.type == self.update_event_id and self.running:
                    self.update()

                # Application has been requested to close
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if DEBUG_OUTPUT:
                print(f"\rFPS: {self.clock.get_fps():.0f}", end="")

            self.render()
            self.clock.tick()
