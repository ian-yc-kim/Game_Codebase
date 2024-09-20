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


def test_check_wall_collision(snake):
    snake.head_position = [0, 0]
    assert not snake.check_wall_collision(), 'Snake should not collide with wall at initial position.'
    snake.head_position = [-10, 0]
    assert snake.check_wall_collision(), 'Snake should collide with left wall.'
    snake.head_position = [0, -10]
    assert snake.check_wall_collision(), 'Snake should collide with top wall.'
    snake.head_position = [100, 0]
    assert snake.check_wall_collision(), 'Snake should collide with right wall.'
    snake.head_position = [0, 100]
    assert snake.check_wall_collision(), 'Snake should collide with bottom wall.'


def test_check_self_collision(snake):
    snake.body_segments = [[50, 50], [40, 50], [30, 50]]
    snake.head_position = [40, 50]
    assert snake.check_self_collision(), 'Snake should collide with itself.'
    snake.head_position = [20, 50]
    assert not snake.check_self_collision(), 'Snake should not collide with itself.'
