import pygame

class Snake:
    def __init__(self, display_width, display_height, block_size):
        self.display_width = display_width
        self.display_height = display_height
        self.block_size = block_size
        self.direction = 'RIGHT'
        self.head_position = [display_width // 2, display_height // 2]
        self.body_segments = [self.head_position[:]]
        self.growing = False

    def move(self):
        if self.direction == 'UP':
            self.head_position[1] -= self.block_size
        elif self.direction == 'DOWN':
            self.head_position[1] += self.block_size
        elif self.direction == 'LEFT':
            self.head_position[0] -= self.block_size
        elif self.direction == 'RIGHT':
            self.head_position[0] += self.block_size

        self.body_segments.insert(0, self.head_position[:])
        if not self.growing:
            self.body_segments.pop()
        else:
            self.growing = False  # Reset the growing state after growth

    def change_direction(self, new_direction):
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            # Prevent the snake from reversing directly
            if new_direction != opposite_directions.get(self.direction):
                self.direction = new_direction

    def grow(self):
        self.growing = True  # Indicate that the snake should grow on the next move

    def draw_snake(self, display, color):
        for segment in self.body_segments:
            pygame.draw.rect(display, color, [segment[0], segment[1], self.block_size, self.block_size])

    def check_wall_collision(self):
        """
        Check if the snake's head has collided with the wall.
        :return: True if collision detected, False otherwise
        """
        if (self.head_position[0] >= self.display_width or self.head_position[0] < 0 or
                self.head_position[1] >= self.display_height or self.head_position[1] < 0):
            return True
        return False

    def check_self_collision(self):
        """
        Check if the snake's head has collided with its body.
        :return: True if collision detected, False otherwise
        """
        for segment in self.body_segments[1:]:
            if self.head_position == segment:
                return True
        return False
