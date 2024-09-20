import pytest
from Game_Codebase.snake import Snake

@pytest.fixture
def snake():
    return Snake(100, 100, 10)


def test_initial_position(snake):
    assert snake.head_position == [50, 50]
    assert snake.body_segments == [[50, 50]]


def test_move(snake):
    old_head_position = snake.head_position.copy()
    snake.move()
    assert snake.head_position != old_head_position, 'Snake did not move.'


def test_change_direction(snake):
    snake.change_direction('UP')
    assert snake.direction == 'UP', f"Expected direction 'UP', got '{snake.direction}'"
    snake.change_direction('DOWN')
    assert snake.direction == 'UP', f"Expected direction 'UP', got '{snake.direction}'"
    snake.change_direction('LEFT')
    assert snake.direction == 'LEFT', f"Expected direction 'LEFT', got '{snake.direction}'"
    snake.change_direction('RIGHT')
    assert snake.direction == 'LEFT', f"Expected direction 'LEFT', got '{snake.direction}'"


def test_grow(snake):
    initial_length = len(snake.body_segments)
    snake.grow()
    snake.move()
    assert len(snake.body_segments) == initial_length + 1, 'Snake did not grow after eating food.'


def test_no_reverse(snake):
    initial_direction = snake.direction  # Should be 'RIGHT' by default
    snake.change_direction('LEFT')  # Attempt to reverse direction
    assert snake.direction == initial_direction, f"Direction should remain '{initial_direction}' when attempting to reverse. Got '{snake.direction}'"
