import pytest
import pygame
from Game_Codebase.snake import Snake


def test_snake_initialization():
    snake = Snake(600, 400, 10)
    assert snake.head_position == [300, 200]
    assert snake.body_segments == [[300, 200]]
    assert snake.direction == 'RIGHT'


def test_snake_move_right():
    snake = Snake(600, 400, 10)
    snake.move()
    assert snake.head_position == [310, 200]
    assert snake.body_segments == [[310, 200]]


def test_snake_move_left():
    snake = Snake(600, 400, 10)
    snake.change_direction('LEFT')
    snake.move()
    assert snake.head_position == [290, 200]
    assert snake.body_segments == [[290, 200]]


def test_snake_move_up():
    snake = Snake(600, 400, 10)
    snake.change_direction('UP')
    snake.move()
    assert snake.head_position == [300, 190]
    assert snake.body_segments == [[300, 190]]


def test_snake_move_down():
    snake = Snake(600, 400, 10)
    snake.change_direction('DOWN')
    snake.move()
    assert snake.head_position == [300, 210]
    assert snake.body_segments == [[300, 210]]


def test_snake_grow():
    snake = Snake(600, 400, 10)
    initial_length = len(snake.body_segments)
    snake.grow()
    assert len(snake.body_segments) == initial_length + 1


def test_draw_snake():
    pygame.init()
    display = pygame.display.set_mode((600, 400))
    snake = Snake(600, 400, 10)
    snake.draw_snake(display, (0, 255, 0))
    pygame.quit()
