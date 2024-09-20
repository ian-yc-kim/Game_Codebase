import pygame
import random
from .constants import *
from .snake import Snake
from .food import generate_food, draw_food

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

    food_position = generate_food(snake.body_segments)

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

        if snake.check_wall_collision():
            game_close = True

        if snake.check_self_collision():
            game_close = True

        display.fill(WHITE)
        draw_food(display, food_position, GREEN)

        snake.draw_snake(display, BLACK)
        display_score(display, score)
        pygame.display.update()

        # Check for collision with food
        if snake.head_position == food_position:
            food_position = generate_food(snake.body_segments)
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


def play_snake_game():
    gameLoop()


def main():
    play_snake_game()


if __name__ == '__main__':
    main()
