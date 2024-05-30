import pygame
import time
from snake import Snake
from food import Food
from leaderboard import load_leaderboard, update_leaderboard, display_leaderboard

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SNAKE_SPEED = 15

def game_over(screen, score, player_name):
    font = pygame.font.SysFont(None, 50)
    text = font.render(f"Game Over! Score: {score}", True, WHITE)
    screen.fill(BLACK)
    screen.blit(text, [SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2])
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds

    # Update leaderboard
    leaderboard = update_leaderboard(player_name, score)

    # Display updated leaderboard
    display_leaderboard(screen, leaderboard)

    # Ask user to quit or play again
    font = pygame.font.SysFont(None, 35)
    text = font.render("Press Q to Quit or R to Restart", True, WHITE)
    screen.blit(text, [SCREEN_WIDTH // 2 - text.get_width() // 2, 50])
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_r:
                    waiting = False

def game_loop(player_name):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                update_leaderboard(player_name, score)
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                snake.change_direction(event.key)

        snake.move()
        if snake.get_head_position() == food.position:
            snake.grow()
            score += 1
            food.randomize_position()

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)

        font = pygame.font.SysFont(None, 35)
        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, [0, 0])

        pygame.display.flip()
        clock.tick(SNAKE_SPEED)

        # Check if snake hits itself
        if snake.positions[0] in snake.positions[1:]:
            game_over(screen, score, player_name)
            running = False

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')

    leaderboard = load_leaderboard()
    display_leaderboard(screen, leaderboard)
    while True:
        game_loop(player_name)
        # Reset score after game over
        score = 0
