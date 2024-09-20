import pytest
import random
from src.Game_Codebase.constants import *


def test_screen_dimensions():
    assert SCREEN_WIDTH == 600
    assert SCREEN_HEIGHT == 400


def test_colors():
    assert WHITE == (255, 255, 255)
    assert YELLOW == (255, 255, 102)
    assert BLACK == (0, 0, 0)
    assert RED == (213, 50, 80)
    assert GREEN == (0, 255, 0)
    assert BLUE == (50, 153, 213)


def test_snake_settings():
    assert SNAKE_SPEED == 15
    assert SNAKE_BLOCK_SIZE == 10


def test_initial_score():
    assert INITIAL_SCORE == 0


def test_initial_snake_position():
    assert INITIAL_SNAKE_POSITION == [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]


def test_initial_direction():
    assert INITIAL_DIRECTION == [0, 0]


def test_initial_snake_body():
    assert INITIAL_SNAKE_BODY == [[SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]]


def test_initial_food_position():
    food_x, food_y = INITIAL_FOOD_POSITION
    assert 0 <= food_x < SCREEN_WIDTH
    assert 0 <= food_y < SCREEN_HEIGHT
    assert food_x % 10 == 0
    assert food_y % 10 == 0


def test_initial_score_counter():
    assert INITIAL_SCORE_COUNTER == 0
