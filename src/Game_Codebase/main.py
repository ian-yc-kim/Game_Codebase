import pygame
import random
from .constants import *
from .snake import Snake

# Initialize Pygame
pygame.init()

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


def message(display, msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])


def gameLoop():
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()

    game_over = False
    game_close = False

    snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_BLOCK_SIZE)

    foodx = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE) / 10.0) * 10.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE) / 10.0) * 10.0

    score = 0

    while not game_over:

        while game_close:
            display.fill(BLUE)
            message(display, 'You Lost! Press Q-Quit or C-Play Again', RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')
                elif event.key == pygame.K_UP:
                    snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')

        snake.move()

        if (snake.head_position[0] >= SCREEN_WIDTH or snake.head_position[0] < 0 or
                snake.head_position[1] >= SCREEN_HEIGHT or snake.head_position[1] < 0):
            game_close = True

        # Check for collision with self
        for segment in snake.body_segments[1:]:
            if snake.head_position == segment:
                game_close = True

        display.fill(WHITE)
        pygame.draw.rect(display, GREEN, [foodx, foody, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])

        snake.draw_snake(display, BLACK)
        display_score(display, score)
        pygame.display.update()

        # Check for collision with food
        if snake.head_position[0] == foodx and snake.head_position[1] == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE) / 10.0) * 10.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE) / 10.0) * 10.0
            snake.grow()
            score += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


def display_score(display, score):
    global score_font
    if score_font is None:
        score_font = pygame.font.SysFont(None, 35)
    value = score_font.render('Your Score: ' + str(score), True, BLACK)
    display.blit(value, [10, 10])


def main():
    gameLoop()

if __name__ == '__main__':
    main()
