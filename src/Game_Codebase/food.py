import random
import pygame
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_BLOCK_SIZE


def generate_food(snake_body):
    while True:
        food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE) / 10.0) * 10.0
        food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE) / 10.0) * 10.0
        food_position = [food_x, food_y]
        if food_position not in snake_body:
            return food_position


def draw_food(display, food_position, color):
    pygame.draw.rect(display, color, [food_position[0], food_position[1], SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])
