import pytest
import pygame
from Game_Codebase.food import generate_food, draw_food
from Game_Codebase.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_BLOCK_SIZE


def test_generate_food():
    snake_body = [[100, 100], [110, 100], [120, 100]]
    food_position = generate_food(snake_body)
    assert food_position not in snake_body
    assert 0 <= food_position[0] < SCREEN_WIDTH
    assert 0 <= food_position[1] < SCREEN_HEIGHT
    assert food_position[0] % SNAKE_BLOCK_SIZE == 0
    assert food_position[1] % SNAKE_BLOCK_SIZE == 0


def test_draw_food():
    pygame.init()
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    food_position = [100, 100]
    color = (0, 255, 0)
    draw_food(display, food_position, color)
    pygame.quit()
