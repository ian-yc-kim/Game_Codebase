import pygame
import random

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Snake settings
SNAKE_SPEED = 15
SNAKE_BLOCK_SIZE = 10

# Initial score
INITIAL_SCORE = 0

# Game clock
CLOCK = pygame.time.Clock()

# Initial snake position
INITIAL_SNAKE_POSITION = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]

# Initial movement direction
INITIAL_DIRECTION = [0, 0]

# Initial snake body list
INITIAL_SNAKE_BODY = [[SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]]

# Initial food position
INITIAL_FOOD_POSITION = [round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE) / 10.0) * 10.0, round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE) / 10.0) * 10.0]

# Initial score counter
INITIAL_SCORE_COUNTER = 0
